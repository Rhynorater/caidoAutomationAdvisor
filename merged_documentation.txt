Directory structure:
└── reference/
    ├── config.md
    ├── index.md
    ├── manifest.md
    ├── plugin_packages.md
    ├── cloud/
    │   ├── api.md
    │   └── authentication.md
    ├── modules/
    │   ├── index.md
    │   ├── caido/
    │   │   └── http.md
    │   ├── extra/
    │   │   ├── console.md
    │   │   ├── os.md
    │   │   ├── sqlite.md
    │   │   ├── timers.md
    │   │   └── url.md
    │   └── llrt/
    │       ├── abort.md
    │       ├── buffer.md
    │       ├── child_process.md
    │       ├── crypto.md
    │       ├── dom-events.md
    │       ├── net.md
    │       ├── process.md
    │       ├── stream.md
    │       ├── fs/
    │       │   ├── index.md
    │       │   ├── fs/
    │       │   │   └── promises.md
    │       │   └── namespaces/
    │       │       └── constants.md
    │       ├── globals/
    │       │   ├── index.md
    │       │   └── namespaces/
    │       │       └── QuickJS.md
    │       └── path/
    │           ├── index.md
    │           └── namespaces/
    │               └── export=.md
    └── sdks/
        ├── backend/
        │   └── index.md
        ├── frontend/
        │   └── index.md
        └── workflow/
            └── index.md

================================================
FILE: src/reference/config.md
================================================
# caido.config.ts

The `caido.config.ts` file is used to configure your package.
It will used to generate the [`manifest.json`](./manifest.md) automatically.

```ts
import { defineConfig } from "@caido-community/dev";

export default defineConfig({
  id: "my-plugin",
  name: "My Plugin",
  description: "A plugin for Caido",
  version: "0.0.0",
  author: {
    name: "Caido Labs Inc.",
    email: "dev@caido.io",
    url: "https://caido.io",
  },
  plugins: [
    {
      kind: "frontend",
      id: "my-frontend",
      name: "My Frontend",
      root: "packages/my-frontend",
      backend: {
        id: "my-backend",
      },
      assets: ["my-assets/*.png"],
    },
    {
      kind: "backend",
      id: "my-backend",
      name: "My Backend",
      root: "packages/my-backend",
    },
  ],
});
```

## Global Options

| Option      | Type     | Required | Description                                                                                                                                                            |
| ----------- | -------- | -------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| id          | `string` | Yes      | Must be unique and must only consist of lowercase letters, numbers, hyphens and underscores (the order of which must satisfy the regex: `^[a-z]+(?:[_-][a-z0-9]+)*$`). |
| name        | `string` | Yes      | The name of your plugin. This is the name that will be displayed when a user installs your plugin.                                                                     |
| description | `string` | Yes      | The description of your plugin. This is the description that will be displayed when a user installs your plugin.                                                       |
| version     | `string` | Yes      | Represents the version of your plugin using [Semantic Versioning](https://semver.org/).                                                                                |

## Author Options

| Option | Type     | Required | Description                             |
| ------ | -------- | -------- | --------------------------------------- |
| name   | `string` | Yes      | The name of the author of your plugin.  |
| email  | `string` | No       | The email of the author of your plugin. |
| url    | `string` | No       | The URL of the author of your plugin.   |

## Frontend Plugin Options

| Option     | Type                                     | Required | Description                                                                                 |
| ---------- | ---------------------------------------- | -------- | ------------------------------------------------------------------------------------------- |
| kind       | `"frontend"`                             | Yes      | The kind of plugin.                                                                         |
| id         | `string`                                 | Yes      | The id of the plugin.                                                                       |
| name       | `string`                                 | No       | The name of the plugin. Defaults to the id.                                                 |
| root       | `string`                                 | Yes      | The root directory of the frontend plugin. (e.g. `packages/my-frontend`)                    |
| backend.id | `string`                                 | Yes      | The id of the backend plugin that this frontend plugin is associated with.                  |
| vite       | [`ViteConfig`](https://vite.dev/config/) | No       | Additional Vite configuration for the frontend plugin.                                      |
| assets     | `Array<string>`                          | No       | Assets to package with the plugin. Supports glob for files and directories (recursive copy) |

## Backend Plugin Options

| Option | Type            | Required | Description                                                                                 |
| ------ | --------------- | -------- | ------------------------------------------------------------------------------------------- |
| kind   | `"backend"`     | Yes      | The kind of plugin.                                                                         |
| id     | `string`        | Yes      | The id of the plugin.                                                                       |
| name   | `string`        | No       | The name of the plugin. Defaults to the id.                                                 |
| root   | `string`        | Yes      | The root directory of the backend plugin. (e.g. `packages/my-backend`)                      |
| assets | `Array<string>` | No       | Assets to package with the plugin. Supports glob for files and directories (recursive copy) |



================================================
FILE: src/reference/index.md
================================================
# Reference

The reference section contains the auto-generated documentation for the frontend, backend, and workflow SDKs, as well as field definitions for various files.

If you need a refresher on how a function works, or whether a certain feature is possible within plugins, this is the place to look.

## SDKs

- **[Backend SDK](./sdks/backend/index.md)** - Backend Software Development Kit.
- **[Frontend SDK](./sdks/frontend/index.md)** - Frontend Software Development Kit.
- **[Workflow SDK](./sdks/workflow/index.md)** - Workflow Software Development Kit.

## Runtime

- **[Backend Modules](./modules/index.md)** - Backend modules

## Files

- **[caido.config.ts](./config.md)** - caido.config.ts field definitions
- **[plugin_packages.json](./plugin_packages.md)** - plugin_packages.json field definitions
- **[manifest.json](./manifest.md)** - Manifest.json field definitions



================================================
FILE: src/reference/manifest.md
================================================
# manifest.json

The `manifest.json` file is the first file that is read by the Caido application when a plugin is installed. It defines the plugin's structure and contains metadata used by the Caido installer.

```json
{
  "id": "authmatrix",
  "name": "AuthMatrix",
  "version": "0.2.0",
  "description": "Grid-based authorization testing across multiple users and roles.",
  "author": {
    "name": "Caido Labs Inc.",
    "email": "dev@caido.io",
    "url": "https://github.com/caido-community/authmatrix"
  },
  "links": {
    "sponsor": "https://patreon.com/..."
  },
  "plugins": [
    {
      "kind": "frontend",
      "id": "authmatrix-frontend",
      "name": "Authmatrix Frontend",
      "entrypoint": "frontend/script.js",
      "style": "frontend/style.css",
      "backend": {
        "id": "authmatrix-backend"
      },
      "assets": "frontend/assets"
    },
    {
      "kind": "backend",
      "id": "authmatrix-backend",
      "name": "Authmatrix Backend",
      "runtime": "javascript",
      "entrypoint": "backend/script.js",
      "assets": "frontend/assets"
    },
    {
      "kind": "workflow",
      "id": "authmatrix-workflow",
      "name": "Authmatrix Workflow",
      "definition": "workflow/definition.json"
    }
  ]
}
```

Here's a summary of each field (**required** fields are marked with an asterisk `*`)

## Main Fields

| Field       | Required | Description                                                                                                                                                                                            |
| ----------- | -------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| id          | Yes      | Must be **unique** and must only consist of **lowercase** letters, **numbers**, **hyphens** and **underscores** (_the order of which must satisfy the regex: `^[a-z][a-z0-9]+(?:[_-][a-z0-9]+)\*$`\_). |
| version     | Yes      | The version of your plugin package. Follows the `MAJOR.MINOR.PATCH` syntax.                                                                                                                            |
| name        | No       | The name of your plugin package. If not supplied, the `id` will be used as the `name`.                                                                                                                 |
| description | No       | A description of the plugin package .                                                                                                                                                                  |
| Author      | No       | See the [author fields](#author-fields).                                                                                                                                                               |
| Links       | No       | See the [links fields](#links-fields)                                                                                                                                                                                 |
| Plugins     | Yes      | Array of plugins. See the [plugin fields](#plugins-fields).                                                                                                                                            |

## Author Fields

The `author` field is optional and may be used for crediting purposes.

| Field | Required | Description                      |
| ----- | -------- | -------------------------------- |
| name  | No       | The name of the author.          |
| email | No       | The email address of the author. |
| url   | No       | A URL to the author's website.   |

## Links Fields

The `links` field is optional and is currently used to provide users with a funding link.

| Field   | Required | Description                             |
| ------- | -------- | --------------------------------------- |
| sponsor | No       | A URL to the project's funding website. |

## Plugins Fields

The `plugins` field is required and must contain an array of plugins.

Plugins can be of type `frontend`, `backend` or `workflow`.

::: tip
You can define multiple plugins of the same type. For example, you can define 3 different frontend plugins that will interact with the same backend plugin.
:::

### Frontend Plugins

| Field      | Required | Description                                                                                                                                                                                                       |
| ---------- | -------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| kind       | Yes      | Must be of type `frontend`                                                                                                                                                                                        |
| id         | Yes      | Must be **unique** and must only consist of **lowercase** letters, **numbers**, **hyphens** and **underscores** (_the order of which must satisfy the regex: `^[a-z][a-z0-9]+(?:[_-][a-z0-9]+)\*$`).              |
| entrypoint | Yes      | Specifies the location of the primary script to be executed when the plugin is launched.                                                                                                                          |
| name       | No       | The cosmetic plugin package name displayed in the [Plugins](https://docs.caido.io/reference/features/workspace/plugins.html) table. If not supplied, the `id` will be used as the `name`.                         |
| style      | No       | Specifies the location of the CSS file to be used to stylize elements of your plugin.                                                                                                                             |
| backend    | No       | This object contains the `id` of the associated backend plugin. Specifying this field will allow the frontend plugin to communicate with the backend plugin via [sdk.backend](/reference/sdks/frontend/#backend). |
| assets     | No       | Extra assets to be bundled with the plugin and loadable at runtime.                                                                                                                                               |

### Backend Plugins

| Field      | Required | Description                                                                                                                                                                                          |
| ---------- | -------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| kind       | Yes      | Must be of type `backend`                                                                                                                                                                            |
| id         | Yes      | Must be **unique** and must only consist of **lowercase** letters, **numbers**, **hyphens** and **underscores** (_the order of which must satisfy the regex: `^[a-z][a-z0-9]+(?:[_-][a-z0-9]+)\*$`). |
| entrypoint | Yes      | Specifies the location of the primary script to be executed when the plugin is launched.                                                                                                             |
| runtime    | Yes      | Specifies that JavaScript code will be executed.                                                                                                                                                     |
| name       | No       | The name of your plugin. If not supplied, the `id` will be used as the `name`.                                                                                                                       |
| assets     | No       | Extra assets to be bundled with the plugin and loadable at runtime.                                                                                                                                  |

### Workflow Plugins

| Field      | Required | Description                                                                                                                                                                                          |
| ---------- | -------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| kind       | Yes      | Must be of type `workflow`                                                                                                                                                                           |
| id         | Yes      | Must be **unique** and must only consist of **lowercase** letters, **numbers**, **hyphens** and **underscores** (_the order of which must satisfy the regex: `^[a-z][a-z0-9]+(?:[_-][a-z0-9]+)\*$`). |
| definition | Yes      | Specifies the location of workflow json definition.                                                                                                                                                  |
| name       | No       | The name of your plugin. If not supplied, the `id` will be used as the `name`.                                                                                                                       |



================================================
FILE: src/reference/plugin_packages.md
================================================
# plugin_packages.json

The `plugin_packages.json` file in the [caido/store](https://github.com/caido/store) repository contains the metadata for all plugins available in the Caido store.

In order to add your plugin to the store, you'll need to add an entry to this file.

Here's an example of what the `plugin_packages.json` file looks like:

```json
[
  {
    "id": "authmatrix",
    "name": "AuthMatrix",
    "license": "CC0-1.0",
    "description": "Grid-based authorization testing across multiple users and roles.",
    "author": {
      "name": "Caido Labs Inc.",
      "email": "dev@caido.io",
      "url": "https://caido.io"
    },
    "public_key": "MCowBQYDK2VwAyEA+du2fw/I+CV6MKEpu0aJ1ki2+MO2V0SnaRB91+GbHwQ=",
    "repository": "caido-community/authmatrix"
  },
]
```

Here's a summary of each field:

Field|Description
-----|-----
`id`|A unique identifier for your plugin. Search `plugin_packages.json` to confirm that there's no existing plugin with the same id.
`name`|Your plugin's name. This will be used as the display name in the store.
`license`|The license of your plugin.
`description`|A short description of your plugin.
`author`|Author details of your plugin.
`public_key`|The Base64 part of the public key generated in the [Setting up your repository](/guides/distribution/repository#_3-generate-a-key-pair) guide. **Don't** include the header/footer (`BEGIN/END PUBLIC KEY`).
`repository`|The path to your GitHub repository. For example, if your GitHub repo is <https://github.com/username/repo-name>, the path is `username/repo-name`.



================================================
FILE: src/reference/cloud/api.md
================================================
---
aside: true
outline: [1, 1]
title: API
---

<OASpec hide-branding />



================================================
FILE: src/reference/cloud/authentication.md
================================================
# Authentication

To access the public cloud API, you must use Personnal Access Tokens (PAT).
PATs act on your behalf and will have the same set of permissions as you have.
The PATs can be tied to a team to access that team's resources.

## Use to a PAT?

When you send a request to the public cloud API, add the following header:

```http
Authorization: Bearer <PAT>
```

## How to create a PAT?

We currently do not have an interface to create PATs.
For the moment you will have to use our internal GraphQL API.

**Endpoint:** `POST` `https://api.caido.io/dashboard/graphql`
**Authentication:** `CAIDO_SESSION` cookie

```graphql
mutation CreatePat {
  createPat(
    input: {
      name: "<NAME>"
      teamId: "<ENTER TEAM ID>"
      expiresAt: "<OPTIONAL RFC3339 DATETIME>"
    }
  ) {
    pat {
      id
      token
    }
  }
}
```

::: tip

<details>
<summary>To view the curl request, expand the following:</summary>

```bash
echo '{ "query":
  "mutation CreatePat($name: String!, $teamId: ID!) {
      createPat(
        input: {
          name: $name
          teamId: $teamId
        }
      ) {
        pat {
          id
          token
        }
      }
    }",
  "variables": {
    "name": "My PAT",
    "teamId": "01JXP5F0C40WYWSPQS9WAHSB9T"
  }
}' | tr -d '\n' | curl --silent \
https://api.caido.io/dashboard/graphql \
--header "Cookie: CAIDO_SESSION=<SESSION>" \
--header "Content-Type: application/json" \
--data @-
```

</details>
:::

## How to revoke a PAT?

We currently do not have an interface to revoke PATs.
For the moment you will have to use our internal GraphQL API.

**Endpoint:** `POST` `https://api.caido.io/dashboard/graphql`
**Authentication:** `CAIDO_SESSION` cookie

```graphql
mutation RevokePat {
  revokePat(id: "<PAT ID>") {
    pat {
      id
    }
  }
}
```

::: tip

<details>
<summary>To view the curl request, expand the following:</summary>

```bash
echo '{ "query":
  "mutation RevokePat($id: ID!) {
    revokePat(id: $id) {
      pat {
        id
      }
    }
  }",
  "variables": {
    "id": "01JXP5F0C40WYWSPQS9WAHSB9T"
  }
}' | tr -d '\n' | curl --silent \
https://api.caido.io/dashboard/graphql \
--header "Cookie: CAIDO_SESSION=<SESSION>" \
--header "Content-Type: application/json" \
--data @-
```

</details>
:::



================================================
FILE: src/reference/modules/index.md
================================================
# QuickJS Modules

Here is the reference of the modules available in our engine.

This documentation is auto-generated from the Typescript typing ([`@caido/quickjs-types`](https://www.npmjs.com/package/@caido/quickjs-types)) which is the source of truth.

Some elements are similar to `Node.JS`, but some imports will be different and start with `caido:`.

## Modules

| Module                                 | Description              | Import             | Global |
| -------------------------------------- | ------------------------ | ------------------ | ------ |
| [url](extra/url.md)                    | URL utilities            | N/A                | ✔︎     |
| [abort](llrt/abort.md)                 | Abort signaling          | N/A                | ✔︎     |
| [buffer](llrt/buffer.md)               | Buffers                  | `buffer`           | ✔︎     |
| [child_process](llrt/child_process.md) | Process spawning         | `child_process`    | ✘      |
| [console](extra/console.md)            | Console logging          | N/A                | ✔︎     |
| [crypto](llrt/crypto.md)               | Cryptographic primitives | `crypto`           | ✘      |
| [dom-events](llrt/dom-events.md)       | Events                   | N/A                | ✔︎     |
| [fs](llrt/fs/index.md)                 | File system              | `fs`, `fs/promise` | ✘      |
| [http](caido/http.md)                  | Fetch implementation     | `caido:http`       | ✘      |
| [globals](llrt/globals/index.md)       | Global classes           | N/A                | ✔︎     |
| [net](llrt/net.md)                     | Sockets                  | `net`              | ✘      |
| [os](extra/os.md)                      | OS information           | `os`               | ✘      |
| [path](llrt/path/index.md)             | Path transformation      | `path`             | ✘      |
| [process](llrt/process.md)             | Process information      | `process`          | ✔︎     |
| [sqlite](extra/sqlite.md)              | SQlite access            | `sqlite`           | ✘      |
| [stream](llrt/stream.md)               | Streams (basic)          | `stream`           | ✔︎     |
| [timers](extra/timers.md)              | Timers                   | N/A                | ✔︎     |



================================================
FILE: src/reference/modules/caido/http.md
================================================
[@caido/quickjs-types](../index.md) / caido/http

# caido/http

## Classes

### Blob

A [`Blob`](https://developer.mozilla.org/en-US/docs/Web/API/Blob) encapsulates immutable, raw data.

#### Extended by

- [`File`](http.md#file)

#### Constructors

##### new Blob()

> **new Blob**(`parts`: (`string` \| `ArrayBuffer` \| [`Blob`](http.md#blob))[], `opts`?: [`BlobOpts`](http.md#blobopts)): [`Blob`](http.md#blob)

Creates a new `Blob` object containing a concatenation of the given sources.

{ArrayBuffer}, and {Blob} sources are copied into the 'Blob' and can therefore be
safely modified after the 'Blob' is created.

String sources are also copied into the `Blob`.

###### Parameters

| Parameter | Type |
| ------ | ------ |
| `parts` | (`string` \| `ArrayBuffer` \| [`Blob`](http.md#blob))[] |
| `opts`? | [`BlobOpts`](http.md#blobopts) |

###### Returns

[`Blob`](http.md#blob)

#### Properties

##### size

> `readonly` **size**: `number`

The total size of the `Blob` in bytes.

##### type

> `readonly` **type**: `string`

The content-type of the `Blob`.

#### Methods

##### arrayBuffer()

> **arrayBuffer**(): `Promise`\<`ArrayBuffer`\>

Returns a promise that fulfills with an [ArrayBuffer](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/ArrayBuffer) containing a copy of
the `Blob` data.

###### Returns

`Promise`\<`ArrayBuffer`\>

##### bytes()

> **bytes**(): `Promise`\<`Uint8Array`\>

Returns a promise that resolves with an Uint8Array containing the contents of the Blob.

###### Returns

`Promise`\<`Uint8Array`\>

##### slice()

> **slice**(`start`?: `number`, `end`?: `number`, `type`?: `string`): [`Blob`](http.md#blob)

Creates and returns a new `Blob` containing a subset of this `Blob` objects
data. The original `Blob` is not altered.

###### Parameters

| Parameter | Type | Description |
| ------ | ------ | ------ |
| `start`? | `number` | The starting index. |
| `end`? | `number` | The ending index. |
| `type`? | `string` | The content-type for the new `Blob` |

###### Returns

[`Blob`](http.md#blob)

##### text()

> **text**(): `Promise`\<`string`\>

Returns a promise that fulfills with the contents of the `Blob` decoded as a UTF-8 string.

###### Returns

`Promise`\<`string`\>

***

### File

A [`Blob`](https://developer.mozilla.org/en-US/docs/Web/API/Blob) encapsulates immutable, raw data.

#### Extends

- [`Blob`](http.md#blob)

#### Constructors

##### new File()

> **new File**(`data`: (`string` \| `ArrayBuffer` \| [`Blob`](http.md#blob))[], `fileName`: `string`, `opts`?: [`FileOpts`](http.md#fileopts)): [`File`](http.md#file)

Returns a newly constructed File.

###### Parameters

| Parameter | Type |
| ------ | ------ |
| `data` | (`string` \| `ArrayBuffer` \| [`Blob`](http.md#blob))[] |
| `fileName` | `string` |
| `opts`? | [`FileOpts`](http.md#fileopts) |

###### Returns

[`File`](http.md#file)

###### Overrides

[`Blob`](http.md#blob).[`constructor`](http.md#constructors)

#### Properties

##### lastModified

> `readonly` **lastModified**: `number`

The last modified date of the file as the number of milliseconds since the Unix epoch (January 1, 1970 at midnight).
Files without a known last modified date return the current date.

##### name

> `readonly` **name**: `string`

Name of the file referenced by the File object.

##### size

> `readonly` **size**: `number`

The total size of the `Blob` in bytes.

###### Inherited from

[`Blob`](http.md#blob).[`size`](http.md#size)

##### type

> `readonly` **type**: `string`

The content-type of the `Blob`.

###### Inherited from

[`Blob`](http.md#blob).[`type`](http.md#type)

#### Methods

##### arrayBuffer()

> **arrayBuffer**(): `Promise`\<`ArrayBuffer`\>

Returns a promise that fulfills with an [ArrayBuffer](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/ArrayBuffer) containing a copy of
the `Blob` data.

###### Returns

`Promise`\<`ArrayBuffer`\>

###### Inherited from

[`Blob`](http.md#blob).[`arrayBuffer`](http.md#arraybuffer)

##### bytes()

> **bytes**(): `Promise`\<`Uint8Array`\>

Returns a promise that resolves with an Uint8Array containing the contents of the Blob.

###### Returns

`Promise`\<`Uint8Array`\>

###### Inherited from

[`Blob`](http.md#blob).[`bytes`](http.md#bytes)

##### slice()

> **slice**(`start`?: `number`, `end`?: `number`, `type`?: `string`): [`Blob`](http.md#blob)

Creates and returns a new `Blob` containing a subset of this `Blob` objects
data. The original `Blob` is not altered.

###### Parameters

| Parameter | Type | Description |
| ------ | ------ | ------ |
| `start`? | `number` | The starting index. |
| `end`? | `number` | The ending index. |
| `type`? | `string` | The content-type for the new `Blob` |

###### Returns

[`Blob`](http.md#blob)

###### Inherited from

[`Blob`](http.md#blob).[`slice`](http.md#slice)

##### text()

> **text**(): `Promise`\<`string`\>

Returns a promise that fulfills with the contents of the `Blob` decoded as a UTF-8 string.

###### Returns

`Promise`\<`string`\>

###### Inherited from

[`Blob`](http.md#blob).[`text`](http.md#text)

***

### Headers

#### Implements

- `Iterable`\<\[`string`, `string`\]\>

#### Constructors

##### new Headers()

> **new Headers**(`opts`?: [`HeadersOpts`](http.md#headersopts)): [`Headers`](http.md#headers)

Creates a new Headers object.

###### Parameters

| Parameter | Type |
| ------ | ------ |
| `opts`? | [`HeadersOpts`](http.md#headersopts) |

###### Returns

[`Headers`](http.md#headers)

#### Properties

##### \[iterator\]()

> `readonly` **\[iterator\]**: () => `Iterator`\<\[`string`, `string`\]\>

###### Returns

`Iterator`\<\[`string`, `string`\]\>

###### Implementation of

`Iterable.[iterator]`

##### append()

> `readonly` **append**: (`name`: `string`, `value`: `string`) => `void`

Appends a new value onto an existing header inside a Headers object, or adds the header if it does not already exist.

###### Parameters

| Parameter | Type |
| ------ | ------ |
| `name` | `string` |
| `value` | `string` |

###### Returns

`void`

##### delete()

> `readonly` **delete**: (`name`: `string`) => `void`

Deletes a header from a Headers object.

###### Parameters

| Parameter | Type |
| ------ | ------ |
| `name` | `string` |

###### Returns

`void`

##### entries()

> `readonly` **entries**: () => `IterableIterator`\<\[`string`, `string`\]\>

Returns an iterator allowing to go through all key/value pairs contained in this object.

###### Returns

`IterableIterator`\<\[`string`, `string`\]\>

##### forEach()

> `readonly` **forEach**: (`callbackfn`: (`value`: `string`, `key`: `string`) => `void`) => `void`

Executes a provided function once for each key/value pair in this Headers object.

###### Parameters

| Parameter | Type |
| ------ | ------ |
| `callbackfn` | (`value`: `string`, `key`: `string`) => `void` |

###### Returns

`void`

##### get()

> `readonly` **get**: (`name`: `string`) => `null` \| `string`

A String sequence representing the values of the retrieved header or null if this header is not set.

###### Parameters

| Parameter | Type |
| ------ | ------ |
| `name` | `string` |

###### Returns

`null` \| `string`

##### getSetCookie()

> `readonly` **getSetCookie**: () => `string`[]

Returns an array containing the values of all Set-Cookie headers associated with a response.

###### Returns

`string`[]

##### has()

> `readonly` **has**: (`name`: `string`) => `boolean`

Returns a boolean stating whether a Headers object contains a certain header.

###### Parameters

| Parameter | Type |
| ------ | ------ |
| `name` | `string` |

###### Returns

`boolean`

##### keys()

> `readonly` **keys**: () => `IterableIterator`\<`string`\>

Returns an iterator allowing you to go through all keys of the key/value pairs contained in this object.

###### Returns

`IterableIterator`\<`string`\>

##### set()

> `readonly` **set**: (`name`: `string`, `value`: `string`) => `void`

Sets a new value for an existing header inside a Headers object, or adds the header if it does not already exist.

###### Parameters

| Parameter | Type |
| ------ | ------ |
| `name` | `string` |
| `value` | `string` |

###### Returns

`void`

##### values()

> `readonly` **values**: () => `IterableIterator`\<`string`\>

Returns an iterator allowing you to go through all values of the key/value pairs contained in this object.

###### Returns

`IterableIterator`\<`string`\>

***

### Request

The Request interface of the Fetch API represents a resource request.

#### Constructors

##### new Request()

> **new Request**(`input`: `string` \| [`Request`](http.md#request), `init`?: [`RequestOpts`](http.md#requestopts)): [`Request`](http.md#request)

Creates a new Request object.

###### Parameters

| Parameter | Type |
| ------ | ------ |
| `input` | `string` \| [`Request`](http.md#request) |
| `init`? | [`RequestOpts`](http.md#requestopts) |

###### Returns

[`Request`](http.md#request)

#### Properties

##### arrayBuffer()

> `readonly` **arrayBuffer**: () => `Promise`\<`ArrayBuffer`\>

Returns a promise that resolves with an ArrayBuffer representation of the request body.

###### Returns

`Promise`\<`ArrayBuffer`\>

##### blob()

> `readonly` **blob**: () => `Promise`\<[`Blob`](http.md#blob)\>

Returns a promise that resolves with a [Blob](http.md#blob) representation of the request body.

###### Returns

`Promise`\<[`Blob`](http.md#blob)\>

##### body

> `readonly` **body**: [`Body`](http.md#body-3)

The body content.

##### bodyUsed

> `readonly` **bodyUsed**: `boolean`

Stores true or false to indicate whether or not the body has been used in a request yet.

##### bytes()

> `readonly` **bytes**: () => `Promise`\<`Uint8Array`\>

Returns a promise that resolves with a Uint8Array representation of the request body.

###### Returns

`Promise`\<`Uint8Array`\>

##### cache

> `readonly` **cache**: `"no-cache"`

Contains the cache mode of the request

##### clone()

> `readonly` **clone**: () => [`Request`](http.md#request)

Creates a copy of the current [Request](http.md#request) object.

###### Returns

[`Request`](http.md#request)

##### headers

> `readonly` **headers**: [`Headers`](http.md#headers)

Contains the associated Headers object of the request.

##### json()

> `readonly` **json**: () => `Promise`\<`unknown`\>

Returns a promise that resolves with the result of parsing the request body as JSON.

###### Returns

`Promise`\<`unknown`\>

##### keepalive

> `readonly` **keepalive**: `boolean`

Contains the request's keepalive setting (true or false), which indicates whether llrt will
keep the associated connection alive.

##### method

> `readonly` **method**: `string`

Contains the request's method (GET, POST, etc.)

##### mode

> `readonly` **mode**: `"navigate"`

Contains the mode of the request

##### signal

> `readonly` **signal**: [`AbortSignal`](../llrt/abort.md#abortsignal)

Returns the [AbortSignal](../llrt/abort.md#abortsignal) associated with the request

##### text()

> `readonly` **text**: () => `Promise`\<`string`\>

Returns a promise that resolves with a text representation of the request body.

###### Returns

`Promise`\<`string`\>

##### url

> `readonly` **url**: `string`

Contains the URL of the request.

***

### Response

The Response interface of the Fetch API represents the response to a request.

#### Constructors

##### new Response()

> **new Response**(`body`?: [`Body`](http.md#body-3), `opts`?: [`ResponseOpts`](http.md#responseopts)): [`Response`](http.md#response)

Creates a new Response object.

###### Parameters

| Parameter | Type |
| ------ | ------ |
| `body`? | [`Body`](http.md#body-3) |
| `opts`? | [`ResponseOpts`](http.md#responseopts) |

###### Returns

[`Response`](http.md#response)

#### Properties

##### arrayBuffer()

> `readonly` **arrayBuffer**: () => `Promise`\<`ArrayBuffer`\>

Returns a promise that resolves with an ArrayBuffer representation of the response body.

###### Returns

`Promise`\<`ArrayBuffer`\>

##### blob()

> `readonly` **blob**: () => `Promise`\<[`Blob`](http.md#blob)\>

Returns a promise that resolves with a [Blob](http.md#blob) representation of the response body.

###### Returns

`Promise`\<[`Blob`](http.md#blob)\>

##### body

> `readonly` **body**: `null`

The body content (NOT IMPLEMENTED YET).

##### bodyUsed

> `readonly` **bodyUsed**: `boolean`

Stores a boolean value that declares whether the body has been used in a response yet.

##### clone()

> `readonly` **clone**: () => [`Response`](http.md#response)

Creates a clone of a [Response](http.md#response) object.

###### Returns

[`Response`](http.md#response)

##### headers

> `readonly` **headers**: [`Headers`](http.md#headers)

The [Headers](http.md#headers) object associated with the response.

##### json()

> `readonly` **json**: () => `Promise`\<`unknown`\>

Returns a promise that resolves with the result of parsing the response body text as JSON.

###### Returns

`Promise`\<`unknown`\>

##### ok

> `readonly` **ok**: `boolean`

A boolean indicating whether the response was successful (status in the range 200 – 299) or not.

##### redirected

> `readonly` **redirected**: `boolean`

Indicates whether or not the response is the result of a redirect (that is, its URL list has more than one entry).

##### status

> `readonly` **status**: `number`

The status code of the response. (This will be 200 for a success).

##### statusText

> `readonly` **statusText**: `string`

The status message corresponding to the status code. (e.g., OK for 200).

##### text()

> `readonly` **text**: () => `Promise`\<`string`\>

Returns a promise that resolves with a text representation of the response body.

###### Returns

`Promise`\<`string`\>

##### type

> `readonly` **type**: [`ResponseType`](http.md#responsetype)

The type of the response.

##### url

> `readonly` **url**: `string`

#### Methods

##### error()

> `static` **error**(): [`Response`](http.md#response)

Returns a new [Response](http.md#response) object associated with a network error.

###### Returns

[`Response`](http.md#response)

##### json()

> `static` **json**(`data`: `any`, `init`?: [`ResponseInit`](http.md#responseinit)): [`Response`](http.md#response)

Returns a new [Response](http.md#response) object for returning the provided JSON encoded data.

###### Parameters

| Parameter | Type |
| ------ | ------ |
| `data` | `any` |
| `init`? | [`ResponseInit`](http.md#responseinit) |

###### Returns

[`Response`](http.md#response)

##### redirect()

> `static` **redirect**(`url`: `string`, `status`?: `number`): [`Response`](http.md#response)

Returns a new [Response](http.md#response) with a different URL.

###### Parameters

| Parameter | Type |
| ------ | ------ |
| `url` | `string` |
| `status`? | `number` |

###### Returns

[`Response`](http.md#response)

## Interfaces

### BlobOpts

#### Extended by

- [`FileOpts`](http.md#fileopts)

#### Properties

##### endings?

> `optional` **endings**: `"transparent"` \| `"native"`

One of either `'transparent'` or `'native'`. When set to `'native'`, line endings in string source parts
will be converted to the platform native line-ending as specified by `import { EOL } from 'os'`.

##### type?

> `optional` **type**: `string`

The Blob content-type. The intent is for `type` to convey the MIME media type of the data,
however no validation of the type format is performed.

***

### FileOpts

#### Extends

- [`BlobOpts`](http.md#blobopts)

#### Properties

##### endings?

> `optional` **endings**: `"transparent"` \| `"native"`

One of either `'transparent'` or `'native'`. When set to `'native'`, line endings in string source parts
will be converted to the platform native line-ending as specified by `import { EOL } from 'os'`.

###### Inherited from

[`BlobOpts`](http.md#blobopts).[`endings`](http.md#endings)

##### lastModified?

> `optional` **lastModified**: `number`

The last modified date of the file as the number of milliseconds since the Unix epoch (January 1, 1970 at midnight).
Files without a known last modified date return the current date.

##### type?

> `optional` **type**: `string`

The Blob content-type. The intent is for `type` to convey the MIME media type of the data,
however no validation of the type format is performed.

###### Inherited from

[`BlobOpts`](http.md#blobopts).[`type`](http.md#type-3)

***

### RequestOpts

#### Properties

##### body?

> `optional` **body**: [`Blob`](http.md#blob)

##### headers?

> `optional` **headers**: [`HeadersLike`](http.md#headerslike)

##### method?

> `optional` **method**: `string`

##### signal?

> `optional` **signal**: [`AbortSignal`](../llrt/abort.md#abortsignal)

##### url?

> `optional` **url**: `string`

***

### ResponseInit

#### Extended by

- [`ResponseOpts`](http.md#responseopts)

#### Properties

##### headers?

> `readonly` `optional` **headers**: [`HeadersLike`](http.md#headerslike)

##### status?

> `readonly` `optional` **status**: `number`

##### statusText?

> `readonly` `optional` **statusText**: `string`

***

### ResponseOpts

#### Extends

- [`ResponseInit`](http.md#responseinit)

#### Properties

##### headers?

> `readonly` `optional` **headers**: [`HeadersLike`](http.md#headerslike)

###### Inherited from

[`ResponseInit`](http.md#responseinit).[`headers`](http.md#headers-4)

##### signal?

> `readonly` `optional` **signal**: [`AbortSignal`](../llrt/abort.md#abortsignal)

##### status?

> `readonly` `optional` **status**: `number`

###### Inherited from

[`ResponseInit`](http.md#responseinit).[`status`](http.md#status-1)

##### statusText?

> `readonly` `optional` **statusText**: `string`

###### Inherited from

[`ResponseInit`](http.md#responseinit).[`statusText`](http.md#statustext-1)

##### url?

> `readonly` `optional` **url**: `string`

## Type Aliases

### Body

> **Body**: [`ArrayBufferView`](../llrt/globals/namespaces/QuickJS.md#arraybufferview) \| [`Blob`](http.md#blob) \| `null`

The `Body` of a [Response](http.md#response) or [Request](http.md#request).
Currently NOT a `ReadableStream`.

***

### HeadersLike

> **HeadersLike**: `Record`\<`string`, `string`\> \| [`Headers`](http.md#headers)

***

### HeadersOpts

> **HeadersOpts**: `string`[][] \| [`HeadersLike`](http.md#headerslike)

***

### RequestCache

> **RequestCache**: `"no-cache"`

***

### RequestMode

> **RequestMode**: `"navigate"`

***

### ResponseType

> **ResponseType**: `"basic"` \| `"error"`

## Functions

### fetch()

> **fetch**(`input`: `string` \| [`Request`](http.md#request), `init`?: [`RequestOpts`](http.md#requestopts)): `Promise`\<[`Response`](http.md#response)\>

#### Parameters

| Parameter | Type |
| ------ | ------ |
| `input` | `string` \| [`Request`](http.md#request) |
| `init`? | [`RequestOpts`](http.md#requestopts) |

#### Returns

`Promise`\<[`Response`](http.md#response)\>



================================================
FILE: src/reference/modules/extra/console.md
================================================
[@caido/quickjs-types](../index.md) / extra/console

# extra/console

## Type Aliases

### Console

> **Console**: `object`

Console interface for logging.

Currently logs are only available in the backend logs.
See the [documentation](https://docs.caido.io/report_bug.html#1-backend-logs) on how to retrieve them.

#### Type declaration

##### debug()

Log a message with the debug level.

Usually used for troubleshooting purposes.

###### Parameters

| Parameter | Type |
| ------ | ------ |
| `message` | `any` |

###### Returns

`void`

##### error()

Log a message with the error level.

Usually used for critical errors.

###### Parameters

| Parameter | Type |
| ------ | ------ |
| `message` | `any` |

###### Returns

`void`

##### log()

Log a message with the info level.

Usually used for general information.

###### Parameters

| Parameter | Type |
| ------ | ------ |
| `message` | `any` |

###### Returns

`void`

##### warn()

Log a message with the warn level.

Usually used for unexpected behaviors.

###### Parameters

| Parameter | Type |
| ------ | ------ |
| `message` | `any` |

###### Returns

`void`

## Variables

### console

> **console**: [`Console`](console.md#console)



================================================
FILE: src/reference/modules/extra/os.md
================================================
[@caido/quickjs-types](../index.md) / extra/os

# extra/os

## Variables

### EOL

> `const` **EOL**: `string`

The operating system-specific end-of-line marker.
* `\n` on POSIX
* `\r\n` on Windows

## Functions

### arch()

> **arch**(): `string`

Returns the operating system CPU architecture for which the LLRT binary was compiled.
Possible values are 'arm64', 'x64'. The return value is equivalent to `process.arch`.

#### Returns

`string`

***

### homedir()

> **homedir**(): `string`

Returns the string path of the current user's home directory.

On POSIX, it uses the `$HOME` environment variable if defined. Otherwise it
uses the [effective UID](https://en.wikipedia.org/wiki/User_identifier#Effective_user_ID) to look up the user's home directory.

On Windows, it uses the `USERPROFILE` environment variable if defined.
Otherwise it uses the path to the profile directory of the current user.

#### Returns

`string`

***

### platform()

> **platform**(): [`Platform`](../llrt/globals/namespaces/QuickJS.md#platform)

Returns a string identifying the operating system platform for which
the Node.js binary was compiled. The value is set at compile time.

#### Returns

[`Platform`](../llrt/globals/namespaces/QuickJS.md#platform)

***

### release()

> **release**(): `string`

Returns the operating system release as a string.

On POSIX systems, the operating system release is determined by calling [`uname(3)`](https://linux.die.net/man/3/uname). On Windows, `RtlGetVersion()` is used. See
[https://en.wikipedia.org/wiki/Uname#Examples](https://en.wikipedia.org/wiki/Uname#Examples) for more information.

#### Returns

`string`

***

### tmpdir()

> **tmpdir**(): `string`

Returns the operating system's default directory for temporary files as a
string.

#### Returns

`string`

***

### type()

> **type**(): `string`

Returns the operating system name as returned by [`uname(3)`](https://linux.die.net/man/3/uname). For example, it
returns `'Linux'` on Linux, `'Darwin'` on macOS, and `'Windows_NT'` on Windows.

See [https://en.wikipedia.org/wiki/Uname#Examples](https://en.wikipedia.org/wiki/Uname#Examples) for additional information
about the output of running [`uname(3)`](https://linux.die.net/man/3/uname) on various operating systems.

#### Returns

`string`

***

### version()

> **version**(): `string`

Returns a string identifying the kernel version.

On POSIX systems, the operating system release is determined by calling [`uname(3)`](https://linux.die.net/man/3/uname). On Windows, `RtlGetVersion()` is used.
See [https://en.wikipedia.org/wiki/Uname#Examples](https://en.wikipedia.org/wiki/Uname#Examples) for more information.

#### Returns

`string`



================================================
FILE: src/reference/modules/extra/sqlite.md
================================================
[@caido/quickjs-types](../index.md) / extra/sqlite

# extra/sqlite

## Classes

### Database

A SQLite database.

The implementation uses a connection pool and is fully asynchronous.
Each connection will be spawned in a worker thread.

#### Example

```ts
const db = await open({ filename: "path/to/database.sqlite" });
await db.exec("CREATE TABLE test (id INTEGER PRIMARY KEY, name TEXT);");
await db.exec("INSERT INTO test (name) VALUES ('foo');");
```

#### Constructors

##### new Database()

> **new Database**(): [`Database`](sqlite.md#database)

###### Returns

[`Database`](sqlite.md#database)

#### Methods

##### exec()

> **exec**(`sql`: `string`): `Promise`\<`void`\>

This method allows one or more SQL statements to be executed without returning any results.

###### Parameters

| Parameter | Type |
| ------ | ------ |
| `sql` | `string` |

###### Returns

`Promise`\<`void`\>

##### prepare()

> **prepare**(`sql`: `string`): `Promise`\<[`Statement`](sqlite.md#statement)\>

Compiles a SQL statement into a [prepared statement](https://www.sqlite.org/c3ref/stmt.html).

###### Parameters

| Parameter | Type |
| ------ | ------ |
| `sql` | `string` |

###### Returns

`Promise`\<[`Statement`](sqlite.md#statement)\>

***

### Statement

This class represents a single prepared statement. This class cannot be instantiated via its constructor.
Instead, instances are created via the database.prepare() method.

#### Constructors

##### new Statement()

> **new Statement**(): [`Statement`](sqlite.md#statement)

###### Returns

[`Statement`](sqlite.md#statement)

#### Methods

##### all()

> **all**\<`T`\>(...`params`: [`Parameter`](sqlite.md#parameter)[]): `Promise`\<`T`[]\>

This method executes a prepared statement and returns all results as an array of objects.
If the prepared statement does not return any results, this method returns an empty array.
The prepared statement [parameters are bound](https://www.sqlite.org/c3ref/bind_blob.html) using the values in `params`.

###### Type Parameters

| Type Parameter | Default type |
| ------ | ------ |
| `T` *extends* `object` | `object` |

###### Parameters

| Parameter | Type | Description |
| ------ | ------ | ------ |
| ...`params` | [`Parameter`](sqlite.md#parameter)[] | The values to bind to the prepared statement. Named parameters are not supported. |

###### Returns

`Promise`\<`T`[]\>

##### get()

> **get**\<`T`\>(...`params`: [`Parameter`](sqlite.md#parameter)[]): `Promise`\<`undefined` \| `T`\>

This method executes a prepared statement and returns the first result as an object.
If the prepared statement does not return any results, this method returns undefined.
The prepared statement [parameters are bound](https://www.sqlite.org/c3ref/bind_blob.html) using the values in params.

###### Type Parameters

| Type Parameter | Default type |
| ------ | ------ |
| `T` *extends* `object` | `object` |

###### Parameters

| Parameter | Type | Description |
| ------ | ------ | ------ |
| ...`params` | [`Parameter`](sqlite.md#parameter)[] | The values to bind to the prepared statement. Named parameters are not supported. |

###### Returns

`Promise`\<`undefined` \| `T`\>

##### run()

> **run**(...`params`: [`Parameter`](sqlite.md#parameter)[]): `Promise`\<[`Result`](sqlite.md#result)\>

This method executes a prepared statement and returns an object summarizing the resulting changes.
The prepared statement [parameters are bound](https://www.sqlite.org/c3ref/bind_blob.html) using the values in params.

###### Parameters

| Parameter | Type | Description |
| ------ | ------ | ------ |
| ...`params` | [`Parameter`](sqlite.md#parameter)[] | The values to bind to the prepared statement. Named parameters are not supported. |

###### Returns

`Promise`\<[`Result`](sqlite.md#result)\>

## Type Aliases

### OpenOptions

> **OpenOptions**: `object`

#### Type declaration

##### busyTimeout?

> `optional` **busyTimeout**: `number`

Time (in milliseconds) to wait for the database to be unlocked before throwing an error.

###### Default

```ts
5000
```

##### filename?

> `optional` **filename**: `string`

The filename of the database. If the file does not exist, a new one will be created.

##### foreignKeys?

> `optional` **foreignKeys**: `boolean`

Enable foreign key constraints.

##### idleTimeout?

> `optional` **idleTimeout**: `number`

Maximum amount of time (in seconds) that a connection is allowed to be idle before it is closed.

###### Default

```ts
infinity
```

##### in\_memory?

> `optional` **in\_memory**: `boolean`

If true, the database will be opened in-memory.

###### Default

```ts
false
```

##### maxConnections?

> `optional` **maxConnections**: `number`

Maximum number of connections to the database.

###### Default

```ts
5
```

##### maxLifetime?

> `optional` **maxLifetime**: `number`

Maximum amount of time (in seconds) that a connection is allowed to exist before it is closed.
Set to `null` to disable.

###### Default

```ts
3600
```

##### minConnections?

> `optional` **minConnections**: `number`

Minimum number of connections to the database.

###### Default

```ts
0
```

##### pageSize?

> `optional` **pageSize**: `number`

Set the SQlite page size.

###### Default

```ts
4096
```

##### wal?

> `optional` **wal**: `boolean`

If true, the database will use the WAL mode.

###### Default

```ts
true
```

***

### Parameter

> **Parameter**: `null` \| `number` \| `bigint` \| `string` \| `Uint8Array`

***

### Result

> **Result**: `object`

#### Type declaration

##### changes

> **changes**: `number`

##### lastInsertRowid

> **lastInsertRowid**: `number`

## Functions

### open()

> **open**(`options`: [`OpenOptions`](sqlite.md#openoptions)): `Promise`\<[`Database`](sqlite.md#database)\>

Open a SQLite database.

#### Parameters

| Parameter | Type | Description |
| ------ | ------ | ------ |
| `options` | [`OpenOptions`](sqlite.md#openoptions) | The options to open the database. |

#### Returns

`Promise`\<[`Database`](sqlite.md#database)\>



================================================
FILE: src/reference/modules/extra/timers.md
================================================
[@caido/quickjs-types](../index.md) / extra/timers

# extra/timers

## Classes

### Timeout

This object is created internally and is returned from `setTimeout()` and `setInterval()`. It can be passed to either `clearTimeout()` or `clearInterval()` in order to cancel the
scheduled actions.

#### Constructors

##### new Timeout()

> **new Timeout**(): [`Timeout`](timers.md#timeout)

###### Returns

[`Timeout`](timers.md#timeout)

## Functions

### clearInterval()

> **clearInterval**(`interval`: [`Timeout`](timers.md#timeout)): `void`

Cancels a `Timeout` object created by `setInterval()`.

#### Parameters

| Parameter | Type |
| ------ | ------ |
| `interval` | [`Timeout`](timers.md#timeout) |

#### Returns

`void`

***

### clearTimeout()

> **clearTimeout**(`timeout`: [`Timeout`](timers.md#timeout)): `void`

Cancels a `Timeout` object created by `setTimeout()`.

#### Parameters

| Parameter | Type | Description |
| ------ | ------ | ------ |
| `timeout` | [`Timeout`](timers.md#timeout) | A `Timeout` object as returned by [setTimeout](timers.md#settimeout). |

#### Returns

`void`

***

### setImmediate()

> **setImmediate**\<`TArgs`\>(`callback`: (...`args`: `TArgs`) => `void`): `void`

Schedules the "immediate" execution of the `callback` after I/O events'
callbacks.

#### Type Parameters

| Type Parameter |
| ------ |
| `TArgs` *extends* `any`[] |

#### Parameters

| Parameter | Type | Description |
| ------ | ------ | ------ |
| `callback` | (...`args`: `TArgs`) => `void` | The function to call at the end of this turn of the Node.js `Event Loop` |

#### Returns

`void`

for use with clearImmediate

***

### setInterval()

> **setInterval**\<`TArgs`\>(`callback`: (...`args`: `TArgs`) => `void`, `ms`?: `number`): [`Timeout`](timers.md#timeout)

Schedules repeated execution of `callback` every `delay` milliseconds.

When `delay` isless than `4`, the `delay` will be set to `4`.

#### Type Parameters

| Type Parameter |
| ------ |
| `TArgs` *extends* `any`[] |

#### Parameters

| Parameter | Type | Description |
| ------ | ------ | ------ |
| `callback` | (...`args`: `TArgs`) => `void` | The function to call when the timer elapses. |
| `ms`? | `number` | - |

#### Returns

[`Timeout`](timers.md#timeout)

for use with [clearInterval](timers.md#clearinterval)

***

### setTimeout()

> **setTimeout**\<`TArgs`\>(`callback`: (...`args`: `TArgs`) => `void`, `ms`?: `number`): [`Timeout`](timers.md#timeout)

Schedules execution of a one-time `callback` after `delay` milliseconds.

The `callback` will likely not be invoked in precisely `delay` milliseconds.
Caido makes no guarantees about the exact timing of when callbacks will fire,
nor of their ordering. The callback will be called as close as possible to the
time specified.

When `delay` is less than `4`, the `delay` will be set to `4`.

#### Type Parameters

| Type Parameter |
| ------ |
| `TArgs` *extends* `any`[] |

#### Parameters

| Parameter | Type | Description |
| ------ | ------ | ------ |
| `callback` | (...`args`: `TArgs`) => `void` | The function to call when the timer elapses. |
| `ms`? | `number` | - |

#### Returns

[`Timeout`](timers.md#timeout)

for use with [clearTimeout](timers.md#cleartimeout)



================================================
FILE: src/reference/modules/extra/url.md
================================================
[@caido/quickjs-types](../index.md) / extra/url

# extra/url

## Classes

### URLSearchParams

The URLSearchParams interface defines utility methods to work with the query string of a URL.

#### Implements

- `Iterable`\<\[`string`, `string`\]\>

#### Constructors

##### new URLSearchParams()

> **new URLSearchParams**(`init`?: `string` \| [`URLSearchParams`](url.md#urlsearchparams) \| \{\} \| `Iterable`\<readonly \[`string`, `string`\]\> \| readonly readonly \[`string`, `string`\][]): [`URLSearchParams`](url.md#urlsearchparams)

###### Parameters

| Parameter | Type |
| ------ | ------ |
| `init`? | `string` \| [`URLSearchParams`](url.md#urlsearchparams) \| \{\} \| `Iterable`\<readonly \[`string`, `string`\]\> \| readonly readonly \[`string`, `string`\][] |

###### Returns

[`URLSearchParams`](url.md#urlsearchparams)

#### Properties

##### size

> `readonly` **size**: `number`

The total number of parameter entries.

#### Methods

##### \[iterator\]()

> **\[iterator\]**(): `IterableIterator`\<\[`string`, `string`\]\>

###### Returns

`IterableIterator`\<\[`string`, `string`\]\>

###### Implementation of

`Iterable.[iterator]`

##### append()

> **append**(`name`: `string`, `value`: `string`): `void`

Append a new name-value pair to the query string.

###### Parameters

| Parameter | Type |
| ------ | ------ |
| `name` | `string` |
| `value` | `string` |

###### Returns

`void`

##### delete()

> **delete**(`name`: `string`, `value`?: `string`): `void`

If `value` is provided, removes all name-value pairs
where name is `name` and value is `value`.

If `value` is not provided, removes all name-value pairs whose name is `name`.

###### Parameters

| Parameter | Type |
| ------ | ------ |
| `name` | `string` |
| `value`? | `string` |

###### Returns

`void`

##### entries()

> **entries**(): `IterableIterator`\<\[`string`, `string`\]\>

Returns an ES6 `Iterator` over each of the name-value pairs in the query.
Each item of the iterator is a JavaScript `Array`. The first item of the `Array` is the `name`, the second item of the `Array` is the `value`.

Alias for `urlSearchParams[@@iterator]()`.

###### Returns

`IterableIterator`\<\[`string`, `string`\]\>

##### forEach()

> **forEach**(`fn`: (`value`: `string`, `name`: `string`) => `void`): `void`

Iterates over each name-value pair in the query and invokes the given function.

```js
const myURL = new URL('https://example.org/?a=b&#x26;c=d');
myURL.searchParams.forEach((value, name) => {
  console.log(name, value);
});
// Prints:
//   a b
//   c d
```

###### Parameters

| Parameter | Type | Description |
| ------ | ------ | ------ |
| `fn` | (`value`: `string`, `name`: `string`) => `void` | Invoked for each name-value pair in the query |

###### Returns

`void`

##### get()

> **get**(`name`: `string`): `null` \| `string`

Returns the value of the first name-value pair whose name is `name`. If there
are no such pairs, `null` is returned.

###### Parameters

| Parameter | Type |
| ------ | ------ |
| `name` | `string` |

###### Returns

`null` \| `string`

or `null` if there is no name-value pair with the given `name`.

##### getAll()

> **getAll**(`name`: `string`): `string`[]

Returns the values of all name-value pairs whose name is `name`. If there are
no such pairs, an empty array is returned.

###### Parameters

| Parameter | Type |
| ------ | ------ |
| `name` | `string` |

###### Returns

`string`[]

##### has()

> **has**(`name`: `string`, `value`?: `string`): `boolean`

Checks if the `URLSearchParams` object contains key-value pair(s) based on `name` and an optional `value` argument.

If `value` is provided, returns `true` when name-value pair with
same `name` and `value` exists.

If `value` is not provided, returns `true` if there is at least one name-value
pair whose name is `name`.

###### Parameters

| Parameter | Type |
| ------ | ------ |
| `name` | `string` |
| `value`? | `string` |

###### Returns

`boolean`

##### keys()

> **keys**(): `IterableIterator`\<`string`\>

Returns an ES6 `Iterator` over the names of each name-value pair.

```js
const params = new URLSearchParams('foo=bar&#x26;foo=baz');
for (const name of params.keys()) {
  console.log(name);
}
// Prints:
//   foo
//   foo
```

###### Returns

`IterableIterator`\<`string`\>

##### set()

> **set**(`name`: `string`, `value`: `string`): `void`

Sets the value in the `URLSearchParams` object associated with `name` to `value`. If there are any pre-existing name-value pairs whose names are `name`,
set the first such pair's value to `value` and remove all others. If not,
append the name-value pair to the query string.

```js
const params = new URLSearchParams();
params.append('foo', 'bar');
params.append('foo', 'baz');
params.append('abc', 'def');
console.log(params.toString());
// Prints foo=bar&#x26;foo=baz&#x26;abc=def

params.set('foo', 'def');
params.set('xyz', 'opq');
console.log(params.toString());
// Prints foo=def&#x26;abc=def&#x26;xyz=opq
```

###### Parameters

| Parameter | Type |
| ------ | ------ |
| `name` | `string` |
| `value` | `string` |

###### Returns

`void`

##### sort()

> **sort**(): `void`

Sort all existing name-value pairs in-place by their names. Sorting is done
with a [stable sorting algorithm](https://en.wikipedia.org/wiki/Sorting_algorithm#Stability), so relative order between name-value pairs
with the same name is preserved.

This method can be used, in particular, to increase cache hits.

```js
const params = new URLSearchParams('query[]=abc&#x26;type=search&#x26;query[]=123');
params.sort();
console.log(params.toString());
// Prints query%5B%5D=abc&#x26;query%5B%5D=123&#x26;type=search
```

###### Returns

`void`

##### toString()

> **toString**(): `string`

Returns the search parameters serialized as a string, with characters
percent-encoded where necessary.

###### Returns

`string`

##### values()

> **values**(): `IterableIterator`\<`string`\>

Returns an ES6 `Iterator` over the values of each name-value pair.

###### Returns

`IterableIterator`\<`string`\>



================================================
FILE: src/reference/modules/llrt/abort.md
================================================
[@caido/quickjs-types](../index.md) / llrt/abort

# llrt/abort

## Classes

### AbortController

#### Constructors

##### new AbortController()

> **new AbortController**(): [`AbortController`](abort.md#abortcontroller)

Creates a new `AbortController` object instance.

###### Returns

[`AbortController`](abort.md#abortcontroller)

#### Properties

##### signal

> `readonly` **signal**: [`AbortSignal`](abort.md#abortsignal)

Returns the AbortSignal object associated with this object.

#### Methods

##### abort()

> **abort**(`reason`?: `any`): `void`

Invoking this method will set this object's AbortSignal's aborted flag and signal to any observers that the associated activity is to be aborted.

###### Parameters

| Parameter | Type |
| ------ | ------ |
| `reason`? | `any` |

###### Returns

`void`

***

### AbortSignal

A signal object that allows you to communicate with a DOM request (such as a Fetch) and abort it if required via an AbortController object.

#### Extends

- [`EventTarget`](dom-events.md#eventtarget)

#### Constructors

##### new AbortSignal()

> **new AbortSignal**(): [`AbortSignal`](abort.md#abortsignal)

Creates a new `AbortSignal` object instance.

###### Returns

[`AbortSignal`](abort.md#abortsignal)

###### Overrides

[`EventTarget`](dom-events.md#eventtarget).[`constructor`](dom-events.md#constructors-1)

#### Properties

##### aborted

> `readonly` **aborted**: `boolean`

Returns true if this AbortSignal's AbortController has signaled to abort, and false otherwise.

##### onabort

> **onabort**: `null` \| (`this`: [`AbortSignal`](abort.md#abortsignal), `event`: [`Event`](dom-events.md#event)) => `any`

Registers an event listener callback to execute when an `abort` event is observed.

##### reason

> `readonly` **reason**: `any`

A JavaScript value providing the abort reason, once the signal has aborted.

#### Methods

##### addEventListener()

> **addEventListener**(`type`: [`EventKey`](dom-events.md#eventkey), `listener`: [`EventListener`](dom-events.md#eventlistener), `options`?: [`AddEventListenerOptions`](dom-events.md#addeventlisteneroptions)): `void`

Adds a new handler for the `type` event. Any given `listener` is added only once per `type`.

If the `once` option is true, the `listener` is removed after the next time a `type` event is dispatched.

###### Parameters

| Parameter | Type |
| ------ | ------ |
| `type` | [`EventKey`](dom-events.md#eventkey) |
| `listener` | [`EventListener`](dom-events.md#eventlistener) |
| `options`? | [`AddEventListenerOptions`](dom-events.md#addeventlisteneroptions) |

###### Returns

`void`

###### Inherited from

[`EventTarget`](dom-events.md#eventtarget).[`addEventListener`](dom-events.md#addeventlistener)

##### dispatchEvent()

> **dispatchEvent**(`event`: [`Event`](dom-events.md#event)): `void`

Dispatches a synthetic event event to target

###### Parameters

| Parameter | Type |
| ------ | ------ |
| `event` | [`Event`](dom-events.md#event) |

###### Returns

`void`

###### Inherited from

[`EventTarget`](dom-events.md#eventtarget).[`dispatchEvent`](dom-events.md#dispatchevent)

##### removeEventListener()

> **removeEventListener**(`type`: [`EventKey`](dom-events.md#eventkey), `listener`: [`EventListener`](dom-events.md#eventlistener)): `void`

Removes the event listener in target's event listener list with the same type and callback

###### Parameters

| Parameter | Type |
| ------ | ------ |
| `type` | [`EventKey`](dom-events.md#eventkey) |
| `listener` | [`EventListener`](dom-events.md#eventlistener) |

###### Returns

`void`

###### Inherited from

[`EventTarget`](dom-events.md#eventtarget).[`removeEventListener`](dom-events.md#removeeventlistener)

##### throwIfAborted()

> **throwIfAborted**(): `void`

Throws the signal's abort reason if the signal has been aborted; otherwise it does nothing.

###### Returns

`void`

##### abort()

> `static` **abort**(`reason`?: `any`): [`AbortSignal`](abort.md#abortsignal)

Returns an `AbortSignal` instance that is already set as aborted.

###### Parameters

| Parameter | Type | Description |
| ------ | ------ | ------ |
| `reason`? | `any` | The reason for the abort. |

###### Returns

[`AbortSignal`](abort.md#abortsignal)

##### any()

> `static` **any**(`signals`: [`AbortSignal`](abort.md#abortsignal)[]): [`AbortSignal`](abort.md#abortsignal)

Returns an `AbortSignal` that aborts when any of the given abort signals abort.

###### Parameters

| Parameter | Type | Description |
| ------ | ------ | ------ |
| `signals` | [`AbortSignal`](abort.md#abortsignal)[] | An array of `AbortSignal` objects to observe. |

###### Returns

[`AbortSignal`](abort.md#abortsignal)

##### timeout()

> `static` **timeout**(`milliseconds`: `number`): [`AbortSignal`](abort.md#abortsignal)

Returns an `AbortSignal` instance that will automatically abort after a specified time.

###### Parameters

| Parameter | Type | Description |
| ------ | ------ | ------ |
| `milliseconds` | `number` | The number of milliseconds to wait before aborting. |

###### Returns

[`AbortSignal`](abort.md#abortsignal)



================================================
FILE: src/reference/modules/llrt/buffer.md
================================================
[@caido/quickjs-types](../index.md) / llrt/buffer

# llrt/buffer

## Interfaces

### Buffer

#### Extends

- `Uint8Array`

#### Indexable

\[`index`: `number`\]: `number`

#### Methods

##### copy()

> **copy**(`target`: `Uint8Array`, `targetStart`?: `number`, `sourceStart`?: `number`, `sourceEnd`?: `number`): `number`

Copies data from a region of `buf` to a region in `target`, even if the `target`memory region overlaps with `buf`.

[`TypedArray.prototype.set()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/TypedArray/set) performs the same operation, and is available
for all TypedArrays, including `Buffer`s, although it takes
different function arguments.

```js
import { Buffer } from 'buffer';

// Create two `Buffer` instances.
const buf1 = Buffer.allocUnsafe(26);
const buf2 = Buffer.allocUnsafe(26).fill('!');

for (let i = 0; i < 26; i++) {
  // 97 is the decimal ASCII value for 'a'.
  buf1[i] = i + 97;
}

// Copy `buf1` bytes 16 through 19 into `buf2` starting at byte 8 of `buf2`.
buf1.copy(buf2, 8, 16, 20);
// This is equivalent to:
// buf2.set(buf1.subarray(16, 20), 8);

console.log(buf2.toString('ascii', 0, 25));
// Prints: !!!!!!!!qrst!!!!!!!!!!!!!
```

```js
import { Buffer } from 'buffer';

// Create a `Buffer` and copy data from one region to an overlapping region
// within the same `Buffer`.

const buf = Buffer.allocUnsafe(26);

for (let i = 0; i < 26; i++) {
  // 97 is the decimal ASCII value for 'a'.
  buf[i] = i + 97;
}

buf.copy(buf, 0, 4, 10);

console.log(buf.toString());
// Prints: efghijghijklmnopqrstuvwxyz
```

###### Parameters

| Parameter | Type | Description |
| ------ | ------ | ------ |
| `target` | `Uint8Array` | A `Buffer` or Uint8Array to copy into. |
| `targetStart`? | `number` | The offset within `target` at which to begin writing. |
| `sourceStart`? | `number` | The offset within `buf` from which to begin copying. |
| `sourceEnd`? | `number` | The offset within `buf` at which to stop copying (not inclusive). |

###### Returns

`number`

The number of bytes copied.

##### subarray()

> **subarray**(`start`?: `number`, `end`?: `number`): [`Buffer`](buffer.md#buffer)

Returns a new `Buffer` that references the same memory as the original, but
offset and cropped by the `start` and `end` indices.

Specifying `end` greater than `buf.length` will return the same result as
that of `end` equal to `buf.length`.

This method is inherited from [`TypedArray.prototype.subarray()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/TypedArray/subarray).

Modifying the new `Buffer` slice will modify the memory in the original `Buffer`because the allocated memory of the two objects overlap.

```js
import { Buffer } from 'buffer';

// Create a `Buffer` with the ASCII alphabet, take a slice, and modify one byte
// from the original `Buffer`.

const buf1 = Buffer.alloc(26);

for (let i = 0; i < 26; i++) {
  // 97 is the decimal ASCII value for 'a'.
  buf1[i] = i + 97;
}

const buf2 = buf1.subarray(0, 3);

console.log(buf2.toString('ascii', 0, buf2.length));
// Prints: abc

buf1[0] = 33;

console.log(buf2.toString('ascii', 0, buf2.length));
// Prints: !bc
```

Specifying negative indexes causes the slice to be generated relative to the
end of `buf` rather than the beginning.

```js
import { Buffer } from 'buffer';

const buf = Buffer.from('buffer');

console.log(buf.subarray(-6, -1).toString());
// Prints: buffe
// (Equivalent to buf.subarray(0, 5).)

console.log(buf.subarray(-6, -2).toString());
// Prints: buff
// (Equivalent to buf.subarray(0, 4).)

console.log(buf.subarray(-5, -2).toString());
// Prints: uff
// (Equivalent to buf.subarray(1, 4).)
```

###### Parameters

| Parameter | Type | Description |
| ------ | ------ | ------ |
| `start`? | `number` | Where the new `Buffer` will start. |
| `end`? | `number` | Where the new `Buffer` will end (not inclusive). |

###### Returns

[`Buffer`](buffer.md#buffer)

###### Overrides

`Uint8Array.subarray`

##### toString()

> **toString**(`encoding`?: [`BufferEncoding`](buffer.md#bufferencoding)): `string`

Decodes `buf` to a string according to the specified character encoding in`encoding`.

If `encoding` is `'utf8'` and a byte sequence in the input is not valid UTF-8,
then each invalid byte is replaced with the replacement character `U+FFFD`.

```js
import { Buffer } from 'buffer';

const buf1 = Buffer.alloc(26);

for (let i = 0; i < 26; i++) {
  // 97 is the decimal ASCII value for 'a'.
  buf1[i] = i + 97;
}

console.log(buf1.toString('utf8'));
// Prints: abcdefghijklmnopqrstuvwxyz

const buf2 = Buffer.from('tést');

console.log(buf2.toString('hex'));
// Prints: 74c3a97374
```

###### Parameters

| Parameter | Type | Description |
| ------ | ------ | ------ |
| `encoding`? | [`BufferEncoding`](buffer.md#bufferencoding) | The character encoding to use. |

###### Returns

`string`

###### Overrides

`Uint8Array.toString`

##### writeDoubleBE()

> **writeDoubleBE**(`value`: `number`, `offset`?: `number`): `number`

Writes `value` to `buf` at the specified `offset` as big-endian. The `value` must be a JavaScript number. Behavior is undefined when `value` is anything
other than a JavaScript number.

```js
import { Buffer } from 'buffer';

const buf = Buffer.allocUnsafe(8);

buf.writeDoubleBE(123.456, 0);

console.log(buf);
// Prints: <Buffer 40 5e dd 2f 1a 9f be 77>
```

###### Parameters

| Parameter | Type | Description |
| ------ | ------ | ------ |
| `value` | `number` | Number to be written to `buf`. |
| `offset`? | `number` | Number of bytes to skip before starting to write. Must satisfy `0 <= offset <= buf.length - 8`. |

###### Returns

`number`

`offset` plus the number of bytes written.

##### writeDoubleLE()

> **writeDoubleLE**(`value`: `number`, `offset`?: `number`): `number`

Writes `value` to `buf` at the specified `offset` as little-endian. The `value` must be a JavaScript number. Behavior is undefined when `value` is anything
other than a JavaScript number.

```js
import { Buffer } from 'buffer';

const buf = Buffer.allocUnsafe(8);

buf.writeDoubleLE(123.456, 0);

console.log(buf);
// Prints: <Buffer 77 be 9f 1a 2f dd 5e 40>
```

###### Parameters

| Parameter | Type | Description |
| ------ | ------ | ------ |
| `value` | `number` | Number to be written to `buf`. |
| `offset`? | `number` | Number of bytes to skip before starting to write. Must satisfy `0 <= offset <= buf.length - 8`. |

###### Returns

`number`

`offset` plus the number of bytes written.

##### writeFloatBE()

> **writeFloatBE**(`value`: `number`, `offset`?: `number`): `number`

Writes `value` to `buf` at the specified `offset` as big-endian. Behavior is
undefined when `value` is anything other than a JavaScript number.

```js
import { Buffer } from 'buffer';

const buf = Buffer.allocUnsafe(4);

buf.writeFloatBE(0xcafebabe, 0);

console.log(buf);
// Prints: <Buffer 4f 4a fe bb>
```

###### Parameters

| Parameter | Type | Description |
| ------ | ------ | ------ |
| `value` | `number` | Number to be written to `buf`. |
| `offset`? | `number` | Number of bytes to skip before starting to write. Must satisfy `0 <= offset <= buf.length - 4`. |

###### Returns

`number`

`offset` plus the number of bytes written.

##### writeFloatLE()

> **writeFloatLE**(`value`: `number`, `offset`?: `number`): `number`

Writes `value` to `buf` at the specified `offset` as little-endian. Behavior is
undefined when `value` is anything other than a JavaScript number.

```js
import { Buffer } from 'buffer';

const buf = Buffer.allocUnsafe(4);

buf.writeFloatLE(0xcafebabe, 0);

console.log(buf);
// Prints: <Buffer bb fe 4a 4f>
```

###### Parameters

| Parameter | Type | Description |
| ------ | ------ | ------ |
| `value` | `number` | Number to be written to `buf`. |
| `offset`? | `number` | Number of bytes to skip before starting to write. Must satisfy `0 <= offset <= buf.length - 4`. |

###### Returns

`number`

`offset` plus the number of bytes written.

##### writeInt16BE()

> **writeInt16BE**(`value`: `number`, `offset`?: `number`): `number`

Writes `value` to `buf` at the specified `offset` as big-endian.  The `value` must be a valid signed 16-bit integer. Behavior is undefined when `value` is
anything other than a signed 16-bit integer.

The `value` is interpreted and written as a two's complement signed integer.

```js
import { Buffer } from 'buffer';

const buf = Buffer.allocUnsafe(2);

buf.writeInt16BE(0x0102, 0);

console.log(buf);
// Prints: <Buffer 01 02>
```

###### Parameters

| Parameter | Type | Description |
| ------ | ------ | ------ |
| `value` | `number` | Number to be written to `buf`. |
| `offset`? | `number` | Number of bytes to skip before starting to write. Must satisfy `0 <= offset <= buf.length - 2`. |

###### Returns

`number`

`offset` plus the number of bytes written.

##### writeInt16LE()

> **writeInt16LE**(`value`: `number`, `offset`?: `number`): `number`

Writes `value` to `buf` at the specified `offset` as little-endian.  The `value` must be a valid signed 16-bit integer. Behavior is undefined when `value` is
anything other than a signed 16-bit integer.

The `value` is interpreted and written as a two's complement signed integer.

```js
import { Buffer } from 'buffer';

const buf = Buffer.allocUnsafe(2);

buf.writeInt16LE(0x0304, 0);

console.log(buf);
// Prints: <Buffer 04 03>
```

###### Parameters

| Parameter | Type | Description |
| ------ | ------ | ------ |
| `value` | `number` | Number to be written to `buf`. |
| `offset`? | `number` | Number of bytes to skip before starting to write. Must satisfy `0 <= offset <= buf.length - 2`. |

###### Returns

`number`

`offset` plus the number of bytes written.

##### writeInt32BE()

> **writeInt32BE**(`value`: `number`, `offset`?: `number`): `number`

Writes `value` to `buf` at the specified `offset` as big-endian. The `value` must be a valid signed 32-bit integer. Behavior is undefined when `value` is
anything other than a signed 32-bit integer.

The `value` is interpreted and written as a two's complement signed integer.

```js
import { Buffer } from 'buffer';

const buf = Buffer.allocUnsafe(4);

buf.writeInt32BE(0x01020304, 0);

console.log(buf);
// Prints: <Buffer 01 02 03 04>
```

###### Parameters

| Parameter | Type | Description |
| ------ | ------ | ------ |
| `value` | `number` | - |
| `offset`? | `number` | Number of bytes to skip before starting to write. Must satisfy `0 <= offset <= buf.length - 4`. |

###### Returns

`number`

`offset` plus the number of bytes written.

##### writeInt32LE()

> **writeInt32LE**(`value`: `number`, `offset`?: `number`): `number`

Writes `value` to `buf` at the specified `offset` as little-endian. The `value` must be a valid signed 32-bit integer. Behavior is undefined when `value` is
anything other than a signed 32-bit integer.

The `value` is interpreted and written as a two's complement signed integer.

```js
import { Buffer } from 'buffer';

const buf = Buffer.allocUnsafe(4);

buf.writeInt32LE(0x05060708, 0);

console.log(buf);
// Prints: <Buffer 08 07 06 05>
```

###### Parameters

| Parameter | Type | Description |
| ------ | ------ | ------ |
| `value` | `number` | Number to be written to `buf`. |
| `offset`? | `number` | Number of bytes to skip before starting to write. Must satisfy `0 <= offset <= buf.length - 4`. |

###### Returns

`number`

`offset` plus the number of bytes written.

##### writeInt8()

> **writeInt8**(`value`: `number`, `offset`?: `number`): `number`

Writes `value` to `buf` at the specified `offset`. `value` must be a valid
signed 8-bit integer. Behavior is undefined when `value` is anything other than
a signed 8-bit integer.

`value` is interpreted and written as a two's complement signed integer.

```js
import { Buffer } from 'buffer';

const buf = Buffer.allocUnsafe(2);

buf.writeInt8(2, 0);
buf.writeInt8(-2, 1);

console.log(buf);
// Prints: <Buffer 02 fe>
```

###### Parameters

| Parameter | Type | Description |
| ------ | ------ | ------ |
| `value` | `number` | Number to be written to `buf`. |
| `offset`? | `number` | Number of bytes to skip before starting to write. Must satisfy `0 <= offset <= buf.length - 1`. |

###### Returns

`number`

`offset` plus the number of bytes written.

***

### BufferConstructor

#### Methods

##### alloc()

> **alloc**(`size`: `number`, `fill`?: `string` \| `number` \| `Uint8Array`, `encoding`?: [`BufferEncoding`](buffer.md#bufferencoding)): [`Buffer`](buffer.md#buffer)

Allocates a new `Buffer` of `size` bytes. If `fill` is `undefined`, the `Buffer` will be zero-filled.

```js
import { Buffer } from 'buffer';

const buf = Buffer.alloc(5);

console.log(buf);
// Prints: <Buffer 00 00 00 00 00>
```

If `fill` is specified, the allocated `Buffer` will be initialized by calling `Buffer.alloc(size, fill)`.

```js
import { Buffer } from 'buffer';

const buf = Buffer.alloc(5, 'a');

console.log(buf);
// Prints: <Buffer 61 61 61 61 61>
```

If both `fill` and `encoding` are specified, the allocated `Buffer` will be
initialized by calling `Buffer.aloc(size, fill, encoding)`.

```js
import { Buffer } from 'buffer';

const buf = Buffer.alloc(11, 'aGVsbG8gd29ybGQ=', 'base64');

console.log(buf);
// Prints: <Buffer 68 65 6c 6c 6f 20 77 6f 72 6c 64>
```

###### Parameters

| Parameter | Type | Description |
| ------ | ------ | ------ |
| `size` | `number` | The desired length of the new `Buffer`. |
| `fill`? | `string` \| `number` \| `Uint8Array` | A value to pre-fill the new `Buffer` with. |
| `encoding`? | [`BufferEncoding`](buffer.md#bufferencoding) | If `fill` is a string, this is its encoding. |

###### Returns

[`Buffer`](buffer.md#buffer)

##### byteLength()

> **byteLength**(`string`: `string` \| `ArrayBuffer` \| `SharedArrayBuffer` \| [`ArrayBufferView`](globals/namespaces/QuickJS.md#arraybufferview) \| [`Buffer`](buffer.md#buffer), `encoding`?: [`BufferEncoding`](buffer.md#bufferencoding)): `number`

Returns the byte length of a string when encoded using `encoding`.
This is not the same as [`String.prototype.length`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/String/length), which does not account
for the encoding that is used to convert the string into bytes.

```js
import { Buffer } from 'buffer';

const str = '\u00bd + \u00bc = \u00be';

console.log(`${str}: ${str.length} characters, ` +
            `${Buffer.byteLength(str, 'utf8')} bytes`);
// Prints: ½ + ¼ = ¾: 9 characters, 12 bytes
```

When `string` is a
`Buffer`/[`DataView`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/DataView)/[`TypedArray`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/-
Reference/Global_Objects/TypedArray)/[`ArrayBuffer`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/ArrayBuffer)/[`SharedArrayBuffer`](https://develop-
er.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/SharedArrayBuffer), the byte length as reported by `.byteLength`is returned.

###### Parameters

| Parameter | Type | Description |
| ------ | ------ | ------ |
| `string` | `string` \| `ArrayBuffer` \| `SharedArrayBuffer` \| [`ArrayBufferView`](globals/namespaces/QuickJS.md#arraybufferview) \| [`Buffer`](buffer.md#buffer) | A value to calculate the length of. |
| `encoding`? | [`BufferEncoding`](buffer.md#bufferencoding) | If `string` is a string, this is its encoding. |

###### Returns

`number`

The number of bytes contained within `string`.

##### concat()

> **concat**(`list`: readonly `Uint8Array`[], `totalLength`?: `number`): [`Buffer`](buffer.md#buffer)

Returns a new `Buffer` which is the result of concatenating all the `Buffer` instances in the `list` together.

If the list has no items, or if the `totalLength` is 0, then a new zero-length `Buffer` is returned.

If `totalLength` is not provided, it is calculated from the `Buffer` instances
in `list` by adding their lengths.

If `totalLength` is provided, it is coerced to an unsigned integer. If the
combined length of the `Buffer`s in `list` exceeds `totalLength`, the result is
truncated to `totalLength`.

```js
import { Buffer } from 'buffer';

// Create a single `Buffer` from a list of three `Buffer` instances.

const buf1 = Buffer.alloc(10);
const buf2 = Buffer.alloc(14);
const buf3 = Buffer.alloc(18);
const totalLength = buf1.length + buf2.length + buf3.length;

console.log(totalLength);
// Prints: 42

const bufA = Buffer.concat([buf1, buf2, buf3], totalLength);

console.log(bufA);
// Prints: <Buffer 00 00 00 00 ...>
console.log(bufA.length);
// Prints: 42
```

###### Parameters

| Parameter | Type | Description |
| ------ | ------ | ------ |
| `list` | readonly `Uint8Array`[] | List of `Buffer` or Uint8Array instances to concatenate. |
| `totalLength`? | `number` | Total length of the `Buffer` instances in `list` when concatenated. |

###### Returns

[`Buffer`](buffer.md#buffer)

##### from()

###### Call Signature

> **from**(`arrayBuffer`: [`WithImplicitCoercion`](buffer.md#withimplicitcoerciont)\<`ArrayBuffer` \| `SharedArrayBuffer`\>, `byteOffset`?: `number`, `length`?: `number`): [`Buffer`](buffer.md#buffer)

Allocates a new `Buffer` using an `array` of bytes in the range `0` – `255`.

###### Parameters

| Parameter | Type |
| ------ | ------ |
| `arrayBuffer` | [`WithImplicitCoercion`](buffer.md#withimplicitcoerciont)\<`ArrayBuffer` \| `SharedArrayBuffer`\> |
| `byteOffset`? | `number` |
| `length`? | `number` |

###### Returns

[`Buffer`](buffer.md#buffer)

###### Call Signature

> **from**(`data`: `Uint8Array` \| readonly `number`[]): [`Buffer`](buffer.md#buffer)

Creates a new Buffer using the passed {data}

###### Parameters

| Parameter | Type | Description |
| ------ | ------ | ------ |
| `data` | `Uint8Array` \| readonly `number`[] | data to create a new Buffer |

###### Returns

[`Buffer`](buffer.md#buffer)

###### Call Signature

> **from**(`data`: [`WithImplicitCoercion`](buffer.md#withimplicitcoerciont)\<`string` \| `Uint8Array` \| readonly `number`[]\>): [`Buffer`](buffer.md#buffer)

###### Parameters

| Parameter | Type |
| ------ | ------ |
| `data` | [`WithImplicitCoercion`](buffer.md#withimplicitcoerciont)\<`string` \| `Uint8Array` \| readonly `number`[]\> |

###### Returns

[`Buffer`](buffer.md#buffer)

###### Call Signature

> **from**(`str`: [`WithImplicitCoercion`](buffer.md#withimplicitcoerciont)\<`string`\> \| \{ `[toPrimitive]`: `string`; \}, `encoding`?: [`BufferEncoding`](buffer.md#bufferencoding)): [`Buffer`](buffer.md#buffer)

Creates a new Buffer containing the given JavaScript string {str}.
If provided, the {encoding} parameter identifies the character encoding.
If not provided, {encoding} defaults to 'utf8'.

###### Parameters

| Parameter | Type |
| ------ | ------ |
| `str` | [`WithImplicitCoercion`](buffer.md#withimplicitcoerciont)\<`string`\> \| \{ `[toPrimitive]`: `string`; \} |
| `encoding`? | [`BufferEncoding`](buffer.md#bufferencoding) |

###### Returns

[`Buffer`](buffer.md#buffer)

## Type Aliases

### BufferEncoding

> **BufferEncoding**: `"hex"` \| `"base64"` \| `"utf-8"` \| `"utf8"` \| `"unicode-1-1-utf8"` \| `"utf-16le"` \| `"utf16le"` \| `"utf-16"` \| `"utf16"` \| `"utf-16be"` \| `"utf16be"` \| `"windows-1252"` \| `"ansi_x3.4-1968"` \| `"ascii"` \| `"cp1252"` \| `"cp819"` \| `"csisolatin1"` \| `"ibm819"` \| `"iso-8859-1"` \| `"iso-ir-100"` \| `"iso8859-1"` \| `"iso88591"` \| `"iso_8859-1"` \| `"iso_8859-1:1987"` \| `"l1"` \| `"latin1"` \| `"us-ascii"` \| `"x-cp1252"`

***

### WithImplicitCoercion\<T\>

> **WithImplicitCoercion**\<`T`\>: `T` \| \{ `valueOf`: `T`; \}

#### Type Parameters

| Type Parameter |
| ------ |
| `T` |

## Variables

### Buffer

> **Buffer**: [`BufferConstructor`](buffer.md#bufferconstructor)

***

### constants

> `const` **constants**: `object`

#### Type declaration

##### MAX\_LENGTH

> **MAX\_LENGTH**: `number`

##### MAX\_STRING\_LENGTH

> **MAX\_STRING\_LENGTH**: `number`

## Functions

### atob()

> **atob**(`data`: `string`): `string`

Decodes a string of Base64-encoded data into bytes, and encodes those bytes
into a string using UTF-8.

The `data` may be any JavaScript-value that can be coerced into a string.

#### Parameters

| Parameter | Type | Description |
| ------ | ------ | ------ |
| `data` | `string` | The Base64-encoded input string. |

#### Returns

`string`

#### Legacy

Use `Buffer.from(data, 'base64')` instead.

***

### btoa()

> **btoa**(`data`: `string`): `string`

Decodes a string into bytes using UTF-8, and encodes those bytes
into a string using Base64.

The `data` may be any JavaScript-value that can be coerced into a string.

#### Parameters

| Parameter | Type | Description |
| ------ | ------ | ------ |
| `data` | `string` | An ASCII (Latin1) string. |

#### Returns

`string`

#### Legacy

Use `buf.toString('base64')` instead.



================================================
FILE: src/reference/modules/llrt/child_process.md
================================================
[@caido/quickjs-types](../index.md) / llrt/child\_process

# llrt/child\_process

## Classes

### ChildProcess

Instances of the `ChildProcess` represent spawned child processes.

Instances of `ChildProcess` are not intended to be created directly. Rather,
use the [spawn](child_process.md#spawn) method to create instances of `ChildProcess`.

#### Extends

- [`EventEmitter`](globals/index.md#eventemittert)

#### Extended by

- [`ChildProcessWithoutNullStreams`](child_process.md#childprocesswithoutnullstreams)
- [`ChildProcessByStdio`](child_process.md#childprocessbystdioi-o-e)

#### Constructors

##### new ChildProcess()

> **new ChildProcess**(): [`ChildProcess`](child_process.md#childprocess)

###### Returns

[`ChildProcess`](child_process.md#childprocess)

###### Inherited from

[`EventEmitter`](globals/index.md#eventemittert).[`constructor`](globals/index.md#constructors)

#### Properties

##### pid?

> `readonly` `optional` **pid**: `number`

Returns the process identifier (PID) of the child process. If the child process
fails to spawn due to errors, then the value is `undefined` and `error` is
emitted.

```js
const { spawn } = require('child_process');
const grep = spawn('grep', ['ssh']);

console.log(`Spawned child pid: ${grep.pid}`);
grep.stdin.end();
```

##### stderr

> **stderr**: `null` \| [`DefaultReadableStream`](stream.md#defaultreadablestream)

A `Readable Stream` that represents the child process's `stderr`.

If the child was spawned with `stdio[2]` set to anything other than `'pipe'`,
then this will be `null`.

`subprocess.stderr` is an alias for `subprocess.stdio[2]`. Both properties will
refer to the same value.

The `subprocess.stderr` property can be `null` or `undefined` if the child process could not be successfully spawned.

##### stdin

> **stdin**: `null` \| [`DefaultWritableStream`](stream.md#defaultwritablestream)

A `Writable Stream` that represents the child process's `stdin`.

If a child process waits to read all of its input, the child will not continue
until this stream has been closed via `end()`.

If the child was spawned with `stdio[0]` set to anything other than `'pipe'`,
then this will be `null`.

`subprocess.stdin` is an alias for `subprocess.stdio[0]`. Both properties will
refer to the same value.

The `subprocess.stdin` property can be `null` or `undefined` if the child process could not be successfully spawned.

##### stdout

> **stdout**: `null` \| [`DefaultReadableStream`](stream.md#defaultreadablestream)

A `Readable Stream` that represents the child process's `stdout`.

If the child was spawned with `stdio[1]` set to anything other than `'pipe'`,
then this will be `null`.

`subprocess.stdout` is an alias for `subprocess.stdio[1]`. Both properties will
refer to the same value.

```js
const { spawn } = require('child_process');

const subprocess = spawn('ls');

subprocess.stdout.on('data', (data) => {
  console.log(`Received chunk ${data}`);
});
```

The `subprocess.stdout` property can be `null` or `undefined` if the child process could not be successfully spawned.

#### Methods

##### \[dispose\]()

> **\[dispose\]**(): `void`

Calls [ChildProcess.kill](child_process.md#kill) with `'SIGTERM'`.

###### Returns

`void`

##### addListener()

###### Call Signature

> **addListener**(`event`: `string`, `listener`: (...`args`: `any`[]) => `void`): `this`

events.EventEmitter
1. close
2. error
3. exit

###### Parameters

| Parameter | Type |
| ------ | ------ |
| `event` | `string` |
| `listener` | (...`args`: `any`[]) => `void` |

###### Returns

`this`

###### Overrides

[`EventEmitter`](globals/index.md#eventemittert).[`addListener`](globals/index.md#addlistener)

###### Call Signature

> **addListener**(`event`: `"close"`, `listener`: (`code`: `null` \| `number`, `signal`: `null` \| [`Signals`](globals/namespaces/QuickJS.md#signals)) => `void`): `this`

events.EventEmitter
1. close
2. error
3. exit

###### Parameters

| Parameter | Type |
| ------ | ------ |
| `event` | `"close"` |
| `listener` | (`code`: `null` \| `number`, `signal`: `null` \| [`Signals`](globals/namespaces/QuickJS.md#signals)) => `void` |

###### Returns

`this`

###### Overrides

`EventEmitter.addListener`

###### Call Signature

> **addListener**(`event`: `"error"`, `listener`: (`err`: `Error`) => `void`): `this`

events.EventEmitter
1. close
2. error
3. exit

###### Parameters

| Parameter | Type |
| ------ | ------ |
| `event` | `"error"` |
| `listener` | (`err`: `Error`) => `void` |

###### Returns

`this`

###### Overrides

`EventEmitter.addListener`

###### Call Signature

> **addListener**(`event`: `"exit"`, `listener`: (`code`: `null` \| `number`, `signal`: `null` \| [`Signals`](globals/namespaces/QuickJS.md#signals)) => `void`): `this`

events.EventEmitter
1. close
2. error
3. exit

###### Parameters

| Parameter | Type |
| ------ | ------ |
| `event` | `"exit"` |
| `listener` | (`code`: `null` \| `number`, `signal`: `null` \| [`Signals`](globals/namespaces/QuickJS.md#signals)) => `void` |

###### Returns

`this`

###### Overrides

`EventEmitter.addListener`

##### emit()

###### Call Signature

> **emit**(`event`: `string` \| `symbol`, ...`args`: `any`[]): `boolean`

Synchronously calls each of the listeners registered for the event named `eventName`, in the order they were registered, passing the supplied arguments
to each.

```js
import { EventEmitter } from 'events';
const myEmitter = new EventEmitter();

// First listener
myEmitter.on('event', function firstListener() {
  console.log('Helloooo! first listener');
});
// Second listener
myEmitter.on('event', function secondListener(arg1, arg2) {
  console.log(`event with parameters ${arg1}, ${arg2} in second listener`);
});
// Third listener
myEmitter.on('event', function thirdListener(...args) {
  const parameters = args.join(', ');
  console.log(`event with parameters ${parameters} in third listener`);
});

myEmitter.emit('event', 1, 2, 3, 4, 5);

// Prints:
// Helloooo! first listener
// event with parameters 1, 2 in second listener
// event with parameters 1, 2, 3, 4, 5 in third listener
```

###### Parameters

| Parameter | Type |
| ------ | ------ |
| `event` | `string` \| `symbol` |
| ...`args` | `any`[] |

###### Returns

`boolean`

###### Overrides

[`EventEmitter`](globals/index.md#eventemittert).[`emit`](globals/index.md#emit)

###### Call Signature

> **emit**(`event`: `"close"`, `code`: `null` \| `number`, `signal`: `null` \| [`Signals`](globals/namespaces/QuickJS.md#signals)): `boolean`

###### Parameters

| Parameter | Type |
| ------ | ------ |
| `event` | `"close"` |
| `code` | `null` \| `number` |
| `signal` | `null` \| [`Signals`](globals/namespaces/QuickJS.md#signals) |

###### Returns

`boolean`

###### Overrides

`EventEmitter.emit`

###### Call Signature

> **emit**(`event`: `"error"`, `err`: `Error`): `boolean`

###### Parameters

| Parameter | Type |
| ------ | ------ |
| `event` | `"error"` |
| `err` | `Error` |

###### Returns

`boolean`

###### Overrides

`EventEmitter.emit`

###### Call Signature

> **emit**(`event`: `"exit"`, `code`: `null` \| `number`, `signal`: `null` \| [`Signals`](globals/namespaces/QuickJS.md#signals)): `boolean`

###### Parameters

| Parameter | Type |
| ------ | ------ |
| `event` | `"exit"` |
| `code` | `null` \| `number` |
| `signal` | `null` \| [`Signals`](globals/namespaces/QuickJS.md#signals) |

###### Returns

`boolean`

###### Overrides

`EventEmitter.emit`

##### eventNames()

> **eventNames**(): [`EventKey`](dom-events.md#eventkey)[]

Returns an array listing the events for which the emitter has registered
listeners. The values in the array are strings or `Symbol`s.

```js
import { EventEmitter } from 'events';

const myEE = new EventEmitter();
myEE.on('foo', () => {});
myEE.on('bar', () => {});

const sym = Symbol('symbol');
myEE.on(sym, () => {});

console.log(myEE.eventNames());
// Prints: [ 'foo', 'bar', Symbol(symbol) ]
```

###### Returns

[`EventKey`](dom-events.md#eventkey)[]

###### Inherited from

[`EventEmitter`](globals/index.md#eventemittert).[`eventNames`](globals/index.md#eventnames)

##### kill()

> **kill**(`signal`?: `number` \| [`Signals`](globals/namespaces/QuickJS.md#signals)): `boolean`

The `subprocess.kill()` method sends a signal to the child process. If no
argument is given, the process will be sent the `'SIGTERM'` signal. See [`signal(7)`](http://man7.org/linux/man-pages/man7/signal.7.html) for a list of available signals. This function
returns `true` if [`kill(2)`](http://man7.org/linux/man-pages/man2/kill.2.html) succeeds, and `false` otherwise.

```js
const { spawn } = require('child_process');
const grep = spawn('grep', ['ssh']);

grep.on('close', (code, signal) => {
  console.log(
    `child process terminated due to receipt of signal ${signal}`);
});

// Send SIGHUP to process.
grep.kill('SIGHUP');
```

The `ChildProcess` object may emit an `'error'` event if the signal
cannot be delivered. Sending a signal to a child process that has already exited
is not an error but may have unforeseen consequences. Specifically, if the
process identifier (PID) has been reassigned to another process, the signal will
be delivered to that process instead which can have unexpected results.

While the function is called `kill`, the signal delivered to the child process
may not actually terminate the process.

See [`kill(2)`](http://man7.org/linux/man-pages/man2/kill.2.html) for reference.

On Windows, where POSIX signals do not exist, the `signal` argument will be
ignored, and the process will be killed forcefully and abruptly (similar to `'SIGKILL'`).
See `Signal Events` for more details.

On Linux, child processes of child processes will not be terminated
when attempting to kill their parent. This is likely to happen when running a
new process in a shell or with the use of the `shell` option of `ChildProcess`:

```js
'use strict';
const { spawn } = require('child_process');

const subprocess = spawn(
  'sh',
  [
    '-c',
    `node -e "setInterval(() => {
      console.log(process.pid, 'is alive')
    }, 500);"`,
  ], {
    stdio: ['inherit', 'inherit', 'inherit'],
  },
);

setTimeout(() => {
  subprocess.kill(); // Does not terminate the Node.js process in the shell.
}, 2000);
```

###### Parameters

| Parameter | Type |
| ------ | ------ |
| `signal`? | `number` \| [`Signals`](globals/namespaces/QuickJS.md#signals) |

###### Returns

`boolean`

##### off()

> **off**\<`K`\>(`eventName`: [`EventKey`](dom-events.md#eventkey), `listener`: (...`args`: `any`[]) => `void`): `this`

Alias for `emitter.removeListener()`.

###### Type Parameters

| Type Parameter |
| ------ |
| `K` |

###### Parameters

| Parameter | Type |
| ------ | ------ |
| `eventName` | [`EventKey`](dom-events.md#eventkey) |
| `listener` | (...`args`: `any`[]) => `void` |

###### Returns

`this`

###### Inherited from

[`EventEmitter`](globals/index.md#eventemittert).[`off`](globals/index.md#off)

##### on()

###### Call Signature

> **on**(`event`: `string`, `listener`: (...`args`: `any`[]) => `void`): `this`

Adds the `listener` function to the end of the listeners array for the event
named `eventName`. No checks are made to see if the `listener` has already
been added. Multiple calls passing the same combination of `eventName` and
`listener` will result in the `listener` being added, and called, multiple times.

```js
server.on('connection', (stream) => {
  console.log('someone connected!');
});
```

Returns a reference to the `EventEmitter`, so that calls can be chained.

By default, event listeners are invoked in the order they are added. The `emitter.prependListener()` method can be used as an alternative to add the
event listener to the beginning of the listeners array.

```js
import { EventEmitter } from 'events';
const myEE = new EventEmitter();
myEE.on('foo', () => console.log('a'));
myEE.prependListener('foo', () => console.log('b'));
myEE.emit('foo');
// Prints:
//   b
//   a
```

###### Parameters

| Parameter | Type | Description |
| ------ | ------ | ------ |
| `event` | `string` | - |
| `listener` | (...`args`: `any`[]) => `void` | The callback function |

###### Returns

`this`

###### Overrides

[`EventEmitter`](globals/index.md#eventemittert).[`on`](globals/index.md#on)

###### Call Signature

> **on**(`event`: `"close"`, `listener`: (`code`: `null` \| `number`, `signal`: `null` \| [`Signals`](globals/namespaces/QuickJS.md#signals)) => `void`): `this`

###### Parameters

| Parameter | Type |
| ------ | ------ |
| `event` | `"close"` |
| `listener` | (`code`: `null` \| `number`, `signal`: `null` \| [`Signals`](globals/namespaces/QuickJS.md#signals)) => `void` |

###### Returns

`this`

###### Overrides

`EventEmitter.on`

###### Call Signature

> **on**(`event`: `"error"`, `listener`: (`err`: `Error`) => `void`): `this`

###### Parameters

| Parameter | Type |
| ------ | ------ |
| `event` | `"error"` |
| `listener` | (`err`: `Error`) => `void` |

###### Returns

`this`

###### Overrides

`EventEmitter.on`

###### Call Signature

> **on**(`event`: `"exit"`, `listener`: (`code`: `null` \| `number`, `signal`: `null` \| [`Signals`](globals/namespaces/QuickJS.md#signals)) => `void`): `this`

###### Parameters

| Parameter | Type |
| ------ | ------ |
| `event` | `"exit"` |
| `listener` | (`code`: `null` \| `number`, `signal`: `null` \| [`Signals`](globals/namespaces/QuickJS.md#signals)) => `void` |

###### Returns

`this`

###### Overrides

`EventEmitter.on`

##### once()

###### Call Signature

> **once**(`event`: `string`, `listener`: (...`args`: `any`[]) => `void`): `this`

Adds a **one-time** `listener` function for the event named `eventName`. The
next time `eventName` is triggered, this listener is removed and then invoked.

Returns a reference to the `EventEmitter`, so that calls can be chained.

By default, event listeners are invoked in the order they are added. The `emitter.prependOnceListener()` method can be used as an alternative to add the
event listener to the beginning of the listeners array.

```js
import { EventEmitter } from 'events';
const myEE = new EventEmitter();
myEE.once('foo', () => console.log('a'));
myEE.prependOnceListener('foo', () => console.log('b'));
myEE.emit('foo');
// Prints:
//   b
//   a
```

###### Parameters

| Parameter | Type | Description |
| ------ | ------ | ------ |
| `event` | `string` | - |
| `listener` | (...`args`: `any`[]) => `void` | The callback function |

###### Returns

`this`

###### Since

v0.3.0

###### Overrides

[`EventEmitter`](globals/index.md#eventemittert).[`once`](globals/index.md#once)

###### Call Signature

> **once**(`event`: `"close"`, `listener`: (`code`: `null` \| `number`, `signal`: `null` \| [`Signals`](globals/namespaces/QuickJS.md#signals)) => `void`): `this`

###### Parameters

| Parameter | Type |
| ------ | ------ |
| `event` | `"close"` |
| `listener` | (`code`: `null` \| `number`, `signal`: `null` \| [`Signals`](globals/namespaces/QuickJS.md#signals)) => `void` |

###### Returns

`this`

###### Overrides

`EventEmitter.once`

###### Call Signature

> **once**(`event`: `"error"`, `listener`: (`err`: `Error`) => `void`): `this`

###### Parameters

| Parameter | Type |
| ------ | ------ |
| `event` | `"error"` |
| `listener` | (`err`: `Error`) => `void` |

###### Returns

`this`

###### Overrides

`EventEmitter.once`

###### Call Signature

> **once**(`event`: `"exit"`, `listener`: (`code`: `null` \| `number`, `signal`: `null` \| [`Signals`](globals/namespaces/QuickJS.md#signals)) => `void`): `this`

###### Parameters

| Parameter | Type |
| ------ | ------ |
| `event` | `"exit"` |
| `listener` | (`code`: `null` \| `number`, `signal`: `null` \| [`Signals`](globals/namespaces/QuickJS.md#signals)) => `void` |

###### Returns

`this`

###### Overrides

`EventEmitter.once`

##### prependListener()

###### Call Signature

> **prependListener**(`event`: `string`, `listener`: (...`args`: `any`[]) => `void`): `this`

Adds the `listener` function to the _beginning_ of the listeners array for the
event named `eventName`. No checks are made to see if the `listener` has
already been added. Multiple calls passing the same combination of `eventName`
and `listener` will result in the `listener` being added, and called, multiple times.

Returns a reference to the `EventEmitter`, so that calls can be chained.

###### Parameters

| Parameter | Type | Description |
| ------ | ------ | ------ |
| `event` | `string` | - |
| `listener` | (...`args`: `any`[]) => `void` | The callback function |

###### Returns

`this`

###### Overrides

[`EventEmitter`](globals/index.md#eventemittert).[`prependListener`](globals/index.md#prependlistener)

###### Call Signature

> **prependListener**(`event`: `"close"`, `listener`: (`code`: `null` \| `number`, `signal`: `null` \| [`Signals`](globals/namespaces/QuickJS.md#signals)) => `void`): `this`

###### Parameters

| Parameter | Type |
| ------ | ------ |
| `event` | `"close"` |
| `listener` | (`code`: `null` \| `number`, `signal`: `null` \| [`Signals`](globals/namespaces/QuickJS.md#signals)) => `void` |

###### Returns

`this`

###### Overrides

`EventEmitter.prependListener`

###### Call Signature

> **prependListener**(`event`: `"error"`, `listener`: (`err`: `Error`) => `void`): `this`

###### Parameters

| Parameter | Type |
| ------ | ------ |
| `event` | `"error"` |
| `listener` | (`err`: `Error`) => `void` |

###### Returns

`this`

###### Overrides

`EventEmitter.prependListener`

###### Call Signature

> **prependListener**(`event`: `"exit"`, `listener`: (`code`: `null` \| `number`, `signal`: `null` \| [`Signals`](globals/namespaces/QuickJS.md#signals)) => `void`): `this`

###### Parameters

| Parameter | Type |
| ------ | ------ |
| `event` | `"exit"` |
| `listener` | (`code`: `null` \| `number`, `signal`: `null` \| [`Signals`](globals/namespaces/QuickJS.md#signals)) => `void` |

###### Returns

`this`

###### Overrides

`EventEmitter.prependListener`

##### prependOnceListener()

###### Call Signature

> **prependOnceListener**(`event`: `string`, `listener`: (...`args`: `any`[]) => `void`): `this`

Adds a **one-time**`listener` function for the event named `eventName` to the _beginning_ of the listeners array.
The next time `eventName` is triggered, this listener is removed, and then invoked.

Returns a reference to the `EventEmitter`, so that calls can be chained.

###### Parameters

| Parameter | Type | Description |
| ------ | ------ | ------ |
| `event` | `string` | - |
| `listener` | (...`args`: `any`[]) => `void` | The callback function |

###### Returns

`this`

###### Overrides

[`EventEmitter`](globals/index.md#eventemittert).[`prependOnceListener`](globals/index.md#prependoncelistener)

###### Call Signature

> **prependOnceListener**(`event`: `"close"`, `listener`: (`code`: `null` \| `number`, `signal`: `null` \| [`Signals`](globals/namespaces/QuickJS.md#signals)) => `void`): `this`

###### Parameters

| Parameter | Type |
| ------ | ------ |
| `event` | `"close"` |
| `listener` | (`code`: `null` \| `number`, `signal`: `null` \| [`Signals`](globals/namespaces/QuickJS.md#signals)) => `void` |

###### Returns

`this`

###### Overrides

`EventEmitter.prependOnceListener`

###### Call Signature

> **prependOnceListener**(`event`: `"error"`, `listener`: (`err`: `Error`) => `void`): `this`

###### Parameters

| Parameter | Type |
| ------ | ------ |
| `event` | `"error"` |
| `listener` | (`err`: `Error`) => `void` |

###### Returns

`this`

###### Overrides

`EventEmitter.prependOnceListener`

###### Call Signature

> **prependOnceListener**(`event`: `"exit"`, `listener`: (`code`: `null` \| `number`, `signal`: `null` \| [`Signals`](globals/namespaces/QuickJS.md#signals)) => `void`): `this`

###### Parameters

| Parameter | Type |
| ------ | ------ |
| `event` | `"exit"` |
| `listener` | (`code`: `null` \| `number`, `signal`: `null` \| [`Signals`](globals/namespaces/QuickJS.md#signals)) => `void` |

###### Returns

`this`

###### Overrides

`EventEmitter.prependOnceListener`

##### removeListener()

> **removeListener**\<`K`\>(`eventName`: [`EventKey`](dom-events.md#eventkey), `listener`: (...`args`: `any`[]) => `void`): `this`

Removes the specified `listener` from the listener array for the event named `eventName`.

`removeListener()` will remove, at most, one instance of a listener from the
listener array. If any single listener has been added multiple times to the
listener array for the specified `eventName`, then `removeListener()` must be
called multiple times to remove each instance.

Once an event is emitted, all listeners attached to it at the time of emitting are called in order.
This implies that any `removeListener()` calls _after_ emitting and _before_ the last listener finishes execution
will not remove them from `emit()` in progress. Subsequent events behave as expected.

```js
import { EventEmitter } from 'events';
class MyEmitter extends EventEmitter {}
const myEmitter = new MyEmitter();

const callbackA = () => {
  console.log('A');
  myEmitter.removeListener('event', callbackB);
};

const callbackB = () => {
  console.log('B');
};

myEmitter.on('event', callbackA);

myEmitter.on('event', callbackB);

// callbackA removes listener callbackB but it will still be called.
// Internal listener array at time of emit [callbackA, callbackB]
myEmitter.emit('event');
// Prints:
//   A
//   B

// callbackB is now removed.
// Internal listener array [callbackA]
myEmitter.emit('event');
// Prints:
//   A
```

Because listeners are managed using an internal array, calling this will
change the position indices of any listener registered _after_ the listener
being removed. This will not impact the order in which listeners are called,
but it means that any copies of the listener array as returned by
the `emitter.listeners()` method will need to be recreated.

When a single function has been added as a handler multiple times for a single
event (as in the example below), `removeListener()` will remove the most
recently added instance. In the example the `once('ping')` listener is removed:

```js
import { EventEmitter } from 'events';
const ee = new EventEmitter();

function pong() {
  console.log('pong');
}

ee.on('ping', pong);
ee.once('ping', pong);
ee.removeListener('ping', pong);

ee.emit('ping');
ee.emit('ping');
```

Returns a reference to the `EventEmitter`, so that calls can be chained.

###### Type Parameters

| Type Parameter |
| ------ |
| `K` |

###### Parameters

| Parameter | Type |
| ------ | ------ |
| `eventName` | [`EventKey`](dom-events.md#eventkey) |
| `listener` | (...`args`: `any`[]) => `void` |

###### Returns

`this`

###### Inherited from

[`EventEmitter`](globals/index.md#eventemittert).[`removeListener`](globals/index.md#removelistener)

## Interfaces

### ChildProcessByStdio\<I, O, E\>

Instances of the `ChildProcess` represent spawned child processes.

Instances of `ChildProcess` are not intended to be created directly. Rather,
use the [spawn](child_process.md#spawn) method to create instances of `ChildProcess`.

#### Extends

- [`ChildProcess`](child_process.md#childprocess)

#### Type Parameters

| Type Parameter |
| ------ |
| `I` *extends* `null` \| [`DefaultWritableStream`](stream.md#defaultwritablestream) |
| `O` *extends* `null` \| [`DefaultReadableStream`](stream.md#defaultreadablestream) |
| `E` *extends* `null` \| [`DefaultReadableStream`](stream.md#defaultreadablestream) |

#### Properties

##### pid?

> `readonly` `optional` **pid**: `number`

Returns the process identifier (PID) of the child process. If the child process
fails to spawn due to errors, then the value is `undefined` and `error` is
emitted.

```js
const { spawn } = require('child_process');
const grep = spawn('grep', ['ssh']);

console.log(`Spawned child pid: ${grep.pid}`);
grep.stdin.end();
```

###### Inherited from

[`ChildProcess`](child_process.md#childprocess).[`pid`](child_process.md#pid)

##### stderr

> **stderr**: `E`

A `Readable Stream` that represents the child process's `stderr`.

If the child was spawned with `stdio[2]` set to anything other than `'pipe'`,
then this will be `null`.

`subprocess.stderr` is an alias for `subprocess.stdio[2]`. Both properties will
refer to the same value.

The `subprocess.stderr` property can be `null` or `undefined` if the child process could not be successfully spawned.

###### Overrides

[`ChildProcess`](child_process.md#childprocess).[`stderr`](child_process.md#stderr)

##### stdin

> **stdin**: `I`

A `Writable Stream` that represents the child process's `stdin`.

If a child process waits to read all of its input, the child will not continue
until this stream has been closed via `end()`.

If the child was spawned with `stdio[0]` set to anything other than `'pipe'`,
then this will be `null`.

`subprocess.stdin` is an alias for `subprocess.stdio[0]`. Both properties will
refer to the same value.

The `subprocess.stdin` property can be `null` or `undefined` if the child process could not be successfully spawned.

###### Overrides

[`ChildProcess`](child_process.md#childprocess).[`stdin`](child_process.md#stdin)

##### stdout

> **stdout**: `O`

A `Readable Stream` that represents the child process's `stdout`.

If the child was spawned with `stdio[1]` set to anything other than `'pipe'`,
then this will be `null`.

`subprocess.stdout` is an alias for `subprocess.stdio[1]`. Both properties will
refer to the same value.

```js
const { spawn } = require('child_process');

const subprocess = spawn('ls');

subprocess.stdout.on('data', (data) => {
  console.log(`Received chunk ${data}`);
});
```

The `subprocess.stdout` property can be `null` or `undefined` if the child process could not be successfully spawned.

###### Overrides

[`ChildProcess`](child_process.md#childprocess).[`stdout`](child_process.md#stdout)

#### Methods

##### \[dispose\]()

> **\[dispose\]**(): `void`

Calls [ChildProcess.kill](child_process.md#kill) with `'SIGTERM'`.

###### Returns

`void`

###### Inherited from

[`ChildProcess`](child_process.md#childprocess).[`[dispose]`](child_process.md#dispose)

##### addListener()

###### Call Signature

> **addListener**(`event`: `string`, `listener`: (...`args`: `any`[]) => `void`): `this`

events.EventEmitter
1. close
2. error
3. exit

###### Parameters

| Parameter | Type |
| ------ | ------ |
| `event` | `string` |
| `listener` | (...`args`: `any`[]) => `void` |

###### Returns

`this`

###### Inherited from

[`ChildProcess`](child_process.md#childprocess).[`addListener`](child_process.md#addlistener)

###### Call Signature

> **addListener**(`event`: `"close"`, `listener`: (`code`: `null` \| `number`, `signal`: `null` \| [`Signals`](globals/namespaces/QuickJS.md#signals)) => `void`): `this`

events.EventEmitter
1. close
2. error
3. exit

###### Parameters

| Parameter | Type |
| ------ | ------ |
| `event` | `"close"` |
| `listener` | (`code`: `null` \| `number`, `signal`: `null` \| [`Signals`](globals/namespaces/QuickJS.md#signals)) => `void` |

###### Returns

`this`

###### Inherited from

[`ChildProcess`](child_process.md#childprocess).[`addListener`](child_process.md#addlistener)

###### Call Signature

> **addListener**(`event`: `"error"`, `listener`: (`err`: `Error`) => `void`): `this`

events.EventEmitter
1. close
2. error
3. exit

###### Parameters

| Parameter | Type |
| ------ | ------ |
| `event` | `"error"` |
| `listener` | (`err`: `Error`) => `void` |

###### Returns

`this`

###### Inherited from

[`ChildProcess`](child_process.md#childprocess).[`addListener`](child_process.md#addlistener)

###### Call Signature

> **addListener**(`event`: `"exit"`, `listener`: (`code`: `null` \| `number`, `signal`: `null` \| [`Signals`](globals/namespaces/QuickJS.md#signals)) => `void`): `this`

events.EventEmitter
1. close
2. error
3. exit

###### Parameters

| Parameter | Type |
| ------ | ------ |
| `event` | `"exit"` |
| `listener` | (`code`: `null` \| `number`, `signal`: `null` \| [`Signals`](globals/namespaces/QuickJS.md#signals)) => `void` |

###### Returns

`this`

###### Inherited from

[`ChildProcess`](child_process.md#childprocess).[`addListener`](child_process.md#addlistener)

##### emit()

###### Call Signature

> **emit**(`event`: `string` \| `symbol`, ...`args`: `any`[]): `boolean`

Synchronously calls each of the listeners registered for the event named `eventName`, in the order they were registered, passing the supplied arguments
to each.

```js
import { EventEmitter } from 'events';
const myEmitter = new EventEmitter();

// First listener
myEmitter.on('event', function firstListener() {
  console.log('Helloooo! first listener');
});
// Second listener
myEmitter.on('event', function secondListener(arg1, arg2) {
  console.log(`event with parameters ${arg1}, ${arg2} in second listener`);
});
// Third listener
myEmitter.on('event', function thirdListener(...args) {
  const parameters = args.join(', ');
  console.log(`event with parameters ${parameters} in third listener`);
});

myEmitter.emit('event', 1, 2, 3, 4, 5);

// Prints:
// Helloooo! first listener
// event with parameters 1, 2 in second listener
// event with parameters 1, 2, 3, 4, 5 in third listener
```

###### Parameters

| Parameter | Type |
| ------ | ------ |
| `event` | `string` \| `symbol` |
| ...`args` | `any`[] |

###### Returns

`boolean`

###### Inherited from

[`ChildProcess`](child_process.md#childprocess).[`emit`](child_process.md#emit)

###### Call Signature

> **emit**(`event`: `"close"`, `code`: `null` \| `number`, `signal`: `null` \| [`Signals`](globals/namespaces/QuickJS.md#signals)): `boolean`

###### Parameters

| Parameter | Type |
| ------ | ------ |
| `event` | `"close"` |
| `code` | `null` \| `number` |
| `signal` | `null` \| [`Signals`](globals/namespaces/QuickJS.md#signals) |

###### Returns

`boolean`

###### Inherited from

[`ChildProcess`](child_process.md#childprocess).[`emit`](child_process.md#emit)

###### Call Signature

> **emit**(`event`: `"error"`, `err`: `Error`): `boolean`

###### Parameters

| Parameter | Type |
| ------ | ------ |
| `event` | `"error"` |
| `err` | `Error` |

###### Returns

`boolean`

###### Inherited from

[`ChildProcess`](child_process.md#childprocess).[`emit`](child_process.md#emit)

###### Call Signature

> **emit**(`event`: `"exit"`, `code`: `null` \| `number`, `signal`: `null` \| [`Signals`](globals/namespaces/QuickJS.md#signals)): `boolean`

###### Parameters

| Parameter | Type |
| ------ | ------ |
| `event` | `"exit"` |
| `code` | `null` \| `number` |
| `signal` | `null` \| [`Signals`](globals/namespaces/QuickJS.md#signals) |

###### Returns

`boolean`

###### Inherited from

[`ChildProcess`](child_process.md#childprocess).[`emit`](child_process.md#emit)

##### eventNames()

> **eventNames**(): [`EventKey`](dom-events.md#eventkey)[]

Returns an array listing the events for which the emitter has registered
listeners. The values in the array are strings or `Symbol`s.

```js
import { EventEmitter } from 'events';

const myEE = new EventEmitter();
myEE.on('foo', () => {});
myEE.on('bar', () => {});

const sym = Symbol('symbol');
myEE.on(sym, () => {});

console.log(myEE.eventNames());
// Prints: [ 'foo', 'bar', Symbol(symbol) ]
```

###### Returns

[`EventKey`](dom-events.md#eventkey)[]

###### Inherited from

[`ChildProcess`](child_process.md#childprocess).[`eventNames`](child_process.md#eventnames)

##### kill()

> **kill**(`signal`?: `number` \| [`Signals`](globals/namespaces/QuickJS.md#signals)): `boolean`

The `subprocess.kill()` method sends a signal to the child process. If no
argument is given, the process will be sent the `'SIGTERM'` signal. See [`signal(7)`](http://man7.org/linux/man-pages/man7/signal.7.html) for a list of available signals. This function
returns `true` if [`kill(2)`](http://man7.org/linux/man-pages/man2/kill.2.html) succeeds, and `false` otherwise.

```js
const { spawn } = require('child_process');
const grep = spawn('grep', ['ssh']);

grep.on('close', (code, signal) => {
  console.log(
    `child process terminated due to receipt of signal ${signal}`);
});

// Send SIGHUP to process.
grep.kill('SIGHUP');
```

The `ChildProcess` object may emit an `'error'` event if the signal
cannot be delivered. Sending a signal to a child process that has already exited
is not an error but may have unforeseen consequences. Specifically, if the
process identifier (PID) has been reassigned to another process, the signal will
be delivered to that process instead which can have unexpected results.

While the function is called `kill`, the signal delivered to the child process
may not actually terminate the process.

See [`kill(2)`](http://man7.org/linux/man-pages/man2/kill.2.html) for reference.

On Windows, where POSIX signals do not exist, the `signal` argument will be
ignored, and the process will be killed forcefully and abruptly (similar to `'SIGKILL'`).
See `Signal Events` for more details.

On Linux, child processes of child processes will not be terminated
when attempting to kill their parent. This is likely to happen when running a
new process in a shell or with the use of the `shell` option of `ChildProcess`:

```js
'use strict';
const { spawn } = require('child_process');

const subprocess = spawn(
  'sh',
  [
    '-c',
    `node -e "setInterval(() => {
      console.log(process.pid, 'is alive')
    }, 500);"`,
  ], {
    stdio: ['inherit', 'inherit', 'inherit'],
  },
);

setTimeout(() => {
  subprocess.kill(); // Does not terminate the Node.js process in the shell.
}, 2000);
```

###### Parameters

| Parameter | Type |
| ------ | ------ |
| `signal`? | `number` \| [`Signals`](globals/namespaces/QuickJS.md#signals) |

###### Returns

`boolean`

###### Inherited from

[`ChildProcess`](child_process.md#childprocess).[`kill`](child_process.md#kill)

##### off()

> **off**\<`K`\>(`eventName`: [`EventKey`](dom-events.md#eventkey), `listener`: (...`args`: `any`[]) => `void`): `this`

Alias for `emitter.removeListener()`.

###### Type Parameters

| Type Parameter |
| ------ |
| `K` |

###### Parameters

| Parameter | Type |
| ------ | ------ |
| `eventName` | [`EventKey`](dom-events.md#eventkey) |
| `listener` | (...`args`: `any`[]) => `void` |

###### Returns

`this`

###### Inherited from

[`ChildProcess`](child_process.md#childprocess).[`off`](child_process.md#off)

##### on()

###### Call Signature

> **on**(`event`: `string`, `listener`: (...`args`: `any`[]) => `void`): `this`

Adds the `listener` function to the end of the listeners array for the event
named `eventName`. No checks are made to see if the `listener` has already
been added. Multiple calls passing the same combination of `eventName` and
`listener` will result in the `listener` being added, and called, multiple times.

```js
server.on('connection', (stream) => {
  console.log('someone connected!');
});
```

Returns a reference to the `EventEmitter`, so that calls can be chained.

By default, event listeners are invoked in the order they are added. The `emitter.prependListener()` method can be used as an alternative to add the
event listener to the beginning of the listeners array.

```js
import { EventEmitter } from 'events';
const myEE = new EventEmitter();
myEE.on('foo', () => console.log('a'));
myEE.prependListener('foo', () => console.log('b'));
myEE.emit('foo');
// Prints:
//   b
//   a
```

###### Parameters

| Parameter | Type | Description |
| ------ | ------ | ------ |
| `event` | `string` | - |
| `listener` | (...`args`: `any`[]) => `void` | The callback function |

###### Returns

`this`

###### Inherited from

[`ChildProcess`](child_process.md#childprocess).[`on`](child_process.md#on)

###### Call Signature

> **on**(`event`: `"close"`, `listener`: (`code`: `null` \| `number`, `signal`: `null` \| [`Signals`](globals/namespaces/QuickJS.md#signals)) => `void`): `this`

###### Parameters

| Parameter | Type |
| ------ | ------ |
| `event` | `"close"` |
| `listener` | (`code`: `null` \| `number`, `signal`: `null` \| [`Signals`](globals/namespaces/QuickJS.md#signals)) => `void` |

###### Returns

`this`

###### Inherited from

[`ChildProcess`](child_process.md#childprocess).[`on`](child_process.md#on)

###### Call Signature

> **on**(`event`: `"error"`, `listener`: (`err`: `Error`) => `void`): `this`

###### Parameters

| Parameter | Type |
| ------ | ------ |
| `event` | `"error"` |
| `listener` | (`err`: `Error`) => `void` |

###### Returns

`this`

###### Inherited from

[`ChildProcess`](child_process.md#childprocess).[`on`](child_process.md#on)

###### Call Signature

> **on**(`event`: `"exit"`, `listener`: (`code`: `null` \| `number`, `signal`: `null` \| [`Signals`](globals/namespaces/QuickJS.md#signals)) => `void`): `this`

###### Parameters

| Parameter | Type |
| ------ | ------ |
| `event` | `"exit"` |
| `listener` | (`code`: `null` \| `number`, `signal`: `null` \| [`Signals`](globals/namespaces/QuickJS.md#signals)) => `void` |

###### Returns

`this`

###### Inherited from

[`ChildProcess`](child_process.md#childprocess).[`on`](child_process.md#on)

##### once()

###### Call Signature

> **once**(`event`: `string`, `listener`: (...`args`: `any`[]) => `void`): `this`

Adds a **one-time** `listener` function for the event named `eventName`. The
next time `eventName` is triggered, this listener is removed and then invoked.

Returns a reference to the `EventEmitter`, so that calls can be chained.

By default, event listeners are invoked in the order they are added. The `emitter.prependOnceListener()` method can be used as an alternative to add the
event listener to the beginning of the listeners array.

```js
import { EventEmitter } from 'events';
const myEE = new EventEmitter();
myEE.once('foo', () => console.log('a'));
myEE.prependOnceListener('foo', () => console.log('b'));
myEE.emit('foo');
// Prints:
//   b
//   a
```

###### Parameters

| Parameter | Type | Description |
| ------ | ------ | ------ |
| `event` | `string` | - |
| `listener` | (...`args`: `any`[]) => `void` | The callback function |

###### Returns

`this`

###### Since

v0.3.0

###### Inherited from

[`ChildProcess`](child_process.md#childprocess).[`once`](child_process.md#once)

###### Call Signature

> **once**(`event`: `"close"`, `listener`: (`code`: `null` \| `number`, `signal`: `null` \| [`Signals`](globals/namespaces/QuickJS.md#signals)) => `void`): `this`

###### Parameters

| Parameter | Type |
| ------ | ------ |
| `event` | `"close"` |
| `listener` | (`code`: `null` \| `number`, `signal`: `null` \| [`Signals`](globals/namespaces/QuickJS.md#signals)) => `void` |

###### Returns

`this`

###### Inherited from

[`ChildProcess`](child_process.md#childprocess).[`once`](child_process.md#once)

###### Call Signature

> **once**(`event`: `"error"`, `listener`: (`err`: `Error`) => `void`): `this`

###### Parameters

| Parameter | Type |
| ------ | ------ |
| `event` | `"error"` |
| `listener` | (`err`: `Error`) => `void` |

###### Returns

`this`

###### Inherited from

[`ChildProcess`](child_process.md#childprocess).[`once`](child_process.md#once)

###### Call Signature

> **once**(`event`: `"exit"`, `listener`: (`code`: `null` \| `number`, `signal`: `null` \| [`Signals`](globals/namespaces/QuickJS.md#signals)) => `void`): `this`

###### Parameters

| Parameter | Type |
| ------ | ------ |
| `event` | `"exit"` |
| `listener` | (`code`: `null` \| `number`, `signal`: `null` \| [`Signals`](globals/namespaces/QuickJS.md#signals)) => `void` |

###### Returns

`this`

###### Inherited from

[`ChildProcess`](child_process.md#childprocess).[`once`](child_process.md#once)

##### prependListener()

###### Call Signature

> **prependListener**(`event`: `string`, `listener`: (...`args`: `any`[]) => `void`): `this`

Adds the `listener` function to the _beginning_ of the listeners array for the
event named `eventName`. No checks are made to see if the `listener` has
already been added. Multiple calls passing the same combination of `eventName`
and `listener` will result in the `listener` being added, and called, multiple times.

Returns a reference to the `EventEmitter`, so that calls can be chained.

###### Parameters

| Parameter | Type | Description |
| ------ | ------ | ------ |
| `event` | `string` | - |
| `listener` | (...`args`: `any`[]) => `void` | The callback function |

###### Returns

`this`

###### Inherited from

[`ChildProcess`](child_process.md#childprocess).[`prependListener`](child_process.md#prependlistener)

###### Call Signature

> **prependListener**(`event`: `"close"`, `listener`: (`code`: `null` \| `number`, `signal`: `null` \| [`Signals`](globals/namespaces/QuickJS.md#signals)) => `void`): `this`

###### Parameters

| Parameter | Type |
| ------ | ------ |
| `event` | `"close"` |
| `listener` | (`code`: `null` \| `number`, `signal`: `null` \| [`Signals`](globals/namespaces/QuickJS.md#signals)) => `void` |

###### Returns

`this`

###### Inherited from

[`ChildProcess`](child_process.md#childprocess).[`prependListener`](child_process.md#prependlistener)

###### Call Signature

> **prependListener**(`event`: `"error"`, `listener`: (`err`: `Error`) => `void`): `this`

###### Parameters

| Parameter | Type |
| ------ | ------ |
| `event` | `"error"` |
| `listener` | (`err`: `Error`) => `void` |

###### Returns

`this`

###### Inherited from

[`ChildProcess`](child_process.md#childprocess).[`prependListener`](child_process.md#prependlistener)

###### Call Signature

> **prependListener**(`event`: `"exit"`, `listener`: (`code`: `null` \| `number`, `signal`: `null` \| [`Signals`](globals/namespaces/QuickJS.md#signals)) => `void`): `this`

###### Parameters

| Parameter | Type |
| ------ | ------ |
| `event` | `"exit"` |
| `listener` | (`code`: `null` \| `number`, `signal`: `null` \| [`Signals`](globals/namespaces/QuickJS.md#signals)) => `void` |

###### Returns

`this`

###### Inherited from

[`ChildProcess`](child_process.md#childprocess).[`prependListener`](child_process.md#prependlistener)

##### prependOnceListener()

###### Call Signature

> **prependOnceListener**(`event`: `string`, `listener`: (...`args`: `any`[]) => `void`): `this`

Adds a **one-time**`listener` function for the event named `eventName` to the _beginning_ of the listeners array.
The next time `eventName` is triggered, this listener is removed, and then invoked.

Returns a reference to the `EventEmitter`, so that calls can be chained.

###### Parameters

| Parameter | Type | Description |
| ------ | ------ | ------ |
| `event` | `string` | - |
| `listener` | (...`args`: `any`[]) => `void` | The callback function |

###### Returns

`this`

###### Inherited from

[`ChildProcess`](child_process.md#childprocess).[`prependOnceListener`](child_process.md#prependoncelistener)

###### Call Signature

> **prependOnceListener**(`event`: `"close"`, `listener`: (`code`: `null` \| `number`, `signal`: `null` \| [`Signals`](globals/namespaces/QuickJS.md#signals)) => `void`): `this`

###### Parameters

| Parameter | Type |
| ------ | ------ |
| `event` | `"close"` |
| `listener` | (`code`: `null` \| `number`, `signal`: `null` \| [`Signals`](globals/namespaces/QuickJS.md#signals)) => `void` |

###### Returns

`this`

###### Inherited from

[`ChildProcess`](child_process.md#childprocess).[`prependOnceListener`](child_process.md#prependoncelistener)

###### Call Signature

> **prependOnceListener**(`event`: `"error"`, `listener`: (`err`: `Error`) => `void`): `this`

###### Parameters

| Parameter | Type |
| ------ | ------ |
| `event` | `"error"` |
| `listener` | (`err`: `Error`) => `void` |

###### Returns

`this`

###### Inherited from

[`ChildProcess`](child_process.md#childprocess).[`prependOnceListener`](child_process.md#prependoncelistener)

###### Call Signature

> **prependOnceListener**(`event`: `"exit"`, `listener`: (`code`: `null` \| `number`, `signal`: `null` \| [`Signals`](globals/namespaces/QuickJS.md#signals)) => `void`): `this`

###### Parameters

| Parameter | Type |
| ------ | ------ |
| `event` | `"exit"` |
| `listener` | (`code`: `null` \| `number`, `signal`: `null` \| [`Signals`](globals/namespaces/QuickJS.md#signals)) => `void` |

###### Returns

`this`

###### Inherited from

[`ChildProcess`](child_process.md#childprocess).[`prependOnceListener`](child_process.md#prependoncelistener)

##### removeListener()

> **removeListener**\<`K`\>(`eventName`: [`EventKey`](dom-events.md#eventkey), `listener`: (...`args`: `any`[]) => `void`): `this`

Removes the specified `listener` from the listener array for the event named `eventName`.

`removeListener()` will remove, at most, one instance of a listener from the
listener array. If any single listener has been added multiple times to the
listener array for the specified `eventName`, then `removeListener()` must be
called multiple times to remove each instance.

Once an event is emitted, all listeners attached to it at the time of emitting are called in order.
This implies that any `removeListener()` calls _after_ emitting and _before_ the last listener finishes execution
will not remove them from `emit()` in progress. Subsequent events behave as expected.

```js
import { EventEmitter } from 'events';
class MyEmitter extends EventEmitter {}
const myEmitter = new MyEmitter();

const callbackA = () => {
  console.log('A');
  myEmitter.removeListener('event', callbackB);
};

const callbackB = () => {
  console.log('B');
};

myEmitter.on('event', callbackA);

myEmitter.on('event', callbackB);

// callbackA removes listener callbackB but it will still be called.
// Internal listener array at time of emit [callbackA, callbackB]
myEmitter.emit('event');
// Prints:
//   A
//   B

// callbackB is now removed.
// Internal listener array [callbackA]
myEmitter.emit('event');
// Prints:
//   A
```

Because listeners are managed using an internal array, calling this will
change the position indices of any listener registered _after_ the listener
being removed. This will not impact the order in which listeners are called,
but it means that any copies of the listener array as returned by
the `emitter.listeners()` method will need to be recreated.

When a single function has been added as a handler multiple times for a single
event (as in the example below), `removeListener()` will remove the most
recently added instance. In the example the `once('ping')` listener is removed:

```js
import { EventEmitter } from 'events';
const ee = new EventEmitter();

function pong() {
  console.log('pong');
}

ee.on('ping', pong);
ee.once('ping', pong);
ee.removeListener('ping', pong);

ee.emit('ping');
ee.emit('ping');
```

Returns a reference to the `EventEmitter`, so that calls can be chained.

###### Type Parameters

| Type Parameter |
| ------ |
| `K` |

###### Parameters

| Parameter | Type |
| ------ | ------ |
| `eventName` | [`EventKey`](dom-events.md#eventkey) |
| `listener` | (...`args`: `any`[]) => `void` |

###### Returns

`this`

###### Inherited from

[`ChildProcess`](child_process.md#childprocess).[`removeListener`](child_process.md#removelistener)

***

### ChildProcessWithoutNullStreams

Instances of the `ChildProcess` represent spawned child processes.

Instances of `ChildProcess` are not intended to be created directly. Rather,
use the [spawn](child_process.md#spawn) method to create instances of `ChildProcess`.

#### Extends

- [`ChildProcess`](child_process.md#childprocess)

#### Properties

##### pid?

> `readonly` `optional` **pid**: `number`

Returns the process identifier (PID) of the child process. If the child process
fails to spawn due to errors, then the value is `undefined` and `error` is
emitted.

```js
const { spawn } = require('child_process');
const grep = spawn('grep', ['ssh']);

console.log(`Spawned child pid: ${grep.pid}`);
grep.stdin.end();
```

###### Inherited from

[`ChildProcess`](child_process.md#childprocess).[`pid`](child_process.md#pid)

##### stderr

> **stderr**: [`DefaultReadableStream`](stream.md#defaultreadablestream)

A `Readable Stream` that represents the child process's `stderr`.

If the child was spawned with `stdio[2]` set to anything other than `'pipe'`,
then this will be `null`.

`subprocess.stderr` is an alias for `subprocess.stdio[2]`. Both properties will
refer to the same value.

The `subprocess.stderr` property can be `null` or `undefined` if the child process could not be successfully spawned.

###### Overrides

[`ChildProcess`](child_process.md#childprocess).[`stderr`](child_process.md#stderr)

##### stdin

> **stdin**: [`DefaultWritableStream`](stream.md#defaultwritablestream)

A `Writable Stream` that represents the child process's `stdin`.

If a child process waits to read all of its input, the child will not continue
until this stream has been closed via `end()`.

If the child was spawned with `stdio[0]` set to anything other than `'pipe'`,
then this will be `null`.

`subprocess.stdin` is an alias for `subprocess.stdio[0]`. Both properties will
refer to the same value.

The `subprocess.stdin` property can be `null` or `undefined` if the child process could not be successfully spawned.

###### Overrides

[`ChildProcess`](child_process.md#childprocess).[`stdin`](child_process.md#stdin)

##### stdout

> **stdout**: [`DefaultReadableStream`](stream.md#defaultreadablestream)

A `Readable Stream` that represents the child process's `stdout`.

If the child was spawned with `stdio[1]` set to anything other than `'pipe'`,
then this will be `null`.

`subprocess.stdout` is an alias for `subprocess.stdio[1]`. Both properties will
refer to the same value.

```js
const { spawn } = require('child_process');

const subprocess = spawn('ls');

subprocess.stdout.on('data', (data) => {
  console.log(`Received chunk ${data}`);
});
```

The `subprocess.stdout` property can be `null` or `undefined` if the child process could not be successfully spawned.

###### Overrides

[`ChildProcess`](child_process.md#childprocess).[`stdout`](child_process.md#stdout)

#### Methods

##### \[dispose\]()

> **\[dispose\]**(): `void`

Calls [ChildProcess.kill](child_process.md#kill) with `'SIGTERM'`.

###### Returns

`void`

###### Inherited from

[`ChildProcess`](child_process.md#childprocess).[`[dispose]`](child_process.md#dispose)

##### addListener()

###### Call Signature

> **addListener**(`event`: `string`, `listener`: (...`args`: `any`[]) => `void`): `this`

events.EventEmitter
1. close
2. error
3. exit

###### Parameters

| Parameter | Type |
| ------ | ------ |
| `event` | `string` |
| `listener` | (...`args`: `any`[]) => `void` |

###### Returns

`this`

###### Inherited from

[`ChildProcess`](child_process.md#childprocess).[`addListener`](child_process.md#addlistener)

###### Call Signature

> **addListener**(`event`: `"close"`, `listener`: (`code`: `null` \| `number`, `signal`: `null` \| [`Signals`](globals/namespaces/QuickJS.md#signals)) => `void`): `this`

events.EventEmitter
1. close
2. error
3. exit

###### Parameters

| Parameter | Type |
| ------ | ------ |
| `event` | `"close"` |
| `listener` | (`code`: `null` \| `number`, `signal`: `null` \| [`Signals`](globals/namespaces/QuickJS.md#signals)) => `void` |

###### Returns

`this`

###### Inherited from

[`ChildProcess`](child_process.md#childprocess).[`addListener`](child_process.md#addlistener)

###### Call Signature

> **addListener**(`event`: `"error"`, `listener`: (`err`: `Error`) => `void`): `this`

events.EventEmitter
1. close
2. error
3. exit

###### Parameters

| Parameter | Type |
| ------ | ------ |
| `event` | `"error"` |
| `listener` | (`err`: `Error`) => `void` |

###### Returns

`this`

###### Inherited from

[`ChildProcess`](child_process.md#childprocess).[`addListener`](child_process.md#addlistener)

###### Call Signature

> **addListener**(`event`: `"exit"`, `listener`: (`code`: `null` \| `number`, `signal`: `null` \| [`Signals`](globals/namespaces/QuickJS.md#signals)) => `void`): `this`

events.EventEmitter
1. close
2. error
3. exit

###### Parameters

| Parameter | Type |
| ------ | ------ |
| `event` | `"exit"` |
| `listener` | (`code`: `null` \| `number`, `signal`: `null` \| [`Signals`](globals/namespaces/QuickJS.md#signals)) => `void` |

###### Returns

`this`

###### Inherited from

[`ChildProcess`](child_process.md#childprocess).[`addListener`](child_process.md#addlistener)

##### emit()

###### Call Signature

> **emit**(`event`: `string` \| `symbol`, ...`args`: `any`[]): `boolean`

Synchronously calls each of the listeners registered for the event named `eventName`, in the order they were registered, passing the supplied arguments
to each.

```js
import { EventEmitter } from 'events';
const myEmitter = new EventEmitter();

// First listener
myEmitter.on('event', function firstListener() {
  console.log('Helloooo! first listener');
});
// Second listener
myEmitter.on('event', function secondListener(arg1, arg2) {
  console.log(`event with parameters ${arg1}, ${arg2} in second listener`);
});
// Third listener
myEmitter.on('event', function thirdListener(...args) {
  const parameters = args.join(', ');
  console.log(`event with parameters ${parameters} in third listener`);
});

myEmitter.emit('event', 1, 2, 3, 4, 5);

// Prints:
// Helloooo! first listener
// event with parameters 1, 2 in second listener
// event with parameters 1, 2, 3, 4, 5 in third listener
```

###### Parameters

| Parameter | Type |
| ------ | ------ |
| `event` | `string` \| `symbol` |
| ...`args` | `any`[] |

###### Returns

`boolean`

###### Inherited from

[`ChildProcess`](child_process.md#childprocess).[`emit`](child_process.md#emit)

###### Call Signature

> **emit**(`event`: `"close"`, `code`: `null` \| `number`, `signal`: `null` \| [`Signals`](globals/namespaces/QuickJS.md#signals)): `boolean`

###### Parameters

| Parameter | Type |
| ------ | ------ |
| `event` | `"close"` |
| `code` | `null` \| `number` |
| `signal` | `null` \| [`Signals`](globals/namespaces/QuickJS.md#signals) |

###### Returns

`boolean`

###### Inherited from

[`ChildProcess`](child_process.md#childprocess).[`emit`](child_process.md#emit)

###### Call Signature

> **emit**(`event`: `"error"`, `err`: `Error`): `boolean`

###### Parameters

| Parameter | Type |
| ------ | ------ |
| `event` | `"error"` |
| `err` | `Error` |

###### Returns

`boolean`

###### Inherited from

[`ChildProcess`](child_process.md#childprocess).[`emit`](child_process.md#emit)

###### Call Signature

> **emit**(`event`: `"exit"`, `code`: `null` \| `number`, `signal`: `null` \| [`Signals`](globals/namespaces/QuickJS.md#signals)): `boolean`

###### Parameters

| Parameter | Type |
| ------ | ------ |
| `event` | `"exit"` |
| `code` | `null` \| `number` |
| `signal` | `null` \| [`Signals`](globals/namespaces/QuickJS.md#signals) |

###### Returns

`boolean`

###### Inherited from

[`ChildProcess`](child_process.md#childprocess).[`emit`](child_process.md#emit)

##### eventNames()

> **eventNames**(): [`EventKey`](dom-events.md#eventkey)[]

Returns an array listing the events for which the emitter has registered
listeners. The values in the array are strings or `Symbol`s.

```js
import { EventEmitter } from 'events';

const myEE = new EventEmitter();
myEE.on('foo', () => {});
myEE.on('bar', () => {});

const sym = Symbol('symbol');
myEE.on(sym, () => {});

console.log(myEE.eventNames());
// Prints: [ 'foo', 'bar', Symbol(symbol) ]
```

###### Returns

[`EventKey`](dom-events.md#eventkey)[]

###### Inherited from

[`ChildProcess`](child_process.md#childprocess).[`eventNames`](child_process.md#eventnames)

##### kill()

> **kill**(`signal`?: `number` \| [`Signals`](globals/namespaces/QuickJS.md#signals)): `boolean`

The `subprocess.kill()` method sends a signal to the child process. If no
argument is given, the process will be sent the `'SIGTERM'` signal. See [`signal(7)`](http://man7.org/linux/man-pages/man7/signal.7.html) for a list of available signals. This function
returns `true` if [`kill(2)`](http://man7.org/linux/man-pages/man2/kill.2.html) succeeds, and `false` otherwise.

```js
const { spawn } = require('child_process');
const grep = spawn('grep', ['ssh']);

grep.on('close', (code, signal) => {
  console.log(
    `child process terminated due to receipt of signal ${signal}`);
});

// Send SIGHUP to process.
grep.kill('SIGHUP');
```

The `ChildProcess` object may emit an `'error'` event if the signal
cannot be delivered. Sending a signal to a child process that has already exited
is not an error but may have unforeseen consequences. Specifically, if the
process identifier (PID) has been reassigned to another process, the signal will
be delivered to that process instead which can have unexpected results.

While the function is called `kill`, the signal delivered to the child process
may not actually terminate the process.

See [`kill(2)`](http://man7.org/linux/man-pages/man2/kill.2.html) for reference.

On Windows, where POSIX signals do not exist, the `signal` argument will be
ignored, and the process will be killed forcefully and abruptly (similar to `'SIGKILL'`).
See `Signal Events` for more details.

On Linux, child processes of child processes will not be terminated
when attempting to kill their parent. This is likely to happen when running a
new process in a shell or with the use of the `shell` option of `ChildProcess`:

```js
'use strict';
const { spawn } = require('child_process');

const subprocess = spawn(
  'sh',
  [
    '-c',
    `node -e "setInterval(() => {
      console.log(process.pid, 'is alive')
    }, 500);"`,
  ], {
    stdio: ['inherit', 'inherit', 'inherit'],
  },
);

setTimeout(() => {
  subprocess.kill(); // Does not terminate the Node.js process in the shell.
}, 2000);
```

###### Parameters

| Parameter | Type |
| ------ | ------ |
| `signal`? | `number` \| [`Signals`](globals/namespaces/QuickJS.md#signals) |

###### Returns

`boolean`

###### Inherited from

[`ChildProcess`](child_process.md#childprocess).[`kill`](child_process.md#kill)

##### off()

> **off**\<`K`\>(`eventName`: [`EventKey`](dom-events.md#eventkey), `listener`: (...`args`: `any`[]) => `void`): `this`

Alias for `emitter.removeListener()`.

###### Type Parameters

| Type Parameter |
| ------ |
| `K` |

###### Parameters

| Parameter | Type |
| ------ | ------ |
| `eventName` | [`EventKey`](dom-events.md#eventkey) |
| `listener` | (...`args`: `any`[]) => `void` |

###### Returns

`this`

###### Inherited from

[`ChildProcess`](child_process.md#childprocess).[`off`](child_process.md#off)

##### on()

###### Call Signature

> **on**(`event`: `string`, `listener`: (...`args`: `any`[]) => `void`): `this`

Adds the `listener` function to the end of the listeners array for the event
named `eventName`. No checks are made to see if the `listener` has already
been added. Multiple calls passing the same combination of `eventName` and
`listener` will result in the `listener` being added, and called, multiple times.

```js
server.on('connection', (stream) => {
  console.log('someone connected!');
});
```

Returns a reference to the `EventEmitter`, so that calls can be chained.

By default, event listeners are invoked in the order they are added. The `emitter.prependListener()` method can be used as an alternative to add the
event listener to the beginning of the listeners array.

```js
import { EventEmitter } from 'events';
const myEE = new EventEmitter();
myEE.on('foo', () => console.log('a'));
myEE.prependListener('foo', () => console.log('b'));
myEE.emit('foo');
// Prints:
//   b
//   a
```

###### Parameters

| Parameter | Type | Description |
| ------ | ------ | ------ |
| `event` | `string` | - |
| `listener` | (...`args`: `any`[]) => `void` | The callback function |

###### Returns

`this`

###### Inherited from

[`ChildProcess`](child_process.md#childprocess).[`on`](child_process.md#on)

###### Call Signature

> **on**(`event`: `"close"`, `listener`: (`code`: `null` \| `number`, `signal`: `null` \| [`Signals`](globals/namespaces/QuickJS.md#signals)) => `void`): `this`

###### Parameters

| Parameter | Type |
| ------ | ------ |
| `event` | `"close"` |
| `listener` | (`code`: `null` \| `number`, `signal`: `null` \| [`Signals`](globals/namespaces/QuickJS.md#signals)) => `void` |

###### Returns

`this`

###### Inherited from

[`ChildProcess`](child_process.md#childprocess).[`on`](child_process.md#on)

###### Call Signature

> **on**(`event`: `"error"`, `listener`: (`err`: `Error`) => `void`): `this`

###### Parameters

| Parameter | Type |
| ------ | ------ |
| `event` | `"error"` |
| `listener` | (`err`: `Error`) => `void` |

###### Returns

`this`

###### Inherited from

[`ChildProcess`](child_process.md#childprocess).[`on`](child_process.md#on)

###### Call Signature

> **on**(`event`: `"exit"`, `listener`: (`code`: `null` \| `number`, `signal`: `null` \| [`Signals`](globals/namespaces/QuickJS.md#signals)) => `void`): `this`

###### Parameters

| Parameter | Type |
| ------ | ------ |
| `event` | `"exit"` |
| `listener` | (`code`: `null` \| `number`, `signal`: `null` \| [`Signals`](globals/namespaces/QuickJS.md#signals)) => `void` |

###### Returns

`this`

###### Inherited from

[`ChildProcess`](child_process.md#childprocess).[`on`](child_process.md#on)

##### once()

###### Call Signature

> **once**(`event`: `string`, `listener`: (...`args`: `any`[]) => `void`): `this`

Adds a **one-time** `listener` function for the event named `eventName`. The
next time `eventName` is triggered, this listener is removed and then invoked.

Returns a reference to the `EventEmitter`, so that calls can be chained.

By default, event listeners are invoked in the order they are added. The `emitter.prependOnceListener()` method can be used as an alternative to add the
event listener to the beginning of the listeners array.

```js
import { EventEmitter } from 'events';
const myEE = new EventEmitter();
myEE.once('foo', () => console.log('a'));
myEE.prependOnceListener('foo', () => console.log('b'));
myEE.emit('foo');
// Prints:
//   b
//   a
```

###### Parameters

| Parameter | Type | Description |
| ------ | ------ | ------ |
| `event` | `string` | - |
| `listener` | (...`args`: `any`[]) => `void` | The callback function |

###### Returns

`this`

###### Since

v0.3.0

###### Inherited from

[`ChildProcess`](child_process.md#childprocess).[`once`](child_process.md#once)

###### Call Signature

> **once**(`event`: `"close"`, `listener`: (`code`: `null` \| `number`, `signal`: `null` \| [`Signals`](globals/namespaces/QuickJS.md#signals)) => `void`): `this`

###### Parameters

| Parameter | Type |
| ------ | ------ |
| `event` | `"close"` |
| `listener` | (`code`: `null` \| `number`, `signal`: `null` \| [`Signals`](globals/namespaces/QuickJS.md#signals)) => `void` |

###### Returns

`this`

###### Inherited from

[`ChildProcess`](child_process.md#childprocess).[`once`](child_process.md#once)

###### Call Signature

> **once**(`event`: `"error"`, `listener`: (`err`: `Error`) => `void`): `this`

###### Parameters

| Parameter | Type |
| ------ | ------ |
| `event` | `"error"` |
| `listener` | (`err`: `Error`) => `void` |

###### Returns

`this`

###### Inherited from

[`ChildProcess`](child_process.md#childprocess).[`once`](child_process.md#once)

###### Call Signature

> **once**(`event`: `"exit"`, `listener`: (`code`: `null` \| `number`, `signal`: `null` \| [`Signals`](globals/namespaces/QuickJS.md#signals)) => `void`): `this`

###### Parameters

| Parameter | Type |
| ------ | ------ |
| `event` | `"exit"` |
| `listener` | (`code`: `null` \| `number`, `signal`: `null` \| [`Signals`](globals/namespaces/QuickJS.md#signals)) => `void` |

###### Returns

`this`

###### Inherited from

[`ChildProcess`](child_process.md#childprocess).[`once`](child_process.md#once)

##### prependListener()

###### Call Signature

> **prependListener**(`event`: `string`, `listener`: (...`args`: `any`[]) => `void`): `this`

Adds the `listener` function to the _beginning_ of the listeners array for the
event named `eventName`. No checks are made to see if the `listener` has
already been added. Multiple calls passing the same combination of `eventName`
and `listener` will result in the `listener` being added, and called, multiple times.

Returns a reference to the `EventEmitter`, so that calls can be chained.

###### Parameters

| Parameter | Type | Description |
| ------ | ------ | ------ |
| `event` | `string` | - |
| `listener` | (...`args`: `any`[]) => `void` | The callback function |

###### Returns

`this`

###### Inherited from

[`ChildProcess`](child_process.md#childprocess).[`prependListener`](child_process.md#prependlistener)

###### Call Signature

> **prependListener**(`event`: `"close"`, `listener`: (`code`: `null` \| `number`, `signal`: `null` \| [`Signals`](globals/namespaces/QuickJS.md#signals)) => `void`): `this`

###### Parameters

| Parameter | Type |
| ------ | ------ |
| `event` | `"close"` |
| `listener` | (`code`: `null` \| `number`, `signal`: `null` \| [`Signals`](globals/namespaces/QuickJS.md#signals)) => `void` |

###### Returns

`this`

###### Inherited from

[`ChildProcess`](child_process.md#childprocess).[`prependListener`](child_process.md#prependlistener)

###### Call Signature

> **prependListener**(`event`: `"error"`, `listener`: (`err`: `Error`) => `void`): `this`

###### Parameters

| Parameter | Type |
| ------ | ------ |
| `event` | `"error"` |
| `listener` | (`err`: `Error`) => `void` |

###### Returns

`this`

###### Inherited from

[`ChildProcess`](child_process.md#childprocess).[`prependListener`](child_process.md#prependlistener)

###### Call Signature

> **prependListener**(`event`: `"exit"`, `listener`: (`code`: `null` \| `number`, `signal`: `null` \| [`Signals`](globals/namespaces/QuickJS.md#signals)) => `void`): `this`

###### Parameters

| Parameter | Type |
| ------ | ------ |
| `event` | `"exit"` |
| `listener` | (`code`: `null` \| `number`, `signal`: `null` \| [`Signals`](globals/namespaces/QuickJS.md#signals)) => `void` |

###### Returns

`this`

###### Inherited from

[`ChildProcess`](child_process.md#childprocess).[`prependListener`](child_process.md#prependlistener)

##### prependOnceListener()

###### Call Signature

> **prependOnceListener**(`event`: `string`, `listener`: (...`args`: `any`[]) => `void`): `this`

Adds a **one-time**`listener` function for the event named `eventName` to the _beginning_ of the listeners array.
The next time `eventName` is triggered, this listener is removed, and then invoked.

Returns a reference to the `EventEmitter`, so that calls can be chained.

###### Parameters

| Parameter | Type | Description |
| ------ | ------ | ------ |
| `event` | `string` | - |
| `listener` | (...`args`: `any`[]) => `void` | The callback function |

###### Returns

`this`

###### Inherited from

[`ChildProcess`](child_process.md#childprocess).[`prependOnceListener`](child_process.md#prependoncelistener)

###### Call Signature

> **prependOnceListener**(`event`: `"close"`, `listener`: (`code`: `null` \| `number`, `signal`: `null` \| [`Signals`](globals/namespaces/QuickJS.md#signals)) => `void`): `this`

###### Parameters

| Parameter | Type |
| ------ | ------ |
| `event` | `"close"` |
| `listener` | (`code`: `null` \| `number`, `signal`: `null` \| [`Signals`](globals/namespaces/QuickJS.md#signals)) => `void` |

###### Returns

`this`

###### Inherited from

[`ChildProcess`](child_process.md#childprocess).[`prependOnceListener`](child_process.md#prependoncelistener)

###### Call Signature

> **prependOnceListener**(`event`: `"error"`, `listener`: (`err`: `Error`) => `void`): `this`

###### Parameters

| Parameter | Type |
| ------ | ------ |
| `event` | `"error"` |
| `listener` | (`err`: `Error`) => `void` |

###### Returns

`this`

###### Inherited from

[`ChildProcess`](child_process.md#childprocess).[`prependOnceListener`](child_process.md#prependoncelistener)

###### Call Signature

> **prependOnceListener**(`event`: `"exit"`, `listener`: (`code`: `null` \| `number`, `signal`: `null` \| [`Signals`](globals/namespaces/QuickJS.md#signals)) => `void`): `this`

###### Parameters

| Parameter | Type |
| ------ | ------ |
| `event` | `"exit"` |
| `listener` | (`code`: `null` \| `number`, `signal`: `null` \| [`Signals`](globals/namespaces/QuickJS.md#signals)) => `void` |

###### Returns

`this`

###### Inherited from

[`ChildProcess`](child_process.md#childprocess).[`prependOnceListener`](child_process.md#prependoncelistener)

##### removeListener()

> **removeListener**\<`K`\>(`eventName`: [`EventKey`](dom-events.md#eventkey), `listener`: (...`args`: `any`[]) => `void`): `this`

Removes the specified `listener` from the listener array for the event named `eventName`.

`removeListener()` will remove, at most, one instance of a listener from the
listener array. If any single listener has been added multiple times to the
listener array for the specified `eventName`, then `removeListener()` must be
called multiple times to remove each instance.

Once an event is emitted, all listeners attached to it at the time of emitting are called in order.
This implies that any `removeListener()` calls _after_ emitting and _before_ the last listener finishes execution
will not remove them from `emit()` in progress. Subsequent events behave as expected.

```js
import { EventEmitter } from 'events';
class MyEmitter extends EventEmitter {}
const myEmitter = new MyEmitter();

const callbackA = () => {
  console.log('A');
  myEmitter.removeListener('event', callbackB);
};

const callbackB = () => {
  console.log('B');
};

myEmitter.on('event', callbackA);

myEmitter.on('event', callbackB);

// callbackA removes listener callbackB but it will still be called.
// Internal listener array at time of emit [callbackA, callbackB]
myEmitter.emit('event');
// Prints:
//   A
//   B

// callbackB is now removed.
// Internal listener array [callbackA]
myEmitter.emit('event');
// Prints:
//   A
```

Because listeners are managed using an internal array, calling this will
change the position indices of any listener registered _after_ the listener
being removed. This will not impact the order in which listeners are called,
but it means that any copies of the listener array as returned by
the `emitter.listeners()` method will need to be recreated.

When a single function has been added as a handler multiple times for a single
event (as in the example below), `removeListener()` will remove the most
recently added instance. In the example the `once('ping')` listener is removed:

```js
import { EventEmitter } from 'events';
const ee = new EventEmitter();

function pong() {
  console.log('pong');
}

ee.on('ping', pong);
ee.once('ping', pong);
ee.removeListener('ping', pong);

ee.emit('ping');
ee.emit('ping');
```

Returns a reference to the `EventEmitter`, so that calls can be chained.

###### Type Parameters

| Type Parameter |
| ------ |
| `K` |

###### Parameters

| Parameter | Type |
| ------ | ------ |
| `eventName` | [`EventKey`](dom-events.md#eventkey) |
| `listener` | (...`args`: `any`[]) => `void` |

###### Returns

`this`

###### Inherited from

[`ChildProcess`](child_process.md#childprocess).[`removeListener`](child_process.md#removelistener)

***

### ProcessEnvOptions

#### Extended by

- [`SpawnOptions`](child_process.md#spawnoptions)

#### Properties

##### cwd?

> `optional` **cwd**: `string`

##### gid?

> `optional` **gid**: `number`

##### uid?

> `optional` **uid**: `number`

***

### SpawnOptions

#### Extends

- [`ProcessEnvOptions`](child_process.md#processenvoptions)

#### Extended by

- [`SpawnOptionsWithoutStdio`](child_process.md#spawnoptionswithoutstdio)
- [`SpawnOptionsWithStdioTuple`](child_process.md#spawnoptionswithstdiotuplestdin-stdout-stderr)

#### Properties

##### cwd?

> `optional` **cwd**: `string`

###### Inherited from

[`ProcessEnvOptions`](child_process.md#processenvoptions).[`cwd`](child_process.md#cwd)

##### gid?

> `optional` **gid**: `number`

###### Inherited from

[`ProcessEnvOptions`](child_process.md#processenvoptions).[`gid`](child_process.md#gid)

##### shell?

> `optional` **shell**: `string` \| `boolean`

##### stdio?

> `optional` **stdio**: [`StdioOptions`](child_process.md#stdiooptions)

Can be set to 'pipe', 'inherit', or 'ignore', or an array of these strings.
If passed as an array, the first element is used for `stdin`, the second for
`stdout`, and the third for `stderr`.

###### Default

```ts
'pipe'
```

##### uid?

> `optional` **uid**: `number`

###### Inherited from

[`ProcessEnvOptions`](child_process.md#processenvoptions).[`uid`](child_process.md#uid)

##### windowsVerbatimArguments?

> `optional` **windowsVerbatimArguments**: `boolean`

***

### SpawnOptionsWithoutStdio

#### Extends

- [`SpawnOptions`](child_process.md#spawnoptions)

#### Properties

##### cwd?

> `optional` **cwd**: `string`

###### Inherited from

[`SpawnOptions`](child_process.md#spawnoptions).[`cwd`](child_process.md#cwd-1)

##### gid?

> `optional` **gid**: `number`

###### Inherited from

[`SpawnOptions`](child_process.md#spawnoptions).[`gid`](child_process.md#gid-1)

##### shell?

> `optional` **shell**: `string` \| `boolean`

###### Inherited from

[`SpawnOptions`](child_process.md#spawnoptions).[`shell`](child_process.md#shell)

##### stdio?

> `optional` **stdio**: `"pipe"` \| [`StdioPipe`](child_process.md#stdiopipe)[]

Can be set to 'pipe', 'inherit', or 'ignore', or an array of these strings.
If passed as an array, the first element is used for `stdin`, the second for
`stdout`, and the third for `stderr`.

###### Default

```ts
'pipe'
```

###### Overrides

[`SpawnOptions`](child_process.md#spawnoptions).[`stdio`](child_process.md#stdio)

##### uid?

> `optional` **uid**: `number`

###### Inherited from

[`SpawnOptions`](child_process.md#spawnoptions).[`uid`](child_process.md#uid-1)

##### windowsVerbatimArguments?

> `optional` **windowsVerbatimArguments**: `boolean`

###### Inherited from

[`SpawnOptions`](child_process.md#spawnoptions).[`windowsVerbatimArguments`](child_process.md#windowsverbatimarguments)

***

### SpawnOptionsWithStdioTuple\<Stdin, Stdout, Stderr\>

#### Extends

- [`SpawnOptions`](child_process.md#spawnoptions)

#### Type Parameters

| Type Parameter |
| ------ |
| `Stdin` *extends* [`StdioNull`](child_process.md#stdionull) \| [`StdioPipe`](child_process.md#stdiopipe) |
| `Stdout` *extends* [`StdioNull`](child_process.md#stdionull) \| [`StdioPipe`](child_process.md#stdiopipe) |
| `Stderr` *extends* [`StdioNull`](child_process.md#stdionull) \| [`StdioPipe`](child_process.md#stdiopipe) |

#### Properties

##### cwd?

> `optional` **cwd**: `string`

###### Inherited from

[`SpawnOptions`](child_process.md#spawnoptions).[`cwd`](child_process.md#cwd-1)

##### gid?

> `optional` **gid**: `number`

###### Inherited from

[`SpawnOptions`](child_process.md#spawnoptions).[`gid`](child_process.md#gid-1)

##### shell?

> `optional` **shell**: `string` \| `boolean`

###### Inherited from

[`SpawnOptions`](child_process.md#spawnoptions).[`shell`](child_process.md#shell)

##### stdio

> **stdio**: \[`Stdin`, `Stdout`, `Stderr`\]

Can be set to 'pipe', 'inherit', or 'ignore', or an array of these strings.
If passed as an array, the first element is used for `stdin`, the second for
`stdout`, and the third for `stderr`.

###### Default

```ts
'pipe'
```

###### Overrides

[`SpawnOptions`](child_process.md#spawnoptions).[`stdio`](child_process.md#stdio)

##### uid?

> `optional` **uid**: `number`

###### Inherited from

[`SpawnOptions`](child_process.md#spawnoptions).[`uid`](child_process.md#uid-1)

##### windowsVerbatimArguments?

> `optional` **windowsVerbatimArguments**: `boolean`

###### Inherited from

[`SpawnOptions`](child_process.md#spawnoptions).[`windowsVerbatimArguments`](child_process.md#windowsverbatimarguments)

## Type Aliases

### IOType

> **IOType**: `"pipe"` \| `"ignore"` \| `"inherit"`

***

### StdioNull

> **StdioNull**: `"inherit"` \| `"ignore"`

***

### StdioOptions

> **StdioOptions**: [`IOType`](child_process.md#iotype) \| ([`IOType`](child_process.md#iotype) \| `number` \| `null` \| `undefined`)[]

***

### StdioPipe

> **StdioPipe**: `undefined` \| `null` \| [`StdioPipeNamed`](child_process.md#stdiopipenamed)

***

### StdioPipeNamed

> **StdioPipeNamed**: `"pipe"`

## Functions

### spawn()

#### Call Signature

> **spawn**(`command`: `string`, `options`?: [`SpawnOptionsWithoutStdio`](child_process.md#spawnoptionswithoutstdio)): [`ChildProcessWithoutNullStreams`](child_process.md#childprocesswithoutnullstreams)

The `child_process.spawn()` method spawns a new process using the given `command`, with command-line arguments in `args`.
If omitted, `args` defaults to an empty array.

**If the `shell` option is enabled, do not pass unsanitized user input to this**
**function. Any input containing shell metacharacters may be used to trigger**
**arbitrary command execution.**

A third argument may be used to specify additional options.

Use `cwd` to specify the working directory from which the process is spawned.
If not given, the default is to inherit the current working directory. If given,
but the path does not exist, the child process emits an `ENOENT` error
and exits immediately. `ENOENT` is also emitted when the command
does not exist.

Example of running `ls -lh /usr`, capturing `stdout`, `stderr`, and the
exit code:

```js
const { spawn } = require('child_process');
const ls = spawn('ls', ['-lh', '/usr']);

ls.stdout.on('data', (data) => {
  console.log(`stdout: ${data}`);
});

ls.stderr.on('data', (data) => {
  console.error(`stderr: ${data}`);
});

ls.on('close', (code) => {
  console.log(`child process exited with code ${code}`);
});
```

Example: A very elaborate way to run `ps ax | grep ssh`

```js
const { spawn } = require('child_process');
const ps = spawn('ps', ['ax']);
const grep = spawn('grep', ['ssh']);

ps.stdout.on('data', (data) => {
  grep.stdin.write(data);
});

ps.stderr.on('data', (data) => {
  console.error(`ps stderr: ${data}`);
});

ps.on('close', (code) => {
  if (code !== 0) {
    console.log(`ps process exited with code ${code}`);
  }
  grep.stdin.end();
});

grep.stdout.on('data', (data) => {
  console.log(data.toString());
});

grep.stderr.on('data', (data) => {
  console.error(`grep stderr: ${data}`);
});

grep.on('close', (code) => {
  if (code !== 0) {
    console.log(`grep process exited with code ${code}`);
  }
});
```

Example of checking for failed `spawn`:

```js
const { spawn } = require('child_process');
const subprocess = spawn('bad_command');

subprocess.on('error', (err) => {
  console.error('Failed to start subprocess.');
});
```

Certain platforms (macOS, Linux) will use the value of `argv[0]` for the process
title while others (Windows, SunOS) will use `command`.

##### Parameters

| Parameter | Type | Description |
| ------ | ------ | ------ |
| `command` | `string` | The command to run. |
| `options`? | [`SpawnOptionsWithoutStdio`](child_process.md#spawnoptionswithoutstdio) | - |

##### Returns

[`ChildProcessWithoutNullStreams`](child_process.md#childprocesswithoutnullstreams)

#### Call Signature

> **spawn**(`command`: `string`, `options`: [`SpawnOptionsWithStdioTuple`](child_process.md#spawnoptionswithstdiotuplestdin-stdout-stderr)\<[`StdioPipe`](child_process.md#stdiopipe), [`StdioPipe`](child_process.md#stdiopipe), [`StdioPipe`](child_process.md#stdiopipe)\>): [`ChildProcessByStdio`](child_process.md#childprocessbystdioi-o-e)\<[`DefaultWritableStream`](stream.md#defaultwritablestream), [`DefaultReadableStream`](stream.md#defaultreadablestream), [`DefaultReadableStream`](stream.md#defaultreadablestream)\>

The `child_process.spawn()` method spawns a new process using the given `command`, with command-line arguments in `args`.
If omitted, `args` defaults to an empty array.

**If the `shell` option is enabled, do not pass unsanitized user input to this**
**function. Any input containing shell metacharacters may be used to trigger**
**arbitrary command execution.**

A third argument may be used to specify additional options.

Use `cwd` to specify the working directory from which the process is spawned.
If not given, the default is to inherit the current working directory. If given,
but the path does not exist, the child process emits an `ENOENT` error
and exits immediately. `ENOENT` is also emitted when the command
does not exist.

Example of running `ls -lh /usr`, capturing `stdout`, `stderr`, and the
exit code:

```js
const { spawn } = require('child_process');
const ls = spawn('ls', ['-lh', '/usr']);

ls.stdout.on('data', (data) => {
  console.log(`stdout: ${data}`);
});

ls.stderr.on('data', (data) => {
  console.error(`stderr: ${data}`);
});

ls.on('close', (code) => {
  console.log(`child process exited with code ${code}`);
});
```

Example: A very elaborate way to run `ps ax | grep ssh`

```js
const { spawn } = require('child_process');
const ps = spawn('ps', ['ax']);
const grep = spawn('grep', ['ssh']);

ps.stdout.on('data', (data) => {
  grep.stdin.write(data);
});

ps.stderr.on('data', (data) => {
  console.error(`ps stderr: ${data}`);
});

ps.on('close', (code) => {
  if (code !== 0) {
    console.log(`ps process exited with code ${code}`);
  }
  grep.stdin.end();
});

grep.stdout.on('data', (data) => {
  console.log(data.toString());
});

grep.stderr.on('data', (data) => {
  console.error(`grep stderr: ${data}`);
});

grep.on('close', (code) => {
  if (code !== 0) {
    console.log(`grep process exited with code ${code}`);
  }
});
```

Example of checking for failed `spawn`:

```js
const { spawn } = require('child_process');
const subprocess = spawn('bad_command');

subprocess.on('error', (err) => {
  console.error('Failed to start subprocess.');
});
```

Certain platforms (macOS, Linux) will use the value of `argv[0]` for the process
title while others (Windows, SunOS) will use `command`.

##### Parameters

| Parameter | Type | Description |
| ------ | ------ | ------ |
| `command` | `string` | The command to run. |
| `options` | [`SpawnOptionsWithStdioTuple`](child_process.md#spawnoptionswithstdiotuplestdin-stdout-stderr)\<[`StdioPipe`](child_process.md#stdiopipe), [`StdioPipe`](child_process.md#stdiopipe), [`StdioPipe`](child_process.md#stdiopipe)\> | - |

##### Returns

[`ChildProcessByStdio`](child_process.md#childprocessbystdioi-o-e)\<[`DefaultWritableStream`](stream.md#defaultwritablestream), [`DefaultReadableStream`](stream.md#defaultreadablestream), [`DefaultReadableStream`](stream.md#defaultreadablestream)\>

#### Call Signature

> **spawn**(`command`: `string`, `options`: [`SpawnOptionsWithStdioTuple`](child_process.md#spawnoptionswithstdiotuplestdin-stdout-stderr)\<[`StdioPipe`](child_process.md#stdiopipe), [`StdioPipe`](child_process.md#stdiopipe), [`StdioNull`](child_process.md#stdionull)\>): [`ChildProcessByStdio`](child_process.md#childprocessbystdioi-o-e)\<[`DefaultWritableStream`](stream.md#defaultwritablestream), [`DefaultReadableStream`](stream.md#defaultreadablestream), `null`\>

The `child_process.spawn()` method spawns a new process using the given `command`, with command-line arguments in `args`.
If omitted, `args` defaults to an empty array.

**If the `shell` option is enabled, do not pass unsanitized user input to this**
**function. Any input containing shell metacharacters may be used to trigger**
**arbitrary command execution.**

A third argument may be used to specify additional options.

Use `cwd` to specify the working directory from which the process is spawned.
If not given, the default is to inherit the current working directory. If given,
but the path does not exist, the child process emits an `ENOENT` error
and exits immediately. `ENOENT` is also emitted when the command
does not exist.

Example of running `ls -lh /usr`, capturing `stdout`, `stderr`, and the
exit code:

```js
const { spawn } = require('child_process');
const ls = spawn('ls', ['-lh', '/usr']);

ls.stdout.on('data', (data) => {
  console.log(`stdout: ${data}`);
});

ls.stderr.on('data', (data) => {
  console.error(`stderr: ${data}`);
});

ls.on('close', (code) => {
  console.log(`child process exited with code ${code}`);
});
```

Example: A very elaborate way to run `ps ax | grep ssh`

```js
const { spawn } = require('child_process');
const ps = spawn('ps', ['ax']);
const grep = spawn('grep', ['ssh']);

ps.stdout.on('data', (data) => {
  grep.stdin.write(data);
});

ps.stderr.on('data', (data) => {
  console.error(`ps stderr: ${data}`);
});

ps.on('close', (code) => {
  if (code !== 0) {
    console.log(`ps process exited with code ${code}`);
  }
  grep.stdin.end();
});

grep.stdout.on('data', (data) => {
  console.log(data.toString());
});

grep.stderr.on('data', (data) => {
  console.error(`grep stderr: ${data}`);
});

grep.on('close', (code) => {
  if (code !== 0) {
    console.log(`grep process exited with code ${code}`);
  }
});
```

Example of checking for failed `spawn`:

```js
const { spawn } = require('child_process');
const subprocess = spawn('bad_command');

subprocess.on('error', (err) => {
  console.error('Failed to start subprocess.');
});
```

Certain platforms (macOS, Linux) will use the value of `argv[0]` for the process
title while others (Windows, SunOS) will use `command`.

##### Parameters

| Parameter | Type | Description |
| ------ | ------ | ------ |
| `command` | `string` | The command to run. |
| `options` | [`SpawnOptionsWithStdioTuple`](child_process.md#spawnoptionswithstdiotuplestdin-stdout-stderr)\<[`StdioPipe`](child_process.md#stdiopipe), [`StdioPipe`](child_process.md#stdiopipe), [`StdioNull`](child_process.md#stdionull)\> | - |

##### Returns

[`ChildProcessByStdio`](child_process.md#childprocessbystdioi-o-e)\<[`DefaultWritableStream`](stream.md#defaultwritablestream), [`DefaultReadableStream`](stream.md#defaultreadablestream), `null`\>

#### Call Signature

> **spawn**(`command`: `string`, `options`: [`SpawnOptionsWithStdioTuple`](child_process.md#spawnoptionswithstdiotuplestdin-stdout-stderr)\<[`StdioPipe`](child_process.md#stdiopipe), [`StdioNull`](child_process.md#stdionull), [`StdioPipe`](child_process.md#stdiopipe)\>): [`ChildProcessByStdio`](child_process.md#childprocessbystdioi-o-e)\<[`DefaultWritableStream`](stream.md#defaultwritablestream), `null`, [`DefaultReadableStream`](stream.md#defaultreadablestream)\>

The `child_process.spawn()` method spawns a new process using the given `command`, with command-line arguments in `args`.
If omitted, `args` defaults to an empty array.

**If the `shell` option is enabled, do not pass unsanitized user input to this**
**function. Any input containing shell metacharacters may be used to trigger**
**arbitrary command execution.**

A third argument may be used to specify additional options.

Use `cwd` to specify the working directory from which the process is spawned.
If not given, the default is to inherit the current working directory. If given,
but the path does not exist, the child process emits an `ENOENT` error
and exits immediately. `ENOENT` is also emitted when the command
does not exist.

Example of running `ls -lh /usr`, capturing `stdout`, `stderr`, and the
exit code:

```js
const { spawn } = require('child_process');
const ls = spawn('ls', ['-lh', '/usr']);

ls.stdout.on('data', (data) => {
  console.log(`stdout: ${data}`);
});

ls.stderr.on('data', (data) => {
  console.error(`stderr: ${data}`);
});

ls.on('close', (code) => {
  console.log(`child process exited with code ${code}`);
});
```

Example: A very elaborate way to run `ps ax | grep ssh`

```js
const { spawn } = require('child_process');
const ps = spawn('ps', ['ax']);
const grep = spawn('grep', ['ssh']);

ps.stdout.on('data', (data) => {
  grep.stdin.write(data);
});

ps.stderr.on('data', (data) => {
  console.error(`ps stderr: ${data}`);
});

ps.on('close', (code) => {
  if (code !== 0) {
    console.log(`ps process exited with code ${code}`);
  }
  grep.stdin.end();
});

grep.stdout.on('data', (data) => {
  console.log(data.toString());
});

grep.stderr.on('data', (data) => {
  console.error(`grep stderr: ${data}`);
});

grep.on('close', (code) => {
  if (code !== 0) {
    console.log(`grep process exited with code ${code}`);
  }
});
```

Example of checking for failed `spawn`:

```js
const { spawn } = require('child_process');
const subprocess = spawn('bad_command');

subprocess.on('error', (err) => {
  console.error('Failed to start subprocess.');
});
```

Certain platforms (macOS, Linux) will use the value of `argv[0]` for the process
title while others (Windows, SunOS) will use `command`.

##### Parameters

| Parameter | Type | Description |
| ------ | ------ | ------ |
| `command` | `string` | The command to run. |
| `options` | [`SpawnOptionsWithStdioTuple`](child_process.md#spawnoptionswithstdiotuplestdin-stdout-stderr)\<[`StdioPipe`](child_process.md#stdiopipe), [`StdioNull`](child_process.md#stdionull), [`StdioPipe`](child_process.md#stdiopipe)\> | - |

##### Returns

[`ChildProcessByStdio`](child_process.md#childprocessbystdioi-o-e)\<[`DefaultWritableStream`](stream.md#defaultwritablestream), `null`, [`DefaultReadableStream`](stream.md#defaultreadablestream)\>

#### Call Signature

> **spawn**(`command`: `string`, `options`: [`SpawnOptionsWithStdioTuple`](child_process.md#spawnoptionswithstdiotuplestdin-stdout-stderr)\<[`StdioNull`](child_process.md#stdionull), [`StdioPipe`](child_process.md#stdiopipe), [`StdioPipe`](child_process.md#stdiopipe)\>): [`ChildProcessByStdio`](child_process.md#childprocessbystdioi-o-e)\<`null`, [`DefaultReadableStream`](stream.md#defaultreadablestream), [`DefaultReadableStream`](stream.md#defaultreadablestream)\>

The `child_process.spawn()` method spawns a new process using the given `command`, with command-line arguments in `args`.
If omitted, `args` defaults to an empty array.

**If the `shell` option is enabled, do not pass unsanitized user input to this**
**function. Any input containing shell metacharacters may be used to trigger**
**arbitrary command execution.**

A third argument may be used to specify additional options.

Use `cwd` to specify the working directory from which the process is spawned.
If not given, the default is to inherit the current working directory. If given,
but the path does not exist, the child process emits an `ENOENT` error
and exits immediately. `ENOENT` is also emitted when the command
does not exist.

Example of running `ls -lh /usr`, capturing `stdout`, `stderr`, and the
exit code:

```js
const { spawn } = require('child_process');
const ls = spawn('ls', ['-lh', '/usr']);

ls.stdout.on('data', (data) => {
  console.log(`stdout: ${data}`);
});

ls.stderr.on('data', (data) => {
  console.error(`stderr: ${data}`);
});

ls.on('close', (code) => {
  console.log(`child process exited with code ${code}`);
});
```

Example: A very elaborate way to run `ps ax | grep ssh`

```js
const { spawn } = require('child_process');
const ps = spawn('ps', ['ax']);
const grep = spawn('grep', ['ssh']);

ps.stdout.on('data', (data) => {
  grep.stdin.write(data);
});

ps.stderr.on('data', (data) => {
  console.error(`ps stderr: ${data}`);
});

ps.on('close', (code) => {
  if (code !== 0) {
    console.log(`ps process exited with code ${code}`);
  }
  grep.stdin.end();
});

grep.stdout.on('data', (data) => {
  console.log(data.toString());
});

grep.stderr.on('data', (data) => {
  console.error(`grep stderr: ${data}`);
});

grep.on('close', (code) => {
  if (code !== 0) {
    console.log(`grep process exited with code ${code}`);
  }
});
```

Example of checking for failed `spawn`:

```js
const { spawn } = require('child_process');
const subprocess = spawn('bad_command');

subprocess.on('error', (err) => {
  console.error('Failed to start subprocess.');
});
```

Certain platforms (macOS, Linux) will use the value of `argv[0]` for the process
title while others (Windows, SunOS) will use `command`.

##### Parameters

| Parameter | Type | Description |
| ------ | ------ | ------ |
| `command` | `string` | The command to run. |
| `options` | [`SpawnOptionsWithStdioTuple`](child_process.md#spawnoptionswithstdiotuplestdin-stdout-stderr)\<[`StdioNull`](child_process.md#stdionull), [`StdioPipe`](child_process.md#stdiopipe), [`StdioPipe`](child_process.md#stdiopipe)\> | - |

##### Returns

[`ChildProcessByStdio`](child_process.md#childprocessbystdioi-o-e)\<`null`, [`DefaultReadableStream`](stream.md#defaultreadablestream), [`DefaultReadableStream`](stream.md#defaultreadablestream)\>

#### Call Signature

> **spawn**(`command`: `string`, `options`: [`SpawnOptionsWithStdioTuple`](child_process.md#spawnoptionswithstdiotuplestdin-stdout-stderr)\<[`StdioPipe`](child_process.md#stdiopipe), [`StdioNull`](child_process.md#stdionull), [`StdioNull`](child_process.md#stdionull)\>): [`ChildProcessByStdio`](child_process.md#childprocessbystdioi-o-e)\<[`DefaultWritableStream`](stream.md#defaultwritablestream), `null`, `null`\>

The `child_process.spawn()` method spawns a new process using the given `command`, with command-line arguments in `args`.
If omitted, `args` defaults to an empty array.

**If the `shell` option is enabled, do not pass unsanitized user input to this**
**function. Any input containing shell metacharacters may be used to trigger**
**arbitrary command execution.**

A third argument may be used to specify additional options.

Use `cwd` to specify the working directory from which the process is spawned.
If not given, the default is to inherit the current working directory. If given,
but the path does not exist, the child process emits an `ENOENT` error
and exits immediately. `ENOENT` is also emitted when the command
does not exist.

Example of running `ls -lh /usr`, capturing `stdout`, `stderr`, and the
exit code:

```js
const { spawn } = require('child_process');
const ls = spawn('ls', ['-lh', '/usr']);

ls.stdout.on('data', (data) => {
  console.log(`stdout: ${data}`);
});

ls.stderr.on('data', (data) => {
  console.error(`stderr: ${data}`);
});

ls.on('close', (code) => {
  console.log(`child process exited with code ${code}`);
});
```

Example: A very elaborate way to run `ps ax | grep ssh`

```js
const { spawn } = require('child_process');
const ps = spawn('ps', ['ax']);
const grep = spawn('grep', ['ssh']);

ps.stdout.on('data', (data) => {
  grep.stdin.write(data);
});

ps.stderr.on('data', (data) => {
  console.error(`ps stderr: ${data}`);
});

ps.on('close', (code) => {
  if (code !== 0) {
    console.log(`ps process exited with code ${code}`);
  }
  grep.stdin.end();
});

grep.stdout.on('data', (data) => {
  console.log(data.toString());
});

grep.stderr.on('data', (data) => {
  console.error(`grep stderr: ${data}`);
});

grep.on('close', (code) => {
  if (code !== 0) {
    console.log(`grep process exited with code ${code}`);
  }
});
```

Example of checking for failed `spawn`:

```js
const { spawn } = require('child_process');
const subprocess = spawn('bad_command');

subprocess.on('error', (err) => {
  console.error('Failed to start subprocess.');
});
```

Certain platforms (macOS, Linux) will use the value of `argv[0]` for the process
title while others (Windows, SunOS) will use `command`.

##### Parameters

| Parameter | Type | Description |
| ------ | ------ | ------ |
| `command` | `string` | The command to run. |
| `options` | [`SpawnOptionsWithStdioTuple`](child_process.md#spawnoptionswithstdiotuplestdin-stdout-stderr)\<[`StdioPipe`](child_process.md#stdiopipe), [`StdioNull`](child_process.md#stdionull), [`StdioNull`](child_process.md#stdionull)\> | - |

##### Returns

[`ChildProcessByStdio`](child_process.md#childprocessbystdioi-o-e)\<[`DefaultWritableStream`](stream.md#defaultwritablestream), `null`, `null`\>

#### Call Signature

> **spawn**(`command`: `string`, `options`: [`SpawnOptionsWithStdioTuple`](child_process.md#spawnoptionswithstdiotuplestdin-stdout-stderr)\<[`StdioNull`](child_process.md#stdionull), [`StdioPipe`](child_process.md#stdiopipe), [`StdioNull`](child_process.md#stdionull)\>): [`ChildProcessByStdio`](child_process.md#childprocessbystdioi-o-e)\<`null`, [`DefaultReadableStream`](stream.md#defaultreadablestream), `null`\>

The `child_process.spawn()` method spawns a new process using the given `command`, with command-line arguments in `args`.
If omitted, `args` defaults to an empty array.

**If the `shell` option is enabled, do not pass unsanitized user input to this**
**function. Any input containing shell metacharacters may be used to trigger**
**arbitrary command execution.**

A third argument may be used to specify additional options.

Use `cwd` to specify the working directory from which the process is spawned.
If not given, the default is to inherit the current working directory. If given,
but the path does not exist, the child process emits an `ENOENT` error
and exits immediately. `ENOENT` is also emitted when the command
does not exist.

Example of running `ls -lh /usr`, capturing `stdout`, `stderr`, and the
exit code:

```js
const { spawn } = require('child_process');
const ls = spawn('ls', ['-lh', '/usr']);

ls.stdout.on('data', (data) => {
  console.log(`stdout: ${data}`);
});

ls.stderr.on('data', (data) => {
  console.error(`stderr: ${data}`);
});

ls.on('close', (code) => {
  console.log(`child process exited with code ${code}`);
});
```

Example: A very elaborate way to run `ps ax | grep ssh`

```js
const { spawn } = require('child_process');
const ps = spawn('ps', ['ax']);
const grep = spawn('grep', ['ssh']);

ps.stdout.on('data', (data) => {
  grep.stdin.write(data);
});

ps.stderr.on('data', (data) => {
  console.error(`ps stderr: ${data}`);
});

ps.on('close', (code) => {
  if (code !== 0) {
    console.log(`ps process exited with code ${code}`);
  }
  grep.stdin.end();
});

grep.stdout.on('data', (data) => {
  console.log(data.toString());
});

grep.stderr.on('data', (data) => {
  console.error(`grep stderr: ${data}`);
});

grep.on('close', (code) => {
  if (code !== 0) {
    console.log(`grep process exited with code ${code}`);
  }
});
```

Example of checking for failed `spawn`:

```js
const { spawn } = require('child_process');
const subprocess = spawn('bad_command');

subprocess.on('error', (err) => {
  console.error('Failed to start subprocess.');
});
```

Certain platforms (macOS, Linux) will use the value of `argv[0]` for the process
title while others (Windows, SunOS) will use `command`.

##### Parameters

| Parameter | Type | Description |
| ------ | ------ | ------ |
| `command` | `string` | The command to run. |
| `options` | [`SpawnOptionsWithStdioTuple`](child_process.md#spawnoptionswithstdiotuplestdin-stdout-stderr)\<[`StdioNull`](child_process.md#stdionull), [`StdioPipe`](child_process.md#stdiopipe), [`StdioNull`](child_process.md#stdionull)\> | - |

##### Returns

[`ChildProcessByStdio`](child_process.md#childprocessbystdioi-o-e)\<`null`, [`DefaultReadableStream`](stream.md#defaultreadablestream), `null`\>

#### Call Signature

> **spawn**(`command`: `string`, `options`: [`SpawnOptionsWithStdioTuple`](child_process.md#spawnoptionswithstdiotuplestdin-stdout-stderr)\<[`StdioNull`](child_process.md#stdionull), [`StdioNull`](child_process.md#stdionull), [`StdioPipe`](child_process.md#stdiopipe)\>): [`ChildProcessByStdio`](child_process.md#childprocessbystdioi-o-e)\<`null`, `null`, [`DefaultReadableStream`](stream.md#defaultreadablestream)\>

The `child_process.spawn()` method spawns a new process using the given `command`, with command-line arguments in `args`.
If omitted, `args` defaults to an empty array.

**If the `shell` option is enabled, do not pass unsanitized user input to this**
**function. Any input containing shell metacharacters may be used to trigger**
**arbitrary command execution.**

A third argument may be used to specify additional options.

Use `cwd` to specify the working directory from which the process is spawned.
If not given, the default is to inherit the current working directory. If given,
but the path does not exist, the child process emits an `ENOENT` error
and exits immediately. `ENOENT` is also emitted when the command
does not exist.

Example of running `ls -lh /usr`, capturing `stdout`, `stderr`, and the
exit code:

```js
const { spawn } = require('child_process');
const ls = spawn('ls', ['-lh', '/usr']);

ls.stdout.on('data', (data) => {
  console.log(`stdout: ${data}`);
});

ls.stderr.on('data', (data) => {
  console.error(`stderr: ${data}`);
});

ls.on('close', (code) => {
  console.log(`child process exited with code ${code}`);
});
```

Example: A very elaborate way to run `ps ax | grep ssh`

```js
const { spawn } = require('child_process');
const ps = spawn('ps', ['ax']);
const grep = spawn('grep', ['ssh']);

ps.stdout.on('data', (data) => {
  grep.stdin.write(data);
});

ps.stderr.on('data', (data) => {
  console.error(`ps stderr: ${data}`);
});

ps.on('close', (code) => {
  if (code !== 0) {
    console.log(`ps process exited with code ${code}`);
  }
  grep.stdin.end();
});

grep.stdout.on('data', (data) => {
  console.log(data.toString());
});

grep.stderr.on('data', (data) => {
  console.error(`grep stderr: ${data}`);
});

grep.on('close', (code) => {
  if (code !== 0) {
    console.log(`grep process exited with code ${code}`);
  }
});
```

Example of checking for failed `spawn`:

```js
const { spawn } = require('child_process');
const subprocess = spawn('bad_command');

subprocess.on('error', (err) => {
  console.error('Failed to start subprocess.');
});
```

Certain platforms (macOS, Linux) will use the value of `argv[0]` for the process
title while others (Windows, SunOS) will use `command`.

##### Parameters

| Parameter | Type | Description |
| ------ | ------ | ------ |
| `command` | `string` | The command to run. |
| `options` | [`SpawnOptionsWithStdioTuple`](child_process.md#spawnoptionswithstdiotuplestdin-stdout-stderr)\<[`StdioNull`](child_process.md#stdionull), [`StdioNull`](child_process.md#stdionull), [`StdioPipe`](child_process.md#stdiopipe)\> | - |

##### Returns

[`ChildProcessByStdio`](child_process.md#childprocessbystdioi-o-e)\<`null`, `null`, [`DefaultReadableStream`](stream.md#defaultreadablestream)\>

#### Call Signature

> **spawn**(`command`: `string`, `options`: [`SpawnOptionsWithStdioTuple`](child_process.md#spawnoptionswithstdiotuplestdin-stdout-stderr)\<[`StdioNull`](child_process.md#stdionull), [`StdioNull`](child_process.md#stdionull), [`StdioNull`](child_process.md#stdionull)\>): [`ChildProcessByStdio`](child_process.md#childprocessbystdioi-o-e)\<`null`, `null`, `null`\>

The `child_process.spawn()` method spawns a new process using the given `command`, with command-line arguments in `args`.
If omitted, `args` defaults to an empty array.

**If the `shell` option is enabled, do not pass unsanitized user input to this**
**function. Any input containing shell metacharacters may be used to trigger**
**arbitrary command execution.**

A third argument may be used to specify additional options.

Use `cwd` to specify the working directory from which the process is spawned.
If not given, the default is to inherit the current working directory. If given,
but the path does not exist, the child process emits an `ENOENT` error
and exits immediately. `ENOENT` is also emitted when the command
does not exist.

Example of running `ls -lh /usr`, capturing `stdout`, `stderr`, and the
exit code:

```js
const { spawn } = require('child_process');
const ls = spawn('ls', ['-lh', '/usr']);

ls.stdout.on('data', (data) => {
  console.log(`stdout: ${data}`);
});

ls.stderr.on('data', (data) => {
  console.error(`stderr: ${data}`);
});

ls.on('close', (code) => {
  console.log(`child process exited with code ${code}`);
});
```

Example: A very elaborate way to run `ps ax | grep ssh`

```js
const { spawn } = require('child_process');
const ps = spawn('ps', ['ax']);
const grep = spawn('grep', ['ssh']);

ps.stdout.on('data', (data) => {
  grep.stdin.write(data);
});

ps.stderr.on('data', (data) => {
  console.error(`ps stderr: ${data}`);
});

ps.on('close', (code) => {
  if (code !== 0) {
    console.log(`ps process exited with code ${code}`);
  }
  grep.stdin.end();
});

grep.stdout.on('data', (data) => {
  console.log(data.toString());
});

grep.stderr.on('data', (data) => {
  console.error(`grep stderr: ${data}`);
});

grep.on('close', (code) => {
  if (code !== 0) {
    console.log(`grep process exited with code ${code}`);
  }
});
```

Example of checking for failed `spawn`:

```js
const { spawn } = require('child_process');
const subprocess = spawn('bad_command');

subprocess.on('error', (err) => {
  console.error('Failed to start subprocess.');
});
```

Certain platforms (macOS, Linux) will use the value of `argv[0]` for the process
title while others (Windows, SunOS) will use `command`.

##### Parameters

| Parameter | Type | Description |
| ------ | ------ | ------ |
| `command` | `string` | The command to run. |
| `options` | [`SpawnOptionsWithStdioTuple`](child_process.md#spawnoptionswithstdiotuplestdin-stdout-stderr)\<[`StdioNull`](child_process.md#stdionull), [`StdioNull`](child_process.md#stdionull), [`StdioNull`](child_process.md#stdionull)\> | - |

##### Returns

[`ChildProcessByStdio`](child_process.md#childprocessbystdioi-o-e)\<`null`, `null`, `null`\>

#### Call Signature

> **spawn**(`command`: `string`, `options`: [`SpawnOptions`](child_process.md#spawnoptions)): [`ChildProcess`](child_process.md#childprocess)

The `child_process.spawn()` method spawns a new process using the given `command`, with command-line arguments in `args`.
If omitted, `args` defaults to an empty array.

**If the `shell` option is enabled, do not pass unsanitized user input to this**
**function. Any input containing shell metacharacters may be used to trigger**
**arbitrary command execution.**

A third argument may be used to specify additional options.

Use `cwd` to specify the working directory from which the process is spawned.
If not given, the default is to inherit the current working directory. If given,
but the path does not exist, the child process emits an `ENOENT` error
and exits immediately. `ENOENT` is also emitted when the command
does not exist.

Example of running `ls -lh /usr`, capturing `stdout`, `stderr`, and the
exit code:

```js
const { spawn } = require('child_process');
const ls = spawn('ls', ['-lh', '/usr']);

ls.stdout.on('data', (data) => {
  console.log(`stdout: ${data}`);
});

ls.stderr.on('data', (data) => {
  console.error(`stderr: ${data}`);
});

ls.on('close', (code) => {
  console.log(`child process exited with code ${code}`);
});
```

Example: A very elaborate way to run `ps ax | grep ssh`

```js
const { spawn } = require('child_process');
const ps = spawn('ps', ['ax']);
const grep = spawn('grep', ['ssh']);

ps.stdout.on('data', (data) => {
  grep.stdin.write(data);
});

ps.stderr.on('data', (data) => {
  console.error(`ps stderr: ${data}`);
});

ps.on('close', (code) => {
  if (code !== 0) {
    console.log(`ps process exited with code ${code}`);
  }
  grep.stdin.end();
});

grep.stdout.on('data', (data) => {
  console.log(data.toString());
});

grep.stderr.on('data', (data) => {
  console.error(`grep stderr: ${data}`);
});

grep.on('close', (code) => {
  if (code !== 0) {
    console.log(`grep process exited with code ${code}`);
  }
});
```

Example of checking for failed `spawn`:

```js
const { spawn } = require('child_process');
const subprocess = spawn('bad_command');

subprocess.on('error', (err) => {
  console.error('Failed to start subprocess.');
});
```

Certain platforms (macOS, Linux) will use the value of `argv[0]` for the process
title while others (Windows, SunOS) will use `command`.

##### Parameters

| Parameter | Type | Description |
| ------ | ------ | ------ |
| `command` | `string` | The command to run. |
| `options` | [`SpawnOptions`](child_process.md#spawnoptions) | - |

##### Returns

[`ChildProcess`](child_process.md#childprocess)

#### Call Signature

> **spawn**(`command`: `string`, `args`?: readonly `string`[], `options`?: [`SpawnOptionsWithoutStdio`](child_process.md#spawnoptionswithoutstdio)): [`ChildProcessWithoutNullStreams`](child_process.md#childprocesswithoutnullstreams)

The `child_process.spawn()` method spawns a new process using the given `command`, with command-line arguments in `args`.
If omitted, `args` defaults to an empty array.

**If the `shell` option is enabled, do not pass unsanitized user input to this**
**function. Any input containing shell metacharacters may be used to trigger**
**arbitrary command execution.**

A third argument may be used to specify additional options.

Use `cwd` to specify the working directory from which the process is spawned.
If not given, the default is to inherit the current working directory. If given,
but the path does not exist, the child process emits an `ENOENT` error
and exits immediately. `ENOENT` is also emitted when the command
does not exist.

Example of running `ls -lh /usr`, capturing `stdout`, `stderr`, and the
exit code:

```js
const { spawn } = require('child_process');
const ls = spawn('ls', ['-lh', '/usr']);

ls.stdout.on('data', (data) => {
  console.log(`stdout: ${data}`);
});

ls.stderr.on('data', (data) => {
  console.error(`stderr: ${data}`);
});

ls.on('close', (code) => {
  console.log(`child process exited with code ${code}`);
});
```

Example: A very elaborate way to run `ps ax | grep ssh`

```js
const { spawn } = require('child_process');
const ps = spawn('ps', ['ax']);
const grep = spawn('grep', ['ssh']);

ps.stdout.on('data', (data) => {
  grep.stdin.write(data);
});

ps.stderr.on('data', (data) => {
  console.error(`ps stderr: ${data}`);
});

ps.on('close', (code) => {
  if (code !== 0) {
    console.log(`ps process exited with code ${code}`);
  }
  grep.stdin.end();
});

grep.stdout.on('data', (data) => {
  console.log(data.toString());
});

grep.stderr.on('data', (data) => {
  console.error(`grep stderr: ${data}`);
});

grep.on('close', (code) => {
  if (code !== 0) {
    console.log(`grep process exited with code ${code}`);
  }
});
```

Example of checking for failed `spawn`:

```js
const { spawn } = require('child_process');
const subprocess = spawn('bad_command');

subprocess.on('error', (err) => {
  console.error('Failed to start subprocess.');
});
```

Certain platforms (macOS, Linux) will use the value of `argv[0]` for the process
title while others (Windows, SunOS) will use `command`.

##### Parameters

| Parameter | Type | Description |
| ------ | ------ | ------ |
| `command` | `string` | The command to run. |
| `args`? | readonly `string`[] | List of string arguments. |
| `options`? | [`SpawnOptionsWithoutStdio`](child_process.md#spawnoptionswithoutstdio) | - |

##### Returns

[`ChildProcessWithoutNullStreams`](child_process.md#childprocesswithoutnullstreams)

#### Call Signature

> **spawn**(`command`: `string`, `args`: readonly `string`[], `options`: [`SpawnOptionsWithStdioTuple`](child_process.md#spawnoptionswithstdiotuplestdin-stdout-stderr)\<[`StdioPipe`](child_process.md#stdiopipe), [`StdioPipe`](child_process.md#stdiopipe), [`StdioPipe`](child_process.md#stdiopipe)\>): [`ChildProcessByStdio`](child_process.md#childprocessbystdioi-o-e)\<[`DefaultWritableStream`](stream.md#defaultwritablestream), [`DefaultReadableStream`](stream.md#defaultreadablestream), [`DefaultReadableStream`](stream.md#defaultreadablestream)\>

The `child_process.spawn()` method spawns a new process using the given `command`, with command-line arguments in `args`.
If omitted, `args` defaults to an empty array.

**If the `shell` option is enabled, do not pass unsanitized user input to this**
**function. Any input containing shell metacharacters may be used to trigger**
**arbitrary command execution.**

A third argument may be used to specify additional options.

Use `cwd` to specify the working directory from which the process is spawned.
If not given, the default is to inherit the current working directory. If given,
but the path does not exist, the child process emits an `ENOENT` error
and exits immediately. `ENOENT` is also emitted when the command
does not exist.

Example of running `ls -lh /usr`, capturing `stdout`, `stderr`, and the
exit code:

```js
const { spawn } = require('child_process');
const ls = spawn('ls', ['-lh', '/usr']);

ls.stdout.on('data', (data) => {
  console.log(`stdout: ${data}`);
});

ls.stderr.on('data', (data) => {
  console.error(`stderr: ${data}`);
});

ls.on('close', (code) => {
  console.log(`child process exited with code ${code}`);
});
```

Example: A very elaborate way to run `ps ax | grep ssh`

```js
const { spawn } = require('child_process');
const ps = spawn('ps', ['ax']);
const grep = spawn('grep', ['ssh']);

ps.stdout.on('data', (data) => {
  grep.stdin.write(data);
});

ps.stderr.on('data', (data) => {
  console.error(`ps stderr: ${data}`);
});

ps.on('close', (code) => {
  if (code !== 0) {
    console.log(`ps process exited with code ${code}`);
  }
  grep.stdin.end();
});

grep.stdout.on('data', (data) => {
  console.log(data.toString());
});

grep.stderr.on('data', (data) => {
  console.error(`grep stderr: ${data}`);
});

grep.on('close', (code) => {
  if (code !== 0) {
    console.log(`grep process exited with code ${code}`);
  }
});
```

Example of checking for failed `spawn`:

```js
const { spawn } = require('child_process');
const subprocess = spawn('bad_command');

subprocess.on('error', (err) => {
  console.error('Failed to start subprocess.');
});
```

Certain platforms (macOS, Linux) will use the value of `argv[0]` for the process
title while others (Windows, SunOS) will use `command`.

##### Parameters

| Parameter | Type | Description |
| ------ | ------ | ------ |
| `command` | `string` | The command to run. |
| `args` | readonly `string`[] | List of string arguments. |
| `options` | [`SpawnOptionsWithStdioTuple`](child_process.md#spawnoptionswithstdiotuplestdin-stdout-stderr)\<[`StdioPipe`](child_process.md#stdiopipe), [`StdioPipe`](child_process.md#stdiopipe), [`StdioPipe`](child_process.md#stdiopipe)\> | - |

##### Returns

[`ChildProcessByStdio`](child_process.md#childprocessbystdioi-o-e)\<[`DefaultWritableStream`](stream.md#defaultwritablestream), [`DefaultReadableStream`](stream.md#defaultreadablestream), [`DefaultReadableStream`](stream.md#defaultreadablestream)\>

#### Call Signature

> **spawn**(`command`: `string`, `args`: readonly `string`[], `options`: [`SpawnOptionsWithStdioTuple`](child_process.md#spawnoptionswithstdiotuplestdin-stdout-stderr)\<[`StdioPipe`](child_process.md#stdiopipe), [`StdioPipe`](child_process.md#stdiopipe), [`StdioNull`](child_process.md#stdionull)\>): [`ChildProcessByStdio`](child_process.md#childprocessbystdioi-o-e)\<[`DefaultWritableStream`](stream.md#defaultwritablestream), [`DefaultReadableStream`](stream.md#defaultreadablestream), `null`\>

The `child_process.spawn()` method spawns a new process using the given `command`, with command-line arguments in `args`.
If omitted, `args` defaults to an empty array.

**If the `shell` option is enabled, do not pass unsanitized user input to this**
**function. Any input containing shell metacharacters may be used to trigger**
**arbitrary command execution.**

A third argument may be used to specify additional options.

Use `cwd` to specify the working directory from which the process is spawned.
If not given, the default is to inherit the current working directory. If given,
but the path does not exist, the child process emits an `ENOENT` error
and exits immediately. `ENOENT` is also emitted when the command
does not exist.

Example of running `ls -lh /usr`, capturing `stdout`, `stderr`, and the
exit code:

```js
const { spawn } = require('child_process');
const ls = spawn('ls', ['-lh', '/usr']);

ls.stdout.on('data', (data) => {
  console.log(`stdout: ${data}`);
});

ls.stderr.on('data', (data) => {
  console.error(`stderr: ${data}`);
});

ls.on('close', (code) => {
  console.log(`child process exited with code ${code}`);
});
```

Example: A very elaborate way to run `ps ax | grep ssh`

```js
const { spawn } = require('child_process');
const ps = spawn('ps', ['ax']);
const grep = spawn('grep', ['ssh']);

ps.stdout.on('data', (data) => {
  grep.stdin.write(data);
});

ps.stderr.on('data', (data) => {
  console.error(`ps stderr: ${data}`);
});

ps.on('close', (code) => {
  if (code !== 0) {
    console.log(`ps process exited with code ${code}`);
  }
  grep.stdin.end();
});

grep.stdout.on('data', (data) => {
  console.log(data.toString());
});

grep.stderr.on('data', (data) => {
  console.error(`grep stderr: ${data}`);
});

grep.on('close', (code) => {
  if (code !== 0) {
    console.log(`grep process exited with code ${code}`);
  }
});
```

Example of checking for failed `spawn`:

```js
const { spawn } = require('child_process');
const subprocess = spawn('bad_command');

subprocess.on('error', (err) => {
  console.error('Failed to start subprocess.');
});
```

Certain platforms (macOS, Linux) will use the value of `argv[0]` for the process
title while others (Windows, SunOS) will use `command`.

##### Parameters

| Parameter | Type | Description |
| ------ | ------ | ------ |
| `command` | `string` | The command to run. |
| `args` | readonly `string`[] | List of string arguments. |
| `options` | [`SpawnOptionsWithStdioTuple`](child_process.md#spawnoptionswithstdiotuplestdin-stdout-stderr)\<[`StdioPipe`](child_process.md#stdiopipe), [`StdioPipe`](child_process.md#stdiopipe), [`StdioNull`](child_process.md#stdionull)\> | - |

##### Returns

[`ChildProcessByStdio`](child_process.md#childprocessbystdioi-o-e)\<[`DefaultWritableStream`](stream.md#defaultwritablestream), [`DefaultReadableStream`](stream.md#defaultreadablestream), `null`\>

#### Call Signature

> **spawn**(`command`: `string`, `args`: readonly `string`[], `options`: [`SpawnOptionsWithStdioTuple`](child_process.md#spawnoptionswithstdiotuplestdin-stdout-stderr)\<[`StdioPipe`](child_process.md#stdiopipe), [`StdioNull`](child_process.md#stdionull), [`StdioPipe`](child_process.md#stdiopipe)\>): [`ChildProcessByStdio`](child_process.md#childprocessbystdioi-o-e)\<[`DefaultWritableStream`](stream.md#defaultwritablestream), `null`, [`DefaultReadableStream`](stream.md#defaultreadablestream)\>

The `child_process.spawn()` method spawns a new process using the given `command`, with command-line arguments in `args`.
If omitted, `args` defaults to an empty array.

**If the `shell` option is enabled, do not pass unsanitized user input to this**
**function. Any input containing shell metacharacters may be used to trigger**
**arbitrary command execution.**

A third argument may be used to specify additional options.

Use `cwd` to specify the working directory from which the process is spawned.
If not given, the default is to inherit the current working directory. If given,
but the path does not exist, the child process emits an `ENOENT` error
and exits immediately. `ENOENT` is also emitted when the command
does not exist.

Example of running `ls -lh /usr`, capturing `stdout`, `stderr`, and the
exit code:

```js
const { spawn } = require('child_process');
const ls = spawn('ls', ['-lh', '/usr']);

ls.stdout.on('data', (data) => {
  console.log(`stdout: ${data}`);
});

ls.stderr.on('data', (data) => {
  console.error(`stderr: ${data}`);
});

ls.on('close', (code) => {
  console.log(`child process exited with code ${code}`);
});
```

Example: A very elaborate way to run `ps ax | grep ssh`

```js
const { spawn } = require('child_process');
const ps = spawn('ps', ['ax']);
const grep = spawn('grep', ['ssh']);

ps.stdout.on('data', (data) => {
  grep.stdin.write(data);
});

ps.stderr.on('data', (data) => {
  console.error(`ps stderr: ${data}`);
});

ps.on('close', (code) => {
  if (code !== 0) {
    console.log(`ps process exited with code ${code}`);
  }
  grep.stdin.end();
});

grep.stdout.on('data', (data) => {
  console.log(data.toString());
});

grep.stderr.on('data', (data) => {
  console.error(`grep stderr: ${data}`);
});

grep.on('close', (code) => {
  if (code !== 0) {
    console.log(`grep process exited with code ${code}`);
  }
});
```

Example of checking for failed `spawn`:

```js
const { spawn } = require('child_process');
const subprocess = spawn('bad_command');

subprocess.on('error', (err) => {
  console.error('Failed to start subprocess.');
});
```

Certain platforms (macOS, Linux) will use the value of `argv[0]` for the process
title while others (Windows, SunOS) will use `command`.

##### Parameters

| Parameter | Type | Description |
| ------ | ------ | ------ |
| `command` | `string` | The command to run. |
| `args` | readonly `string`[] | List of string arguments. |
| `options` | [`SpawnOptionsWithStdioTuple`](child_process.md#spawnoptionswithstdiotuplestdin-stdout-stderr)\<[`StdioPipe`](child_process.md#stdiopipe), [`StdioNull`](child_process.md#stdionull), [`StdioPipe`](child_process.md#stdiopipe)\> | - |

##### Returns

[`ChildProcessByStdio`](child_process.md#childprocessbystdioi-o-e)\<[`DefaultWritableStream`](stream.md#defaultwritablestream), `null`, [`DefaultReadableStream`](stream.md#defaultreadablestream)\>

#### Call Signature

> **spawn**(`command`: `string`, `args`: readonly `string`[], `options`: [`SpawnOptionsWithStdioTuple`](child_process.md#spawnoptionswithstdiotuplestdin-stdout-stderr)\<[`StdioNull`](child_process.md#stdionull), [`StdioPipe`](child_process.md#stdiopipe), [`StdioPipe`](child_process.md#stdiopipe)\>): [`ChildProcessByStdio`](child_process.md#childprocessbystdioi-o-e)\<`null`, [`DefaultReadableStream`](stream.md#defaultreadablestream), [`DefaultReadableStream`](stream.md#defaultreadablestream)\>

The `child_process.spawn()` method spawns a new process using the given `command`, with command-line arguments in `args`.
If omitted, `args` defaults to an empty array.

**If the `shell` option is enabled, do not pass unsanitized user input to this**
**function. Any input containing shell metacharacters may be used to trigger**
**arbitrary command execution.**

A third argument may be used to specify additional options.

Use `cwd` to specify the working directory from which the process is spawned.
If not given, the default is to inherit the current working directory. If given,
but the path does not exist, the child process emits an `ENOENT` error
and exits immediately. `ENOENT` is also emitted when the command
does not exist.

Example of running `ls -lh /usr`, capturing `stdout`, `stderr`, and the
exit code:

```js
const { spawn } = require('child_process');
const ls = spawn('ls', ['-lh', '/usr']);

ls.stdout.on('data', (data) => {
  console.log(`stdout: ${data}`);
});

ls.stderr.on('data', (data) => {
  console.error(`stderr: ${data}`);
});

ls.on('close', (code) => {
  console.log(`child process exited with code ${code}`);
});
```

Example: A very elaborate way to run `ps ax | grep ssh`

```js
const { spawn } = require('child_process');
const ps = spawn('ps', ['ax']);
const grep = spawn('grep', ['ssh']);

ps.stdout.on('data', (data) => {
  grep.stdin.write(data);
});

ps.stderr.on('data', (data) => {
  console.error(`ps stderr: ${data}`);
});

ps.on('close', (code) => {
  if (code !== 0) {
    console.log(`ps process exited with code ${code}`);
  }
  grep.stdin.end();
});

grep.stdout.on('data', (data) => {
  console.log(data.toString());
});

grep.stderr.on('data', (data) => {
  console.error(`grep stderr: ${data}`);
});

grep.on('close', (code) => {
  if (code !== 0) {
    console.log(`grep process exited with code ${code}`);
  }
});
```

Example of checking for failed `spawn`:

```js
const { spawn } = require('child_process');
const subprocess = spawn('bad_command');

subprocess.on('error', (err) => {
  console.error('Failed to start subprocess.');
});
```

Certain platforms (macOS, Linux) will use the value of `argv[0]` for the process
title while others (Windows, SunOS) will use `command`.

##### Parameters

| Parameter | Type | Description |
| ------ | ------ | ------ |
| `command` | `string` | The command to run. |
| `args` | readonly `string`[] | List of string arguments. |
| `options` | [`SpawnOptionsWithStdioTuple`](child_process.md#spawnoptionswithstdiotuplestdin-stdout-stderr)\<[`StdioNull`](child_process.md#stdionull), [`StdioPipe`](child_process.md#stdiopipe), [`StdioPipe`](child_process.md#stdiopipe)\> | - |

##### Returns

[`ChildProcessByStdio`](child_process.md#childprocessbystdioi-o-e)\<`null`, [`DefaultReadableStream`](stream.md#defaultreadablestream), [`DefaultReadableStream`](stream.md#defaultreadablestream)\>

#### Call Signature

> **spawn**(`command`: `string`, `args`: readonly `string`[], `options`: [`SpawnOptionsWithStdioTuple`](child_process.md#spawnoptionswithstdiotuplestdin-stdout-stderr)\<[`StdioPipe`](child_process.md#stdiopipe), [`StdioNull`](child_process.md#stdionull), [`StdioNull`](child_process.md#stdionull)\>): [`ChildProcessByStdio`](child_process.md#childprocessbystdioi-o-e)\<[`DefaultWritableStream`](stream.md#defaultwritablestream), `null`, `null`\>

The `child_process.spawn()` method spawns a new process using the given `command`, with command-line arguments in `args`.
If omitted, `args` defaults to an empty array.

**If the `shell` option is enabled, do not pass unsanitized user input to this**
**function. Any input containing shell metacharacters may be used to trigger**
**arbitrary command execution.**

A third argument may be used to specify additional options.

Use `cwd` to specify the working directory from which the process is spawned.
If not given, the default is to inherit the current working directory. If given,
but the path does not exist, the child process emits an `ENOENT` error
and exits immediately. `ENOENT` is also emitted when the command
does not exist.

Example of running `ls -lh /usr`, capturing `stdout`, `stderr`, and the
exit code:

```js
const { spawn } = require('child_process');
const ls = spawn('ls', ['-lh', '/usr']);

ls.stdout.on('data', (data) => {
  console.log(`stdout: ${data}`);
});

ls.stderr.on('data', (data) => {
  console.error(`stderr: ${data}`);
});

ls.on('close', (code) => {
  console.log(`child process exited with code ${code}`);
});
```

Example: A very elaborate way to run `ps ax | grep ssh`

```js
const { spawn } = require('child_process');
const ps = spawn('ps', ['ax']);
const grep = spawn('grep', ['ssh']);

ps.stdout.on('data', (data) => {
  grep.stdin.write(data);
});

ps.stderr.on('data', (data) => {
  console.error(`ps stderr: ${data}`);
});

ps.on('close', (code) => {
  if (code !== 0) {
    console.log(`ps process exited with code ${code}`);
  }
  grep.stdin.end();
});

grep.stdout.on('data', (data) => {
  console.log(data.toString());
});

grep.stderr.on('data', (data) => {
  console.error(`grep stderr: ${data}`);
});

grep.on('close', (code) => {
  if (code !== 0) {
    console.log(`grep process exited with code ${code}`);
  }
});
```

Example of checking for failed `spawn`:

```js
const { spawn } = require('child_process');
const subprocess = spawn('bad_command');

subprocess.on('error', (err) => {
  console.error('Failed to start subprocess.');
});
```

Certain platforms (macOS, Linux) will use the value of `argv[0]` for the process
title while others (Windows, SunOS) will use `command`.

##### Parameters

| Parameter | Type | Description |
| ------ | ------ | ------ |
| `command` | `string` | The command to run. |
| `args` | readonly `string`[] | List of string arguments. |
| `options` | [`SpawnOptionsWithStdioTuple`](child_process.md#spawnoptionswithstdiotuplestdin-stdout-stderr)\<[`StdioPipe`](child_process.md#stdiopipe), [`StdioNull`](child_process.md#stdionull), [`StdioNull`](child_process.md#stdionull)\> | - |

##### Returns

[`ChildProcessByStdio`](child_process.md#childprocessbystdioi-o-e)\<[`DefaultWritableStream`](stream.md#defaultwritablestream), `null`, `null`\>

#### Call Signature

> **spawn**(`command`: `string`, `args`: readonly `string`[], `options`: [`SpawnOptionsWithStdioTuple`](child_process.md#spawnoptionswithstdiotuplestdin-stdout-stderr)\<[`StdioNull`](child_process.md#stdionull), [`StdioPipe`](child_process.md#stdiopipe), [`StdioNull`](child_process.md#stdionull)\>): [`ChildProcessByStdio`](child_process.md#childprocessbystdioi-o-e)\<`null`, [`DefaultReadableStream`](stream.md#defaultreadablestream), `null`\>

The `child_process.spawn()` method spawns a new process using the given `command`, with command-line arguments in `args`.
If omitted, `args` defaults to an empty array.

**If the `shell` option is enabled, do not pass unsanitized user input to this**
**function. Any input containing shell metacharacters may be used to trigger**
**arbitrary command execution.**

A third argument may be used to specify additional options.

Use `cwd` to specify the working directory from which the process is spawned.
If not given, the default is to inherit the current working directory. If given,
but the path does not exist, the child process emits an `ENOENT` error
and exits immediately. `ENOENT` is also emitted when the command
does not exist.

Example of running `ls -lh /usr`, capturing `stdout`, `stderr`, and the
exit code:

```js
const { spawn } = require('child_process');
const ls = spawn('ls', ['-lh', '/usr']);

ls.stdout.on('data', (data) => {
  console.log(`stdout: ${data}`);
});

ls.stderr.on('data', (data) => {
  console.error(`stderr: ${data}`);
});

ls.on('close', (code) => {
  console.log(`child process exited with code ${code}`);
});
```

Example: A very elaborate way to run `ps ax | grep ssh`

```js
const { spawn } = require('child_process');
const ps = spawn('ps', ['ax']);
const grep = spawn('grep', ['ssh']);

ps.stdout.on('data', (data) => {
  grep.stdin.write(data);
});

ps.stderr.on('data', (data) => {
  console.error(`ps stderr: ${data}`);
});

ps.on('close', (code) => {
  if (code !== 0) {
    console.log(`ps process exited with code ${code}`);
  }
  grep.stdin.end();
});

grep.stdout.on('data', (data) => {
  console.log(data.toString());
});

grep.stderr.on('data', (data) => {
  console.error(`grep stderr: ${data}`);
});

grep.on('close', (code) => {
  if (code !== 0) {
    console.log(`grep process exited with code ${code}`);
  }
});
```

Example of checking for failed `spawn`:

```js
const { spawn } = require('child_process');
const subprocess = spawn('bad_command');

subprocess.on('error', (err) => {
  console.error('Failed to start subprocess.');
});
```

Certain platforms (macOS, Linux) will use the value of `argv[0]` for the process
title while others (Windows, SunOS) will use `command`.

##### Parameters

| Parameter | Type | Description |
| ------ | ------ | ------ |
| `command` | `string` | The command to run. |
| `args` | readonly `string`[] | List of string arguments. |
| `options` | [`SpawnOptionsWithStdioTuple`](child_process.md#spawnoptionswithstdiotuplestdin-stdout-stderr)\<[`StdioNull`](child_process.md#stdionull), [`StdioPipe`](child_process.md#stdiopipe), [`StdioNull`](child_process.md#stdionull)\> | - |

##### Returns

[`ChildProcessByStdio`](child_process.md#childprocessbystdioi-o-e)\<`null`, [`DefaultReadableStream`](stream.md#defaultreadablestream), `null`\>

#### Call Signature

> **spawn**(`command`: `string`, `args`: readonly `string`[], `options`: [`SpawnOptionsWithStdioTuple`](child_process.md#spawnoptionswithstdiotuplestdin-stdout-stderr)\<[`StdioNull`](child_process.md#stdionull), [`StdioNull`](child_process.md#stdionull), [`StdioPipe`](child_process.md#stdiopipe)\>): [`ChildProcessByStdio`](child_process.md#childprocessbystdioi-o-e)\<`null`, `null`, [`DefaultReadableStream`](stream.md#defaultreadablestream)\>

The `child_process.spawn()` method spawns a new process using the given `command`, with command-line arguments in `args`.
If omitted, `args` defaults to an empty array.

**If the `shell` option is enabled, do not pass unsanitized user input to this**
**function. Any input containing shell metacharacters may be used to trigger**
**arbitrary command execution.**

A third argument may be used to specify additional options.

Use `cwd` to specify the working directory from which the process is spawned.
If not given, the default is to inherit the current working directory. If given,
but the path does not exist, the child process emits an `ENOENT` error
and exits immediately. `ENOENT` is also emitted when the command
does not exist.

Example of running `ls -lh /usr`, capturing `stdout`, `stderr`, and the
exit code:

```js
const { spawn } = require('child_process');
const ls = spawn('ls', ['-lh', '/usr']);

ls.stdout.on('data', (data) => {
  console.log(`stdout: ${data}`);
});

ls.stderr.on('data', (data) => {
  console.error(`stderr: ${data}`);
});

ls.on('close', (code) => {
  console.log(`child process exited with code ${code}`);
});
```

Example: A very elaborate way to run `ps ax | grep ssh`

```js
const { spawn } = require('child_process');
const ps = spawn('ps', ['ax']);
const grep = spawn('grep', ['ssh']);

ps.stdout.on('data', (data) => {
  grep.stdin.write(data);
});

ps.stderr.on('data', (data) => {
  console.error(`ps stderr: ${data}`);
});

ps.on('close', (code) => {
  if (code !== 0) {
    console.log(`ps process exited with code ${code}`);
  }
  grep.stdin.end();
});

grep.stdout.on('data', (data) => {
  console.log(data.toString());
});

grep.stderr.on('data', (data) => {
  console.error(`grep stderr: ${data}`);
});

grep.on('close', (code) => {
  if (code !== 0) {
    console.log(`grep process exited with code ${code}`);
  }
});
```

Example of checking for failed `spawn`:

```js
const { spawn } = require('child_process');
const subprocess = spawn('bad_command');

subprocess.on('error', (err) => {
  console.error('Failed to start subprocess.');
});
```

Certain platforms (macOS, Linux) will use the value of `argv[0]` for the process
title while others (Windows, SunOS) will use `command`.

##### Parameters

| Parameter | Type | Description |
| ------ | ------ | ------ |
| `command` | `string` | The command to run. |
| `args` | readonly `string`[] | List of string arguments. |
| `options` | [`SpawnOptionsWithStdioTuple`](child_process.md#spawnoptionswithstdiotuplestdin-stdout-stderr)\<[`StdioNull`](child_process.md#stdionull), [`StdioNull`](child_process.md#stdionull), [`StdioPipe`](child_process.md#stdiopipe)\> | - |

##### Returns

[`ChildProcessByStdio`](child_process.md#childprocessbystdioi-o-e)\<`null`, `null`, [`DefaultReadableStream`](stream.md#defaultreadablestream)\>

#### Call Signature

> **spawn**(`command`: `string`, `args`: readonly `string`[], `options`: [`SpawnOptionsWithStdioTuple`](child_process.md#spawnoptionswithstdiotuplestdin-stdout-stderr)\<[`StdioNull`](child_process.md#stdionull), [`StdioNull`](child_process.md#stdionull), [`StdioNull`](child_process.md#stdionull)\>): [`ChildProcessByStdio`](child_process.md#childprocessbystdioi-o-e)\<`null`, `null`, `null`\>

The `child_process.spawn()` method spawns a new process using the given `command`, with command-line arguments in `args`.
If omitted, `args` defaults to an empty array.

**If the `shell` option is enabled, do not pass unsanitized user input to this**
**function. Any input containing shell metacharacters may be used to trigger**
**arbitrary command execution.**

A third argument may be used to specify additional options.

Use `cwd` to specify the working directory from which the process is spawned.
If not given, the default is to inherit the current working directory. If given,
but the path does not exist, the child process emits an `ENOENT` error
and exits immediately. `ENOENT` is also emitted when the command
does not exist.

Example of running `ls -lh /usr`, capturing `stdout`, `stderr`, and the
exit code:

```js
const { spawn } = require('child_process');
const ls = spawn('ls', ['-lh', '/usr']);

ls.stdout.on('data', (data) => {
  console.log(`stdout: ${data}`);
});

ls.stderr.on('data', (data) => {
  console.error(`stderr: ${data}`);
});

ls.on('close', (code) => {
  console.log(`child process exited with code ${code}`);
});
```

Example: A very elaborate way to run `ps ax | grep ssh`

```js
const { spawn } = require('child_process');
const ps = spawn('ps', ['ax']);
const grep = spawn('grep', ['ssh']);

ps.stdout.on('data', (data) => {
  grep.stdin.write(data);
});

ps.stderr.on('data', (data) => {
  console.error(`ps stderr: ${data}`);
});

ps.on('close', (code) => {
  if (code !== 0) {
    console.log(`ps process exited with code ${code}`);
  }
  grep.stdin.end();
});

grep.stdout.on('data', (data) => {
  console.log(data.toString());
});

grep.stderr.on('data', (data) => {
  console.error(`grep stderr: ${data}`);
});

grep.on('close', (code) => {
  if (code !== 0) {
    console.log(`grep process exited with code ${code}`);
  }
});
```

Example of checking for failed `spawn`:

```js
const { spawn } = require('child_process');
const subprocess = spawn('bad_command');

subprocess.on('error', (err) => {
  console.error('Failed to start subprocess.');
});
```

Certain platforms (macOS, Linux) will use the value of `argv[0]` for the process
title while others (Windows, SunOS) will use `command`.

##### Parameters

| Parameter | Type | Description |
| ------ | ------ | ------ |
| `command` | `string` | The command to run. |
| `args` | readonly `string`[] | List of string arguments. |
| `options` | [`SpawnOptionsWithStdioTuple`](child_process.md#spawnoptionswithstdiotuplestdin-stdout-stderr)\<[`StdioNull`](child_process.md#stdionull), [`StdioNull`](child_process.md#stdionull), [`StdioNull`](child_process.md#stdionull)\> | - |

##### Returns

[`ChildProcessByStdio`](child_process.md#childprocessbystdioi-o-e)\<`null`, `null`, `null`\>

#### Call Signature

> **spawn**(`command`: `string`, `args`: readonly `string`[], `options`: [`SpawnOptions`](child_process.md#spawnoptions)): [`ChildProcess`](child_process.md#childprocess)

The `child_process.spawn()` method spawns a new process using the given `command`, with command-line arguments in `args`.
If omitted, `args` defaults to an empty array.

**If the `shell` option is enabled, do not pass unsanitized user input to this**
**function. Any input containing shell metacharacters may be used to trigger**
**arbitrary command execution.**

A third argument may be used to specify additional options.

Use `cwd` to specify the working directory from which the process is spawned.
If not given, the default is to inherit the current working directory. If given,
but the path does not exist, the child process emits an `ENOENT` error
and exits immediately. `ENOENT` is also emitted when the command
does not exist.

Example of running `ls -lh /usr`, capturing `stdout`, `stderr`, and the
exit code:

```js
const { spawn } = require('child_process');
const ls = spawn('ls', ['-lh', '/usr']);

ls.stdout.on('data', (data) => {
  console.log(`stdout: ${data}`);
});

ls.stderr.on('data', (data) => {
  console.error(`stderr: ${data}`);
});

ls.on('close', (code) => {
  console.log(`child process exited with code ${code}`);
});
```

Example: A very elaborate way to run `ps ax | grep ssh`

```js
const { spawn } = require('child_process');
const ps = spawn('ps', ['ax']);
const grep = spawn('grep', ['ssh']);

ps.stdout.on('data', (data) => {
  grep.stdin.write(data);
});

ps.stderr.on('data', (data) => {
  console.error(`ps stderr: ${data}`);
});

ps.on('close', (code) => {
  if (code !== 0) {
    console.log(`ps process exited with code ${code}`);
  }
  grep.stdin.end();
});

grep.stdout.on('data', (data) => {
  console.log(data.toString());
});

grep.stderr.on('data', (data) => {
  console.error(`grep stderr: ${data}`);
});

grep.on('close', (code) => {
  if (code !== 0) {
    console.log(`grep process exited with code ${code}`);
  }
});
```

Example of checking for failed `spawn`:

```js
const { spawn } = require('child_process');
const subprocess = spawn('bad_command');

subprocess.on('error', (err) => {
  console.error('Failed to start subprocess.');
});
```

Certain platforms (macOS, Linux) will use the value of `argv[0]` for the process
title while others (Windows, SunOS) will use `command`.

##### Parameters

| Parameter | Type | Description |
| ------ | ------ | ------ |
| `command` | `string` | The command to run. |
| `args` | readonly `string`[] | List of string arguments. |
| `options` | [`SpawnOptions`](child_process.md#spawnoptions) | - |

##### Returns

[`ChildProcess`](child_process.md#childprocess)



================================================
FILE: src/reference/modules/llrt/crypto.md
================================================
[@caido/quickjs-types](../index.md) / llrt/crypto

# llrt/crypto

## Classes

### Hash

The `Hash` class is a utility for creating hash digests of data.

Using the `hash.update()` and `hash.digest()` methods to produce the
computed hash.

The [createHash](crypto.md#createhash) method is used to create `Hash` instances.
`Hash`objects are not to be created directly using the `new` keyword.

Example: Using the `hash.update()` and `hash.digest()` methods:

```js
import { createHash } from 'crypto';

const hash = createHash('sha256');

hash.update('some data to hash');
console.log(hash.digest('hex'));
// Prints:
//   6a2da20943931e9834fc12cfe5bb47bbd9ae43489a30726962b576f4e3993e50
```

#### Methods

##### digest()

###### Call Signature

> **digest**(): [`Buffer`](buffer.md#buffer)

Calculates the digest of all of the data passed to be hashed (using the `hash.update()` method).
If `encoding` is provided a string will be returned; otherwise
a `Buffer` is returned.

The `Hash` object can not be used again after `hash.digest()` method has been
called. Multiple calls will cause an error to be thrown.

###### Returns

[`Buffer`](buffer.md#buffer)

###### Call Signature

> **digest**(`encoding`: [`BinaryToTextEncoding`](crypto.md#binarytotextencoding)): `string`

Calculates the digest of all of the data passed to be hashed (using the `hash.update()` method).
If `encoding` is provided a string will be returned; otherwise
a `Buffer` is returned.

The `Hash` object can not be used again after `hash.digest()` method has been
called. Multiple calls will cause an error to be thrown.

###### Parameters

| Parameter | Type | Description |
| ------ | ------ | ------ |
| `encoding` | [`BinaryToTextEncoding`](crypto.md#binarytotextencoding) | The `encoding` of the return value. |

###### Returns

`string`

##### update()

###### Call Signature

> **update**(`data`: [`BinaryLike`](crypto.md#binarylike)): [`Hash`](crypto.md#hash)

Updates the hash content with the given `data`, the encoding of which
is given in `inputEncoding`.
If `encoding` is not provided, and the `data` is a string, an
encoding of `'utf8'` is enforced. If `data` is a `Buffer`, `TypedArray`, or`DataView`,
then `inputEncoding` is ignored.

This can be called many times with new data as it is streamed.

###### Parameters

| Parameter | Type |
| ------ | ------ |
| `data` | [`BinaryLike`](crypto.md#binarylike) |

###### Returns

[`Hash`](crypto.md#hash)

###### Call Signature

> **update**(`data`: `string`, `inputEncoding`: [`Encoding`](crypto.md#encoding)): [`Hash`](crypto.md#hash)

Updates the hash content with the given `data`, the encoding of which
is given in `inputEncoding`.
If `encoding` is not provided, and the `data` is a string, an
encoding of `'utf8'` is enforced. If `data` is a `Buffer`, `TypedArray`, or`DataView`,
then `inputEncoding` is ignored.

This can be called many times with new data as it is streamed.

###### Parameters

| Parameter | Type | Description |
| ------ | ------ | ------ |
| `data` | `string` | - |
| `inputEncoding` | [`Encoding`](crypto.md#encoding) | The `encoding` of the `data` string. |

###### Returns

[`Hash`](crypto.md#hash)

***

### Hmac

The `Hmac` class is a utility for creating cryptographic HMAC digests.

Using the `hmac.update()` and `hmac.digest()` methods to produce the
computed HMAC digest.

The [createHmac](crypto.md#createhmac) method is used to create `Hmac` instances.
`Hmac`objects are not to be created directly using the `new` keyword.

Example: Using the `hmac.update()` and `hmac.digest()` methods:

```js
import { createHmac } from 'crypto';

const hmac = createHmac('sha256', 'a secret');

hmac.update('some data to hash');
console.log(hmac.digest('hex'));
// Prints:
//   7fd04df92f636fd450bc841c9418e5825c17f33ad9c87c518115a45971f7f77e
```

#### Methods

##### digest()

###### Call Signature

> **digest**(): [`Buffer`](buffer.md#buffer)

Calculates the HMAC digest of all of the data passed using `hmac.update()`.
If `encoding` is
provided a string is returned; otherwise a `Buffer` is returned;

The `Hmac` object can not be used again after `hmac.digest()` has been
called. Multiple calls to `hmac.digest()` will result in an error being thrown.

###### Returns

[`Buffer`](buffer.md#buffer)

###### Call Signature

> **digest**(`encoding`: [`BinaryToTextEncoding`](crypto.md#binarytotextencoding)): `string`

Calculates the HMAC digest of all of the data passed using `hmac.update()`.
If `encoding` is
provided a string is returned; otherwise a `Buffer` is returned;

The `Hmac` object can not be used again after `hmac.digest()` has been
called. Multiple calls to `hmac.digest()` will result in an error being thrown.

###### Parameters

| Parameter | Type | Description |
| ------ | ------ | ------ |
| `encoding` | [`BinaryToTextEncoding`](crypto.md#binarytotextencoding) | The `encoding` of the return value. |

###### Returns

`string`

##### update()

###### Call Signature

> **update**(`data`: [`BinaryLike`](crypto.md#binarylike)): [`Hmac`](crypto.md#hmac)

Updates the `Hmac` content with the given `data`, the encoding of which
is given in `inputEncoding`.
If `encoding` is not provided, and the `data` is a string, an
encoding of `'utf8'` is enforced. If `data` is a `Buffer`, `TypedArray`, or`DataView`,
then `inputEncoding` is ignored.

This can be called many times with new data as it is streamed.

###### Parameters

| Parameter | Type |
| ------ | ------ |
| `data` | [`BinaryLike`](crypto.md#binarylike) |

###### Returns

[`Hmac`](crypto.md#hmac)

###### Call Signature

> **update**(`data`: `string`, `inputEncoding`: [`Encoding`](crypto.md#encoding)): [`Hmac`](crypto.md#hmac)

Updates the `Hmac` content with the given `data`, the encoding of which
is given in `inputEncoding`.
If `encoding` is not provided, and the `data` is a string, an
encoding of `'utf8'` is enforced. If `data` is a `Buffer`, `TypedArray`, or`DataView`,
then `inputEncoding` is ignored.

This can be called many times with new data as it is streamed.

###### Parameters

| Parameter | Type | Description |
| ------ | ------ | ------ |
| `data` | `string` | - |
| `inputEncoding` | [`Encoding`](crypto.md#encoding) | The `encoding` of the `data` string. |

###### Returns

[`Hmac`](crypto.md#hmac)

## Type Aliases

### BinaryLike

> **BinaryLike**: `string` \| [`ArrayBufferView`](globals/namespaces/QuickJS.md#arraybufferview)

***

### BinaryToTextEncoding

> **BinaryToTextEncoding**: `"base64"` \| `"hex"`

***

### CharacterEncoding

> **CharacterEncoding**: `"utf8"` \| `"utf-8"` \| `"utf16le"` \| `"utf-16le"` \| `"latin1"`

***

### Encoding

> **Encoding**: [`BinaryToTextEncoding`](crypto.md#binarytotextencoding) \| [`CharacterEncoding`](crypto.md#characterencoding) \| [`LegacyCharacterEncoding`](crypto.md#legacycharacterencoding)

***

### LegacyCharacterEncoding

> **LegacyCharacterEncoding**: `"ascii"`

***

### UUID

> **UUID**: `` `${string}-${string}-${string}-${string}-${string}` ``

## Functions

### createHash()

> **createHash**(`algorithm`: `string`): [`Hash`](crypto.md#hash)

Creates and returns a `Hash` object that can be used to generate hash digests
using the given `algorithm`.

The `algorithm` is supported by `'sha1'`, `'sha256'`,`'sha384'` and `'sha512'`.

#### Parameters

| Parameter | Type |
| ------ | ------ |
| `algorithm` | `string` |

#### Returns

[`Hash`](crypto.md#hash)

***

### createHmac()

> **createHmac**(`algorithm`: `string`, `key`: [`BinaryLike`](crypto.md#binarylike)): [`Hmac`](crypto.md#hmac)

Creates and returns an `Hmac` object that uses the given `algorithm` and `key`.

The `algorithm` is supported by `'sha1'`, `'sha256'`,`'sha384'` and `'sha512'`.

The `key` is the HMAC key used to generate the cryptographic HMAC hash.
If it is a string, please consider `caveats when using strings as inputs to cryptographic APIs`.
If it was obtained from a cryptographically secure source of entropy, such as [randomBytes](crypto.md#randombytes)
or generateKey, its length should not exceed the block size of `algorithm`
(e.g., 512 bits for SHA-256).

#### Parameters

| Parameter | Type |
| ------ | ------ |
| `algorithm` | `string` |
| `key` | [`BinaryLike`](crypto.md#binarylike) |

#### Returns

[`Hmac`](crypto.md#hmac)

***

### getRandomValues()

> **getRandomValues**\<`T`\>(`typedArray`: `T`): `T`

A convenient alias for webcrypto.getRandomValues. This
implementation is not compliant with the Web Crypto spec, to write
web-compatible code use webcrypto.getRandomValues instead.

#### Type Parameters

| Type Parameter |
| ------ |
| `T` *extends* [`ArrayBufferView`](globals/namespaces/QuickJS.md#arraybufferview) |

#### Parameters

| Parameter | Type |
| ------ | ------ |
| `typedArray` | `T` |

#### Returns

`T`

Returns `typedArray`.

***

### randomBytes()

> **randomBytes**(`size`: `number`): [`Buffer`](buffer.md#buffer)

Generates cryptographically strong pseudorandom data. The `size` argument
is a number indicating the number of bytes to generate.

the random bytes are generated synchronously and returned as a `Buffer`.
An error will be thrown if there is a problem generating the bytes.

```js
// Synchronous
import { randomBytes } from 'crypto';

const buf = randomBytes(256);
console.log(
  `${buf.length} bytes of random data: ${buf.toString('hex')}`);
```

The `crypto.randomBytes()` method will not complete until there is
sufficient entropy available.
This should normally never take longer than a few milliseconds. The only time
when generating the random bytes may conceivably block for a longer period of
time is right after boot, when the whole system is still low on entropy.

#### Parameters

| Parameter | Type | Description |
| ------ | ------ | ------ |
| `size` | `number` | The number of bytes to generate. The `size` must not be larger than `2**31 - 1`. |

#### Returns

[`Buffer`](buffer.md#buffer)

***

### randomFill()

#### Call Signature

> **randomFill**\<`T`\>(`buffer`: `T`, `callback`: (`err`: `null` \| `Error`, `buf`: `T`) => `void`): `void`

This function is similar to [randomBytes](crypto.md#randombytes) but requires the first
argument to be a `Buffer` that will be filled. It also
requires that a callback is passed in.

If the `callback` function is not provided, an error will be thrown.

```js
import { Buffer } from 'buffer';
import { randomFill } from 'crypto';

const buf = Buffer.alloc(10);
randomFill(buf, (err, buf) => {
  if (err) throw err;
  console.log(buf.toString('hex'));
});

randomFill(buf, 5, (err, buf) => {
  if (err) throw err;
  console.log(buf.toString('hex'));
});

// The above is equivalent to the following:
randomFill(buf, 5, 5, (err, buf) => {
  if (err) throw err;
  console.log(buf.toString('hex'));
});
```

Any `ArrayBuffer`, `TypedArray`, or `DataView` instance may be passed as `buffer`.

While this includes instances of `Float32Array` and `Float64Array`, this
function should not be used to generate random floating-point numbers. The
result may contain `+Infinity`, `-Infinity`, and `NaN`, and even if the array
contains finite numbers only, they are not drawn from a uniform random
distribution and have no meaningful lower or upper bounds.

```js
import { Buffer } from 'buffer';
import { randomFill } from 'crypto';

const a = new Uint32Array(10);
randomFill(a, (err, buf) => {
  if (err) throw err;
  console.log(Buffer.from(buf.buffer, buf.byteOffset, buf.byteLength)
    .toString('hex'));
});

const b = new DataView(new ArrayBuffer(10));
randomFill(b, (err, buf) => {
  if (err) throw err;
  console.log(Buffer.from(buf.buffer, buf.byteOffset, buf.byteLength)
    .toString('hex'));
});

const c = new ArrayBuffer(10);
randomFill(c, (err, buf) => {
  if (err) throw err;
  console.log(Buffer.from(buf).toString('hex'));
});
```

##### Type Parameters

| Type Parameter |
| ------ |
| `T` *extends* [`ArrayBufferView`](globals/namespaces/QuickJS.md#arraybufferview) |

##### Parameters

| Parameter | Type | Description |
| ------ | ------ | ------ |
| `buffer` | `T` | Must be supplied. The size of the provided `buffer` must not be larger than `2**31 - 1`. |
| `callback` | (`err`: `null` \| `Error`, `buf`: `T`) => `void` | `function(err, buf) {}`. |

##### Returns

`void`

#### Call Signature

> **randomFill**\<`T`\>(`buffer`: `T`, `offset`: `number`, `callback`: (`err`: `null` \| `Error`, `buf`: `T`) => `void`): `void`

This function is similar to [randomBytes](crypto.md#randombytes) but requires the first
argument to be a `Buffer` that will be filled. It also
requires that a callback is passed in.

If the `callback` function is not provided, an error will be thrown.

```js
import { Buffer } from 'buffer';
import { randomFill } from 'crypto';

const buf = Buffer.alloc(10);
randomFill(buf, (err, buf) => {
  if (err) throw err;
  console.log(buf.toString('hex'));
});

randomFill(buf, 5, (err, buf) => {
  if (err) throw err;
  console.log(buf.toString('hex'));
});

// The above is equivalent to the following:
randomFill(buf, 5, 5, (err, buf) => {
  if (err) throw err;
  console.log(buf.toString('hex'));
});
```

Any `ArrayBuffer`, `TypedArray`, or `DataView` instance may be passed as `buffer`.

While this includes instances of `Float32Array` and `Float64Array`, this
function should not be used to generate random floating-point numbers. The
result may contain `+Infinity`, `-Infinity`, and `NaN`, and even if the array
contains finite numbers only, they are not drawn from a uniform random
distribution and have no meaningful lower or upper bounds.

```js
import { Buffer } from 'buffer';
import { randomFill } from 'crypto';

const a = new Uint32Array(10);
randomFill(a, (err, buf) => {
  if (err) throw err;
  console.log(Buffer.from(buf.buffer, buf.byteOffset, buf.byteLength)
    .toString('hex'));
});

const b = new DataView(new ArrayBuffer(10));
randomFill(b, (err, buf) => {
  if (err) throw err;
  console.log(Buffer.from(buf.buffer, buf.byteOffset, buf.byteLength)
    .toString('hex'));
});

const c = new ArrayBuffer(10);
randomFill(c, (err, buf) => {
  if (err) throw err;
  console.log(Buffer.from(buf).toString('hex'));
});
```

##### Type Parameters

| Type Parameter |
| ------ |
| `T` *extends* [`ArrayBufferView`](globals/namespaces/QuickJS.md#arraybufferview) |

##### Parameters

| Parameter | Type | Description |
| ------ | ------ | ------ |
| `buffer` | `T` | Must be supplied. The size of the provided `buffer` must not be larger than `2**31 - 1`. |
| `offset` | `number` |  |
| `callback` | (`err`: `null` \| `Error`, `buf`: `T`) => `void` | `function(err, buf) {}`. |

##### Returns

`void`

#### Call Signature

> **randomFill**\<`T`\>(`buffer`: `T`, `offset`: `number`, `size`: `number`, `callback`: (`err`: `null` \| `Error`, `buf`: `T`) => `void`): `void`

This function is similar to [randomBytes](crypto.md#randombytes) but requires the first
argument to be a `Buffer` that will be filled. It also
requires that a callback is passed in.

If the `callback` function is not provided, an error will be thrown.

```js
import { Buffer } from 'buffer';
import { randomFill } from 'crypto';

const buf = Buffer.alloc(10);
randomFill(buf, (err, buf) => {
  if (err) throw err;
  console.log(buf.toString('hex'));
});

randomFill(buf, 5, (err, buf) => {
  if (err) throw err;
  console.log(buf.toString('hex'));
});

// The above is equivalent to the following:
randomFill(buf, 5, 5, (err, buf) => {
  if (err) throw err;
  console.log(buf.toString('hex'));
});
```

Any `ArrayBuffer`, `TypedArray`, or `DataView` instance may be passed as `buffer`.

While this includes instances of `Float32Array` and `Float64Array`, this
function should not be used to generate random floating-point numbers. The
result may contain `+Infinity`, `-Infinity`, and `NaN`, and even if the array
contains finite numbers only, they are not drawn from a uniform random
distribution and have no meaningful lower or upper bounds.

```js
import { Buffer } from 'buffer';
import { randomFill } from 'crypto';

const a = new Uint32Array(10);
randomFill(a, (err, buf) => {
  if (err) throw err;
  console.log(Buffer.from(buf.buffer, buf.byteOffset, buf.byteLength)
    .toString('hex'));
});

const b = new DataView(new ArrayBuffer(10));
randomFill(b, (err, buf) => {
  if (err) throw err;
  console.log(Buffer.from(buf.buffer, buf.byteOffset, buf.byteLength)
    .toString('hex'));
});

const c = new ArrayBuffer(10);
randomFill(c, (err, buf) => {
  if (err) throw err;
  console.log(Buffer.from(buf).toString('hex'));
});
```

##### Type Parameters

| Type Parameter |
| ------ |
| `T` *extends* [`ArrayBufferView`](globals/namespaces/QuickJS.md#arraybufferview) |

##### Parameters

| Parameter | Type | Description |
| ------ | ------ | ------ |
| `buffer` | `T` | Must be supplied. The size of the provided `buffer` must not be larger than `2**31 - 1`. |
| `offset` | `number` |  |
| `size` | `number` |  |
| `callback` | (`err`: `null` \| `Error`, `buf`: `T`) => `void` | `function(err, buf) {}`. |

##### Returns

`void`

***

### randomFillSync()

> **randomFillSync**\<`T`\>(`buffer`: `T`, `offset`?: `number`, `size`?: `number`): `T`

Synchronous version of [randomFill](crypto.md#randomfill).

```js
import { Buffer } from 'buffer';
import { randomFillSync } from 'crypto';

const buf = Buffer.alloc(10);
console.log(randomFillSync(buf).toString('hex'));

randomFillSync(buf, 5);
console.log(buf.toString('hex'));

// The above is equivalent to the following:
randomFillSync(buf, 5, 5);
console.log(buf.toString('hex'));
```

Any `ArrayBuffer`, `TypedArray` or `DataView` instance may be passed as`buffer`.

```js
import { Buffer } from 'buffer';
import { randomFillSync } from 'crypto';

const a = new Uint32Array(10);
console.log(Buffer.from(randomFillSync(a).buffer,
                        a.byteOffset, a.byteLength).toString('hex'));

const b = new DataView(new ArrayBuffer(10));
console.log(Buffer.from(randomFillSync(b).buffer,
                        b.byteOffset, b.byteLength).toString('hex'));

const c = new ArrayBuffer(10);
console.log(Buffer.from(randomFillSync(c)).toString('hex'));
```

#### Type Parameters

| Type Parameter |
| ------ |
| `T` *extends* [`ArrayBufferView`](globals/namespaces/QuickJS.md#arraybufferview) |

#### Parameters

| Parameter | Type | Description |
| ------ | ------ | ------ |
| `buffer` | `T` | Must be supplied. The size of the provided `buffer` must not be larger than `2**31 - 1`. |
| `offset`? | `number` |  |
| `size`? | `number` |  |

#### Returns

`T`

The object passed as `buffer` argument.

***

### randomInt()

#### Call Signature

> **randomInt**(`max`: `number`): `number`

Return a random integer `n` such that `min <= n < max`.  This
implementation avoids [modulo bias](https://en.wikipedia.org/wiki/Fisher%E2%80%93Yates_shuffle#Modulo_bias).

The range (`max - min`) must be less than 2**48. `min` and `max` must
be [safe integers](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Number/isSafeInteger).

```js
// Synchronous
import { randomInt } from 'crypto';

const n = randomInt(3);
console.log(`Random number chosen from (0, 1, 2): ${n}`);
```

```js
// With `min` argument
import { randomInt } from 'crypto';

const n = randomInt(1, 7);
console.log(`The dice rolled: ${n}`);
```

##### Parameters

| Parameter | Type | Description |
| ------ | ------ | ------ |
| `max` | `number` | End of random range (exclusive). |

##### Returns

`number`

#### Call Signature

> **randomInt**(`min`: `number`, `max`: `number`): `number`

Return a random integer `n` such that `min <= n < max`.  This
implementation avoids [modulo bias](https://en.wikipedia.org/wiki/Fisher%E2%80%93Yates_shuffle#Modulo_bias).

The range (`max - min`) must be less than 2**48. `min` and `max` must
be [safe integers](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Number/isSafeInteger).

```js
// Synchronous
import { randomInt } from 'crypto';

const n = randomInt(3);
console.log(`Random number chosen from (0, 1, 2): ${n}`);
```

```js
// With `min` argument
import { randomInt } from 'crypto';

const n = randomInt(1, 7);
console.log(`The dice rolled: ${n}`);
```

##### Parameters

| Parameter | Type | Description |
| ------ | ------ | ------ |
| `min` | `number` | Start of random range (inclusive). |
| `max` | `number` | End of random range (exclusive). |

##### Returns

`number`

***

### randomUUID()

> **randomUUID**(): [`UUID`](crypto.md#uuid)

Generates a random [RFC 4122](https://www.rfc-editor.org/rfc/rfc4122.txt) version 4 UUID.
The UUID is generated using a cryptographic pseudorandom number generator.

#### Returns

[`UUID`](crypto.md#uuid)



================================================
FILE: src/reference/modules/llrt/dom-events.md
================================================
[@caido/quickjs-types](../index.md) / llrt/dom-events

# llrt/dom-events

## Classes

### CustomEvent\<D\>

An event which takes place in the system.

#### Type Parameters

| Type Parameter | Default type |
| ------ | ------ |
| `D` | `any` |

#### Implements

- [`Event`](dom-events.md#event)

#### Constructors

##### new CustomEvent()

> **new CustomEvent**\<`D`\>(`type`: `string`, `opts`?: `object`): [`CustomEvent`](dom-events.md#customeventd)\<`D`\>

###### Parameters

| Parameter | Type |
| ------ | ------ |
| `type` | `string` |
| `opts`? | \{ `details`: `D`; \} |
| `opts.details`? | `D` |

###### Returns

[`CustomEvent`](dom-events.md#customeventd)\<`D`\>

#### Properties

##### details

> `readonly` **details**: `null` \| `D`

##### type

> `readonly` **type**: `string`

Returns the type of event, e.g. "click", "hashchange", or "submit".

###### Implementation of

[`Event`](dom-events.md#event).[`type`](dom-events.md#type-1)

***

### EventTarget

EventTarget is an interface implemented by objects that can
receive events and may have listeners for them.

#### Extended by

- [`AbortSignal`](abort.md#abortsignal)

#### Constructors

##### new EventTarget()

> **new EventTarget**(): [`EventTarget`](dom-events.md#eventtarget)

###### Returns

[`EventTarget`](dom-events.md#eventtarget)

#### Methods

##### addEventListener()

> **addEventListener**(`type`: [`EventKey`](dom-events.md#eventkey), `listener`: [`EventListener`](dom-events.md#eventlistener), `options`?: [`AddEventListenerOptions`](dom-events.md#addeventlisteneroptions)): `void`

Adds a new handler for the `type` event. Any given `listener` is added only once per `type`.

If the `once` option is true, the `listener` is removed after the next time a `type` event is dispatched.

###### Parameters

| Parameter | Type |
| ------ | ------ |
| `type` | [`EventKey`](dom-events.md#eventkey) |
| `listener` | [`EventListener`](dom-events.md#eventlistener) |
| `options`? | [`AddEventListenerOptions`](dom-events.md#addeventlisteneroptions) |

###### Returns

`void`

##### dispatchEvent()

> **dispatchEvent**(`event`: [`Event`](dom-events.md#event)): `void`

Dispatches a synthetic event event to target

###### Parameters

| Parameter | Type |
| ------ | ------ |
| `event` | [`Event`](dom-events.md#event) |

###### Returns

`void`

##### removeEventListener()

> **removeEventListener**(`type`: [`EventKey`](dom-events.md#eventkey), `listener`: [`EventListener`](dom-events.md#eventlistener)): `void`

Removes the event listener in target's event listener list with the same type and callback

###### Parameters

| Parameter | Type |
| ------ | ------ |
| `type` | [`EventKey`](dom-events.md#eventkey) |
| `listener` | [`EventListener`](dom-events.md#eventlistener) |

###### Returns

`void`

## Interfaces

### AddEventListenerOptions

#### Properties

##### once?

> `optional` **once**: `boolean`

When `true`, the listener is automatically removed when it is first invoked. Default: `false`.

***

### Event

An event which takes place in the system.

#### Properties

##### type

> `readonly` **type**: [`EventKey`](dom-events.md#eventkey)

Returns the type of event, e.g. "click", "hashchange", or "submit".

***

### EventListener()

> **EventListener**(`evt`: [`Event`](dom-events.md#event)): `void`

#### Parameters

| Parameter | Type |
| ------ | ------ |
| `evt` | [`Event`](dom-events.md#event) |

#### Returns

`void`

## Type Aliases

### EventKey

> **EventKey**: `string` \| `symbol`



================================================
FILE: src/reference/modules/llrt/net.md
================================================
[@caido/quickjs-types](../index.md) / llrt/net

# llrt/net

## Classes

### Server

This class is used to create a TCP or `IPC` server.

#### Extends

- [`EventEmitter`](globals/index.md#eventemittert)

#### Constructors

##### new Server()

> **new Server**(`connectionListener`?: (`socket`: [`Socket`](net.md#socket)) => `void`): [`Server`](net.md#server)

###### Parameters

| Parameter | Type |
| ------ | ------ |
| `connectionListener`? | (`socket`: [`Socket`](net.md#socket)) => `void` |

###### Returns

[`Server`](net.md#server)

###### Overrides

[`EventEmitter`](globals/index.md#eventemittert).[`constructor`](globals/index.md#constructors)

##### new Server()

> **new Server**(`options`?: [`ServerOpts`](net.md#serveropts), `connectionListener`?: (`socket`: [`Socket`](net.md#socket)) => `void`): [`Server`](net.md#server)

###### Parameters

| Parameter | Type |
| ------ | ------ |
| `options`? | [`ServerOpts`](net.md#serveropts) |
| `connectionListener`? | (`socket`: [`Socket`](net.md#socket)) => `void` |

###### Returns

[`Server`](net.md#server)

###### Overrides

`EventEmitter.constructor`

#### Methods

##### addListener()

###### Call Signature

> **addListener**(`event`: `string`, `listener`: (...`args`: `any`[]) => `void`): `this`

events.EventEmitter
  1. close
  2. connection
  3. error
  4. listening

###### Parameters

| Parameter | Type |
| ------ | ------ |
| `event` | `string` |
| `listener` | (...`args`: `any`[]) => `void` |

###### Returns

`this`

###### Overrides

[`EventEmitter`](globals/index.md#eventemittert).[`addListener`](globals/index.md#addlistener)

###### Call Signature

> **addListener**(`event`: `"close"`, `listener`: () => `void`): `this`

events.EventEmitter
  1. close
  2. connection
  3. error
  4. listening

###### Parameters

| Parameter | Type |
| ------ | ------ |
| `event` | `"close"` |
| `listener` | () => `void` |

###### Returns

`this`

###### Overrides

`EventEmitter.addListener`

###### Call Signature

> **addListener**(`event`: `"connection"`, `listener`: (`socket`: [`Socket`](net.md#socket)) => `void`): `this`

events.EventEmitter
  1. close
  2. connection
  3. error
  4. listening

###### Parameters

| Parameter | Type |
| ------ | ------ |
| `event` | `"connection"` |
| `listener` | (`socket`: [`Socket`](net.md#socket)) => `void` |

###### Returns

`this`

###### Overrides

`EventEmitter.addListener`

###### Call Signature

> **addListener**(`event`: `"error"`, `listener`: (`err`: `Error`) => `void`): `this`

events.EventEmitter
  1. close
  2. connection
  3. error
  4. listening

###### Parameters

| Parameter | Type |
| ------ | ------ |
| `event` | `"error"` |
| `listener` | (`err`: `Error`) => `void` |

###### Returns

`this`

###### Overrides

`EventEmitter.addListener`

###### Call Signature

> **addListener**(`event`: `"listening"`, `listener`: () => `void`): `this`

events.EventEmitter
  1. close
  2. connection
  3. error
  4. listening

###### Parameters

| Parameter | Type |
| ------ | ------ |
| `event` | `"listening"` |
| `listener` | () => `void` |

###### Returns

`this`

###### Overrides

`EventEmitter.addListener`

##### address()

> **address**(): `null` \| `string` \| [`AddressInfo`](net.md#addressinfo)

Returns the bound `address`, the address `family` name, and `port` of the server
as reported by the operating system if listening on an IP socket
(useful to find which port was assigned when getting an OS-assigned address):`{ port: 12346, family: 'IPv4', address: '127.0.0.1' }`.

For a server listening on a pipe or Unix domain socket, the name is returned
as a string.

```js
const server = net.createServer((socket) => {
  socket.end('goodbye\n');
}).on('error', (err) => {
  // Handle errors here.
  throw err;
});

// Grab an arbitrary unused port.
server.listen(() => {
  console.log('opened server on', server.address());
});
```

`server.address()` returns `null` before the `'listening'` event has been
emitted or after calling `server.close()`.

###### Returns

`null` \| `string` \| [`AddressInfo`](net.md#addressinfo)

##### close()

> **close**(`callback`?: (`err`?: `Error`) => `void`): `this`

Stops the server from accepting new connections and keeps existing
connections. This function is asynchronous, the server is finally closed
when all connections are ended and the server emits a `'close'` event.
The optional `callback` will be called once the `'close'` event occurs. Unlike
that event, it will be called with an `Error` as its only argument if the server
was not open when it was closed.

###### Parameters

| Parameter | Type | Description |
| ------ | ------ | ------ |
| `callback`? | (`err`?: `Error`) => `void` | Called when the server is closed. |

###### Returns

`this`

##### emit()

###### Call Signature

> **emit**(`event`: `string` \| `symbol`, ...`args`: `any`[]): `boolean`

Synchronously calls each of the listeners registered for the event named `eventName`, in the order they were registered, passing the supplied arguments
to each.

```js
import { EventEmitter } from 'events';
const myEmitter = new EventEmitter();

// First listener
myEmitter.on('event', function firstListener() {
  console.log('Helloooo! first listener');
});
// Second listener
myEmitter.on('event', function secondListener(arg1, arg2) {
  console.log(`event with parameters ${arg1}, ${arg2} in second listener`);
});
// Third listener
myEmitter.on('event', function thirdListener(...args) {
  const parameters = args.join(', ');
  console.log(`event with parameters ${parameters} in third listener`);
});

myEmitter.emit('event', 1, 2, 3, 4, 5);

// Prints:
// Helloooo! first listener
// event with parameters 1, 2 in second listener
// event with parameters 1, 2, 3, 4, 5 in third listener
```

###### Parameters

| Parameter | Type |
| ------ | ------ |
| `event` | `string` \| `symbol` |
| ...`args` | `any`[] |

###### Returns

`boolean`

###### Overrides

[`EventEmitter`](globals/index.md#eventemittert).[`emit`](globals/index.md#emit)

###### Call Signature

> **emit**(`event`: `"close"`): `boolean`

###### Parameters

| Parameter | Type |
| ------ | ------ |
| `event` | `"close"` |

###### Returns

`boolean`

###### Overrides

`EventEmitter.emit`

###### Call Signature

> **emit**(`event`: `"connection"`, `socket`: [`Socket`](net.md#socket)): `boolean`

###### Parameters

| Parameter | Type |
| ------ | ------ |
| `event` | `"connection"` |
| `socket` | [`Socket`](net.md#socket) |

###### Returns

`boolean`

###### Overrides

`EventEmitter.emit`

###### Call Signature

> **emit**(`event`: `"error"`, `err`: `Error`): `boolean`

###### Parameters

| Parameter | Type |
| ------ | ------ |
| `event` | `"error"` |
| `err` | `Error` |

###### Returns

`boolean`

###### Overrides

`EventEmitter.emit`

###### Call Signature

> **emit**(`event`: `"listening"`): `boolean`

###### Parameters

| Parameter | Type |
| ------ | ------ |
| `event` | `"listening"` |

###### Returns

`boolean`

###### Overrides

`EventEmitter.emit`

##### eventNames()

> **eventNames**(): [`EventKey`](dom-events.md#eventkey)[]

Returns an array listing the events for which the emitter has registered
listeners. The values in the array are strings or `Symbol`s.

```js
import { EventEmitter } from 'events';

const myEE = new EventEmitter();
myEE.on('foo', () => {});
myEE.on('bar', () => {});

const sym = Symbol('symbol');
myEE.on(sym, () => {});

console.log(myEE.eventNames());
// Prints: [ 'foo', 'bar', Symbol(symbol) ]
```

###### Returns

[`EventKey`](dom-events.md#eventkey)[]

###### Inherited from

[`EventEmitter`](globals/index.md#eventemittert).[`eventNames`](globals/index.md#eventnames)

##### listen()

###### Call Signature

> **listen**(`listeningListener`?: () => `void`): `void`

Start a server listening for connections. A `net.Server` can be a TCP or
an `IPC` server depending on what it listens to.

Possible signatures:

* `server.listen(options[, callback])`
* `server.listen(path[, backlog][, callback])` for `IPC` servers
* `server.listen([port[, host[, backlog]]][, callback])` for TCP servers

This function is asynchronous. When the server starts listening, the `'listening'` event will be emitted. The last parameter `callback`will be added as a listener for the `'listening'`
event.

All `listen()` methods can take a `backlog` parameter to specify the maximum length of the queue of pending connections.
Currently this parameter is IGNORED, support will be added in the future.

All [Socket](net.md#socket) are set to `SO_REUSEADDR` (see [`socket(7)`](https://man7.org/linux/man-pages/man7/socket.7.html) for details).

The `server.listen()` method can be called again if and only if there was an error during the first `server.listen()`
call or `server.close()` has been called. Otherwise, an error will be thrown.

###### Parameters

| Parameter | Type |
| ------ | ------ |
| `listeningListener`? | () => `void` |

###### Returns

`void`

###### Call Signature

> **listen**(`port`?: `number`, `hostname`?: `string`, `backlog`?: `number`, `listeningListener`?: () => `void`): `void`

Start a server listening for connections. A `net.Server` can be a TCP or
an `IPC` server depending on what it listens to.

Possible signatures:

* `server.listen(options[, callback])`
* `server.listen(path[, backlog][, callback])` for `IPC` servers
* `server.listen([port[, host[, backlog]]][, callback])` for TCP servers

This function is asynchronous. When the server starts listening, the `'listening'` event will be emitted. The last parameter `callback`will be added as a listener for the `'listening'`
event.

All `listen()` methods can take a `backlog` parameter to specify the maximum length of the queue of pending connections.
Currently this parameter is IGNORED, support will be added in the future.

All [Socket](net.md#socket) are set to `SO_REUSEADDR` (see [`socket(7)`](https://man7.org/linux/man-pages/man7/socket.7.html) for details).

The `server.listen()` method can be called again if and only if there was an error during the first `server.listen()`
call or `server.close()` has been called. Otherwise, an error will be thrown.

###### Parameters

| Parameter | Type |
| ------ | ------ |
| `port`? | `number` |
| `hostname`? | `string` |
| `backlog`? | `number` |
| `listeningListener`? | () => `void` |

###### Returns

`void`

###### Call Signature

> **listen**(`port`?: `number`, `hostname`?: `string`, `listeningListener`?: () => `void`): `void`

Start a server listening for connections. A `net.Server` can be a TCP or
an `IPC` server depending on what it listens to.

Possible signatures:

* `server.listen(options[, callback])`
* `server.listen(path[, backlog][, callback])` for `IPC` servers
* `server.listen([port[, host[, backlog]]][, callback])` for TCP servers

This function is asynchronous. When the server starts listening, the `'listening'` event will be emitted. The last parameter `callback`will be added as a listener for the `'listening'`
event.

All `listen()` methods can take a `backlog` parameter to specify the maximum length of the queue of pending connections.
Currently this parameter is IGNORED, support will be added in the future.

All [Socket](net.md#socket) are set to `SO_REUSEADDR` (see [`socket(7)`](https://man7.org/linux/man-pages/man7/socket.7.html) for details).

The `server.listen()` method can be called again if and only if there was an error during the first `server.listen()`
call or `server.close()` has been called. Otherwise, an error will be thrown.

###### Parameters

| Parameter | Type |
| ------ | ------ |
| `port`? | `number` |
| `hostname`? | `string` |
| `listeningListener`? | () => `void` |

###### Returns

`void`

###### Call Signature

> **listen**(`port`?: `number`, `backlog`?: `number`, `listeningListener`?: () => `void`): `void`

Start a server listening for connections. A `net.Server` can be a TCP or
an `IPC` server depending on what it listens to.

Possible signatures:

* `server.listen(options[, callback])`
* `server.listen(path[, backlog][, callback])` for `IPC` servers
* `server.listen([port[, host[, backlog]]][, callback])` for TCP servers

This function is asynchronous. When the server starts listening, the `'listening'` event will be emitted. The last parameter `callback`will be added as a listener for the `'listening'`
event.

All `listen()` methods can take a `backlog` parameter to specify the maximum length of the queue of pending connections.
Currently this parameter is IGNORED, support will be added in the future.

All [Socket](net.md#socket) are set to `SO_REUSEADDR` (see [`socket(7)`](https://man7.org/linux/man-pages/man7/socket.7.html) for details).

The `server.listen()` method can be called again if and only if there was an error during the first `server.listen()`
call or `server.close()` has been called. Otherwise, an error will be thrown.

###### Parameters

| Parameter | Type |
| ------ | ------ |
| `port`? | `number` |
| `backlog`? | `number` |
| `listeningListener`? | () => `void` |

###### Returns

`void`

###### Call Signature

> **listen**(`port`?: `number`, `listeningListener`?: () => `void`): `void`

Start a server listening for connections. A `net.Server` can be a TCP or
an `IPC` server depending on what it listens to.

Possible signatures:

* `server.listen(options[, callback])`
* `server.listen(path[, backlog][, callback])` for `IPC` servers
* `server.listen([port[, host[, backlog]]][, callback])` for TCP servers

This function is asynchronous. When the server starts listening, the `'listening'` event will be emitted. The last parameter `callback`will be added as a listener for the `'listening'`
event.

All `listen()` methods can take a `backlog` parameter to specify the maximum length of the queue of pending connections.
Currently this parameter is IGNORED, support will be added in the future.

All [Socket](net.md#socket) are set to `SO_REUSEADDR` (see [`socket(7)`](https://man7.org/linux/man-pages/man7/socket.7.html) for details).

The `server.listen()` method can be called again if and only if there was an error during the first `server.listen()`
call or `server.close()` has been called. Otherwise, an error will be thrown.

###### Parameters

| Parameter | Type |
| ------ | ------ |
| `port`? | `number` |
| `listeningListener`? | () => `void` |

###### Returns

`void`

###### Call Signature

> **listen**(`path`: `string`, `backlog`?: `number`, `listeningListener`?: () => `void`): `void`

Start a server listening for connections. A `net.Server` can be a TCP or
an `IPC` server depending on what it listens to.

Possible signatures:

* `server.listen(options[, callback])`
* `server.listen(path[, backlog][, callback])` for `IPC` servers
* `server.listen([port[, host[, backlog]]][, callback])` for TCP servers

This function is asynchronous. When the server starts listening, the `'listening'` event will be emitted. The last parameter `callback`will be added as a listener for the `'listening'`
event.

All `listen()` methods can take a `backlog` parameter to specify the maximum length of the queue of pending connections.
Currently this parameter is IGNORED, support will be added in the future.

All [Socket](net.md#socket) are set to `SO_REUSEADDR` (see [`socket(7)`](https://man7.org/linux/man-pages/man7/socket.7.html) for details).

The `server.listen()` method can be called again if and only if there was an error during the first `server.listen()`
call or `server.close()` has been called. Otherwise, an error will be thrown.

###### Parameters

| Parameter | Type |
| ------ | ------ |
| `path` | `string` |
| `backlog`? | `number` |
| `listeningListener`? | () => `void` |

###### Returns

`void`

###### Call Signature

> **listen**(`path`: `string`, `listeningListener`?: () => `void`): `void`

Start a server listening for connections. A `net.Server` can be a TCP or
an `IPC` server depending on what it listens to.

Possible signatures:

* `server.listen(options[, callback])`
* `server.listen(path[, backlog][, callback])` for `IPC` servers
* `server.listen([port[, host[, backlog]]][, callback])` for TCP servers

This function is asynchronous. When the server starts listening, the `'listening'` event will be emitted. The last parameter `callback`will be added as a listener for the `'listening'`
event.

All `listen()` methods can take a `backlog` parameter to specify the maximum length of the queue of pending connections.
Currently this parameter is IGNORED, support will be added in the future.

All [Socket](net.md#socket) are set to `SO_REUSEADDR` (see [`socket(7)`](https://man7.org/linux/man-pages/man7/socket.7.html) for details).

The `server.listen()` method can be called again if and only if there was an error during the first `server.listen()`
call or `server.close()` has been called. Otherwise, an error will be thrown.

###### Parameters

| Parameter | Type |
| ------ | ------ |
| `path` | `string` |
| `listeningListener`? | () => `void` |

###### Returns

`void`

###### Call Signature

> **listen**(`options`: [`ListenOptions`](net.md#listenoptions), `listeningListener`?: () => `void`): `void`

Start a server listening for connections. A `net.Server` can be a TCP or
an `IPC` server depending on what it listens to.

Possible signatures:

* `server.listen(options[, callback])`
* `server.listen(path[, backlog][, callback])` for `IPC` servers
* `server.listen([port[, host[, backlog]]][, callback])` for TCP servers

This function is asynchronous. When the server starts listening, the `'listening'` event will be emitted. The last parameter `callback`will be added as a listener for the `'listening'`
event.

All `listen()` methods can take a `backlog` parameter to specify the maximum length of the queue of pending connections.
Currently this parameter is IGNORED, support will be added in the future.

All [Socket](net.md#socket) are set to `SO_REUSEADDR` (see [`socket(7)`](https://man7.org/linux/man-pages/man7/socket.7.html) for details).

The `server.listen()` method can be called again if and only if there was an error during the first `server.listen()`
call or `server.close()` has been called. Otherwise, an error will be thrown.

###### Parameters

| Parameter | Type |
| ------ | ------ |
| `options` | [`ListenOptions`](net.md#listenoptions) |
| `listeningListener`? | () => `void` |

###### Returns

`void`

##### off()

> **off**\<`K`\>(`eventName`: [`EventKey`](dom-events.md#eventkey), `listener`: (...`args`: `any`[]) => `void`): `this`

Alias for `emitter.removeListener()`.

###### Type Parameters

| Type Parameter |
| ------ |
| `K` |

###### Parameters

| Parameter | Type |
| ------ | ------ |
| `eventName` | [`EventKey`](dom-events.md#eventkey) |
| `listener` | (...`args`: `any`[]) => `void` |

###### Returns

`this`

###### Inherited from

[`EventEmitter`](globals/index.md#eventemittert).[`off`](globals/index.md#off)

##### on()

###### Call Signature

> **on**(`event`: `string`, `listener`: (...`args`: `any`[]) => `void`): `this`

Adds the `listener` function to the end of the listeners array for the event
named `eventName`. No checks are made to see if the `listener` has already
been added. Multiple calls passing the same combination of `eventName` and
`listener` will result in the `listener` being added, and called, multiple times.

```js
server.on('connection', (stream) => {
  console.log('someone connected!');
});
```

Returns a reference to the `EventEmitter`, so that calls can be chained.

By default, event listeners are invoked in the order they are added. The `emitter.prependListener()` method can be used as an alternative to add the
event listener to the beginning of the listeners array.

```js
import { EventEmitter } from 'events';
const myEE = new EventEmitter();
myEE.on('foo', () => console.log('a'));
myEE.prependListener('foo', () => console.log('b'));
myEE.emit('foo');
// Prints:
//   b
//   a
```

###### Parameters

| Parameter | Type | Description |
| ------ | ------ | ------ |
| `event` | `string` | - |
| `listener` | (...`args`: `any`[]) => `void` | The callback function |

###### Returns

`this`

###### Overrides

[`EventEmitter`](globals/index.md#eventemittert).[`on`](globals/index.md#on)

###### Call Signature

> **on**(`event`: `"close"`, `listener`: () => `void`): `this`

###### Parameters

| Parameter | Type |
| ------ | ------ |
| `event` | `"close"` |
| `listener` | () => `void` |

###### Returns

`this`

###### Overrides

`EventEmitter.on`

###### Call Signature

> **on**(`event`: `"connection"`, `listener`: (`socket`: [`Socket`](net.md#socket)) => `void`): `this`

###### Parameters

| Parameter | Type |
| ------ | ------ |
| `event` | `"connection"` |
| `listener` | (`socket`: [`Socket`](net.md#socket)) => `void` |

###### Returns

`this`

###### Overrides

`EventEmitter.on`

###### Call Signature

> **on**(`event`: `"error"`, `listener`: (`err`: `Error`) => `void`): `this`

###### Parameters

| Parameter | Type |
| ------ | ------ |
| `event` | `"error"` |
| `listener` | (`err`: `Error`) => `void` |

###### Returns

`this`

###### Overrides

`EventEmitter.on`

###### Call Signature

> **on**(`event`: `"listening"`, `listener`: () => `void`): `this`

###### Parameters

| Parameter | Type |
| ------ | ------ |
| `event` | `"listening"` |
| `listener` | () => `void` |

###### Returns

`this`

###### Overrides

`EventEmitter.on`

##### once()

###### Call Signature

> **once**(`event`: `string`, `listener`: (...`args`: `any`[]) => `void`): `this`

Adds a **one-time** `listener` function for the event named `eventName`. The
next time `eventName` is triggered, this listener is removed and then invoked.

Returns a reference to the `EventEmitter`, so that calls can be chained.

By default, event listeners are invoked in the order they are added. The `emitter.prependOnceListener()` method can be used as an alternative to add the
event listener to the beginning of the listeners array.

```js
import { EventEmitter } from 'events';
const myEE = new EventEmitter();
myEE.once('foo', () => console.log('a'));
myEE.prependOnceListener('foo', () => console.log('b'));
myEE.emit('foo');
// Prints:
//   b
//   a
```

###### Parameters

| Parameter | Type | Description |
| ------ | ------ | ------ |
| `event` | `string` | - |
| `listener` | (...`args`: `any`[]) => `void` | The callback function |

###### Returns

`this`

###### Since

v0.3.0

###### Overrides

[`EventEmitter`](globals/index.md#eventemittert).[`once`](globals/index.md#once)

###### Call Signature

> **once**(`event`: `"close"`, `listener`: () => `void`): `this`

###### Parameters

| Parameter | Type |
| ------ | ------ |
| `event` | `"close"` |
| `listener` | () => `void` |

###### Returns

`this`

###### Overrides

`EventEmitter.once`

###### Call Signature

> **once**(`event`: `"connection"`, `listener`: (`socket`: [`Socket`](net.md#socket)) => `void`): `this`

###### Parameters

| Parameter | Type |
| ------ | ------ |
| `event` | `"connection"` |
| `listener` | (`socket`: [`Socket`](net.md#socket)) => `void` |

###### Returns

`this`

###### Overrides

`EventEmitter.once`

###### Call Signature

> **once**(`event`: `"error"`, `listener`: (`err`: `Error`) => `void`): `this`

###### Parameters

| Parameter | Type |
| ------ | ------ |
| `event` | `"error"` |
| `listener` | (`err`: `Error`) => `void` |

###### Returns

`this`

###### Overrides

`EventEmitter.once`

###### Call Signature

> **once**(`event`: `"listening"`, `listener`: () => `void`): `this`

###### Parameters

| Parameter | Type |
| ------ | ------ |
| `event` | `"listening"` |
| `listener` | () => `void` |

###### Returns

`this`

###### Overrides

`EventEmitter.once`

##### prependListener()

###### Call Signature

> **prependListener**(`event`: `string`, `listener`: (...`args`: `any`[]) => `void`): `this`

Adds the `listener` function to the _beginning_ of the listeners array for the
event named `eventName`. No checks are made to see if the `listener` has
already been added. Multiple calls passing the same combination of `eventName`
and `listener` will result in the `listener` being added, and called, multiple times.

Returns a reference to the `EventEmitter`, so that calls can be chained.

###### Parameters

| Parameter | Type | Description |
| ------ | ------ | ------ |
| `event` | `string` | - |
| `listener` | (...`args`: `any`[]) => `void` | The callback function |

###### Returns

`this`

###### Overrides

[`EventEmitter`](globals/index.md#eventemittert).[`prependListener`](globals/index.md#prependlistener)

###### Call Signature

> **prependListener**(`event`: `"close"`, `listener`: () => `void`): `this`

###### Parameters

| Parameter | Type |
| ------ | ------ |
| `event` | `"close"` |
| `listener` | () => `void` |

###### Returns

`this`

###### Overrides

`EventEmitter.prependListener`

###### Call Signature

> **prependListener**(`event`: `"connection"`, `listener`: (`socket`: [`Socket`](net.md#socket)) => `void`): `this`

###### Parameters

| Parameter | Type |
| ------ | ------ |
| `event` | `"connection"` |
| `listener` | (`socket`: [`Socket`](net.md#socket)) => `void` |

###### Returns

`this`

###### Overrides

`EventEmitter.prependListener`

###### Call Signature

> **prependListener**(`event`: `"error"`, `listener`: (`err`: `Error`) => `void`): `this`

###### Parameters

| Parameter | Type |
| ------ | ------ |
| `event` | `"error"` |
| `listener` | (`err`: `Error`) => `void` |

###### Returns

`this`

###### Overrides

`EventEmitter.prependListener`

###### Call Signature

> **prependListener**(`event`: `"listening"`, `listener`: () => `void`): `this`

###### Parameters

| Parameter | Type |
| ------ | ------ |
| `event` | `"listening"` |
| `listener` | () => `void` |

###### Returns

`this`

###### Overrides

`EventEmitter.prependListener`

##### prependOnceListener()

###### Call Signature

> **prependOnceListener**(`event`: `string`, `listener`: (...`args`: `any`[]) => `void`): `this`

Adds a **one-time**`listener` function for the event named `eventName` to the _beginning_ of the listeners array.
The next time `eventName` is triggered, this listener is removed, and then invoked.

Returns a reference to the `EventEmitter`, so that calls can be chained.

###### Parameters

| Parameter | Type | Description |
| ------ | ------ | ------ |
| `event` | `string` | - |
| `listener` | (...`args`: `any`[]) => `void` | The callback function |

###### Returns

`this`

###### Overrides

[`EventEmitter`](globals/index.md#eventemittert).[`prependOnceListener`](globals/index.md#prependoncelistener)

###### Call Signature

> **prependOnceListener**(`event`: `"close"`, `listener`: () => `void`): `this`

###### Parameters

| Parameter | Type |
| ------ | ------ |
| `event` | `"close"` |
| `listener` | () => `void` |

###### Returns

`this`

###### Overrides

`EventEmitter.prependOnceListener`

###### Call Signature

> **prependOnceListener**(`event`: `"connection"`, `listener`: (`socket`: [`Socket`](net.md#socket)) => `void`): `this`

###### Parameters

| Parameter | Type |
| ------ | ------ |
| `event` | `"connection"` |
| `listener` | (`socket`: [`Socket`](net.md#socket)) => `void` |

###### Returns

`this`

###### Overrides

`EventEmitter.prependOnceListener`

###### Call Signature

> **prependOnceListener**(`event`: `"error"`, `listener`: (`err`: `Error`) => `void`): `this`

###### Parameters

| Parameter | Type |
| ------ | ------ |
| `event` | `"error"` |
| `listener` | (`err`: `Error`) => `void` |

###### Returns

`this`

###### Overrides

`EventEmitter.prependOnceListener`

###### Call Signature

> **prependOnceListener**(`event`: `"listening"`, `listener`: () => `void`): `this`

###### Parameters

| Parameter | Type |
| ------ | ------ |
| `event` | `"listening"` |
| `listener` | () => `void` |

###### Returns

`this`

###### Overrides

`EventEmitter.prependOnceListener`

##### removeListener()

> **removeListener**\<`K`\>(`eventName`: [`EventKey`](dom-events.md#eventkey), `listener`: (...`args`: `any`[]) => `void`): `this`

Removes the specified `listener` from the listener array for the event named `eventName`.

`removeListener()` will remove, at most, one instance of a listener from the
listener array. If any single listener has been added multiple times to the
listener array for the specified `eventName`, then `removeListener()` must be
called multiple times to remove each instance.

Once an event is emitted, all listeners attached to it at the time of emitting are called in order.
This implies that any `removeListener()` calls _after_ emitting and _before_ the last listener finishes execution
will not remove them from `emit()` in progress. Subsequent events behave as expected.

```js
import { EventEmitter } from 'events';
class MyEmitter extends EventEmitter {}
const myEmitter = new MyEmitter();

const callbackA = () => {
  console.log('A');
  myEmitter.removeListener('event', callbackB);
};

const callbackB = () => {
  console.log('B');
};

myEmitter.on('event', callbackA);

myEmitter.on('event', callbackB);

// callbackA removes listener callbackB but it will still be called.
// Internal listener array at time of emit [callbackA, callbackB]
myEmitter.emit('event');
// Prints:
//   A
//   B

// callbackB is now removed.
// Internal listener array [callbackA]
myEmitter.emit('event');
// Prints:
//   A
```

Because listeners are managed using an internal array, calling this will
change the position indices of any listener registered _after_ the listener
being removed. This will not impact the order in which listeners are called,
but it means that any copies of the listener array as returned by
the `emitter.listeners()` method will need to be recreated.

When a single function has been added as a handler multiple times for a single
event (as in the example below), `removeListener()` will remove the most
recently added instance. In the example the `once('ping')` listener is removed:

```js
import { EventEmitter } from 'events';
const ee = new EventEmitter();

function pong() {
  console.log('pong');
}

ee.on('ping', pong);
ee.once('ping', pong);
ee.removeListener('ping', pong);

ee.emit('ping');
ee.emit('ping');
```

Returns a reference to the `EventEmitter`, so that calls can be chained.

###### Type Parameters

| Type Parameter |
| ------ |
| `K` |

###### Parameters

| Parameter | Type |
| ------ | ------ |
| `eventName` | [`EventKey`](dom-events.md#eventkey) |
| `listener` | (...`args`: `any`[]) => `void` |

###### Returns

`this`

###### Inherited from

[`EventEmitter`](globals/index.md#eventemittert).[`removeListener`](globals/index.md#removelistener)

***

### Socket

This class is an abstraction of a TCP socket or a streaming `IPC` endpoint (only available on Unix with domain sockets).
It is also an `EventEmitter`.

A `net.Socket` can be created by the user and used directly to interact with a server. For example, it is returned by [createConnection](net.md#createconnection),
so the user can use it to talk to the server.

It can also be created by LLRT and passed to the user when a connection is received.
For example, it is passed to the listeners of a `'connection'` event emitted on a [Server](net.md#server), so the user can use it to interact with the client.

#### Extends

- [`DefaultDuplexStream`](stream.md#defaultduplexstream)

#### Constructors

##### new Socket()

> **new Socket**(`options`?: [`SocketConstructorOpts`](net.md#socketconstructoropts)): [`Socket`](net.md#socket)

###### Parameters

| Parameter | Type |
| ------ | ------ |
| `options`? | [`SocketConstructorOpts`](net.md#socketconstructoropts) |

###### Returns

[`Socket`](net.md#socket)

###### Overrides

[`DefaultDuplexStream`](stream.md#defaultduplexstream).[`constructor`](stream.md#constructors)

#### Properties

##### connecting

> `readonly` **connecting**: `boolean`

If `true`, `socket.connect(options[, connectListener])` was
called and has not yet finished. It will stay `true` until the socket becomes
connected, then it is set to `false` and the `'connect'` event is emitted. Note
that the `socket.connect(options[, connectListener])` callback is a listener for the `'connect'` event.

##### localAddress?

> `readonly` `optional` **localAddress**: `string`

The string representation of the local IP address the remote client is
connecting on. For example, in a server listening on `'0.0.0.0'`, if a client
connects on `'192.168.1.1'`, the value of `socket.localAddress` would be`'192.168.1.1'`.

##### localFamily?

> `readonly` `optional` **localFamily**: `string`

The string representation of the local IP family. `'IPv4'` or `'IPv6'`.

##### localPort?

> `readonly` `optional` **localPort**: `number`

The numeric representation of the local port. For example, `80` or `21`.

##### pending

> `readonly` **pending**: `boolean`

This is `true` if the socket is not connected yet, either because `.connect()`has not yet been called or because it is still in the process of connecting
(see `socket.connecting`).

##### readyState

> `readonly` **readyState**: [`SocketReadyState`](net.md#socketreadystate)

This property represents the state of the connection as a string.

* If the stream is connecting `socket.readyState` is `opening`.
* If the stream is readable and writable, it is `open`.
* If the stream is readable and not writable, it is `readOnly`.
* If the stream is not readable and writable, it is `writeOnly`.

##### remoteAddress?

> `readonly` `optional` **remoteAddress**: `string`

The string representation of the remote IP address. For example,`'74.125.127.100'` or `'2001:4860:a005::68'`. Value may be `undefined` if
the socket is destroyed (for example, if the client disconnected).

##### remoteFamily?

> `readonly` `optional` **remoteFamily**: `string`

The string representation of the remote IP family. `'IPv4'` or `'IPv6'`. Value may be `undefined` if
the socket is destroyed (for example, if the client disconnected).

##### remotePort?

> `readonly` `optional` **remotePort**: `number`

The numeric representation of the remote port. For example, `80` or `21`. Value may be `undefined` if
the socket is destroyed (for example, if the client disconnected).

#### Methods

##### \[dispose\]()

> **\[dispose\]**(): `void`

Calls `readable.destroy()`.

###### Returns

`void`

###### Inherited from

[`DefaultDuplexStream`](stream.md#defaultduplexstream).[`[dispose]`](stream.md#dispose)

##### addListener()

###### Call Signature

> **addListener**(`event`: `string`, `listener`: (...`args`: `any`[]) => `void`): `this`

events.EventEmitter
  1. close
  2. connect
  3. data
  4. end
  5. error

###### Parameters

| Parameter | Type |
| ------ | ------ |
| `event` | `string` |
| `listener` | (...`args`: `any`[]) => `void` |

###### Returns

`this`

###### Overrides

[`DefaultDuplexStream`](stream.md#defaultduplexstream).[`addListener`](stream.md#addlistener)

###### Call Signature

> **addListener**(`event`: `"close"`, `listener`: (`hadError`: `boolean`) => `void`): `this`

events.EventEmitter
  1. close
  2. connect
  3. data
  4. end
  5. error

###### Parameters

| Parameter | Type |
| ------ | ------ |
| `event` | `"close"` |
| `listener` | (`hadError`: `boolean`) => `void` |

###### Returns

`this`

###### Overrides

[`DefaultDuplexStream`](stream.md#defaultduplexstream).[`addListener`](stream.md#addlistener)

###### Call Signature

> **addListener**(`event`: `"connect"`, `listener`: () => `void`): `this`

events.EventEmitter
  1. close
  2. connect
  3. data
  4. end
  5. error

###### Parameters

| Parameter | Type |
| ------ | ------ |
| `event` | `"connect"` |
| `listener` | () => `void` |

###### Returns

`this`

###### Overrides

[`DefaultDuplexStream`](stream.md#defaultduplexstream).[`addListener`](stream.md#addlistener)

###### Call Signature

> **addListener**(`event`: `"data"`, `listener`: (`data`: [`Buffer`](buffer.md#buffer)) => `void`): `this`

events.EventEmitter
  1. close
  2. connect
  3. data
  4. end
  5. error

###### Parameters

| Parameter | Type |
| ------ | ------ |
| `event` | `"data"` |
| `listener` | (`data`: [`Buffer`](buffer.md#buffer)) => `void` |

###### Returns

`this`

###### Overrides

[`DefaultDuplexStream`](stream.md#defaultduplexstream).[`addListener`](stream.md#addlistener)

###### Call Signature

> **addListener**(`event`: `"drain"`, `listener`: () => `void`): `this`

events.EventEmitter
  1. close
  2. connect
  3. data
  4. end
  5. error

###### Parameters

| Parameter | Type |
| ------ | ------ |
| `event` | `"drain"` |
| `listener` | () => `void` |

###### Returns

`this`

###### Overrides

`Duplex.addListener`

###### Call Signature

> **addListener**(`event`: `"end"`, `listener`: () => `void`): `this`

events.EventEmitter
  1. close
  2. connect
  3. data
  4. end
  5. error

###### Parameters

| Parameter | Type |
| ------ | ------ |
| `event` | `"end"` |
| `listener` | () => `void` |

###### Returns

`this`

###### Overrides

`Duplex.addListener`

###### Call Signature

> **addListener**(`event`: `"error"`, `listener`: (`err`: `Error`) => `void`): `this`

events.EventEmitter
  1. close
  2. connect
  3. data
  4. end
  5. error

###### Parameters

| Parameter | Type |
| ------ | ------ |
| `event` | `"error"` |
| `listener` | (`err`: `Error`) => `void` |

###### Returns

`this`

###### Overrides

`Duplex.addListener`

##### address()

> **address**(): \{\} \| [`AddressInfo`](net.md#addressinfo)

Returns the bound `address`, the address `family` name and `port` of the
socket as reported by the operating system:`{ port: 12346, family: 'IPv4', address: '127.0.0.1' }`

###### Returns

\{\} \| [`AddressInfo`](net.md#addressinfo)

###### Since

v0.1.90

##### connect()

###### Call Signature

> **connect**(`options`: [`SocketConnectOpts`](net.md#socketconnectopts), `connectionListener`?: () => `void`): `this`

Initiate a connection on a given socket.

Possible signatures:

* `socket.connect(options[, connectListener])`
* `socket.connect(path[, connectListener])` for `IPC` connections.
* `socket.connect(port[, host][, connectListener])` for TCP connections.
* Returns: `net.Socket` The socket itself.

This function is asynchronous. When the connection is established, the `'connect'` event will be emitted. If there is a problem connecting,
instead of a `'connect'` event, an `'error'` event will be emitted with
the error passed to the `'error'` listener.
The last parameter `connectListener`, if supplied, will be added as a listener
for the `'connect'` event **once**.

This function should only be used for reconnecting a socket after`'close'` has been emitted or otherwise it may lead to undefined
behavior.

###### Parameters

| Parameter | Type |
| ------ | ------ |
| `options` | [`SocketConnectOpts`](net.md#socketconnectopts) |
| `connectionListener`? | () => `void` |

###### Returns

`this`

###### Call Signature

> **connect**(`port`: `number`, `host`: `string`, `connectionListener`?: () => `void`): `this`

Initiate a connection on a given socket.

Possible signatures:

* `socket.connect(options[, connectListener])`
* `socket.connect(path[, connectListener])` for `IPC` connections.
* `socket.connect(port[, host][, connectListener])` for TCP connections.
* Returns: `net.Socket` The socket itself.

This function is asynchronous. When the connection is established, the `'connect'` event will be emitted. If there is a problem connecting,
instead of a `'connect'` event, an `'error'` event will be emitted with
the error passed to the `'error'` listener.
The last parameter `connectListener`, if supplied, will be added as a listener
for the `'connect'` event **once**.

This function should only be used for reconnecting a socket after`'close'` has been emitted or otherwise it may lead to undefined
behavior.

###### Parameters

| Parameter | Type |
| ------ | ------ |
| `port` | `number` |
| `host` | `string` |
| `connectionListener`? | () => `void` |

###### Returns

`this`

###### Call Signature

> **connect**(`port`: `number`, `connectionListener`?: () => `void`): `this`

Initiate a connection on a given socket.

Possible signatures:

* `socket.connect(options[, connectListener])`
* `socket.connect(path[, connectListener])` for `IPC` connections.
* `socket.connect(port[, host][, connectListener])` for TCP connections.
* Returns: `net.Socket` The socket itself.

This function is asynchronous. When the connection is established, the `'connect'` event will be emitted. If there is a problem connecting,
instead of a `'connect'` event, an `'error'` event will be emitted with
the error passed to the `'error'` listener.
The last parameter `connectListener`, if supplied, will be added as a listener
for the `'connect'` event **once**.

This function should only be used for reconnecting a socket after`'close'` has been emitted or otherwise it may lead to undefined
behavior.

###### Parameters

| Parameter | Type |
| ------ | ------ |
| `port` | `number` |
| `connectionListener`? | () => `void` |

###### Returns

`this`

###### Call Signature

> **connect**(`path`: `string`, `connectionListener`?: () => `void`): `this`

Initiate a connection on a given socket.

Possible signatures:

* `socket.connect(options[, connectListener])`
* `socket.connect(path[, connectListener])` for `IPC` connections.
* `socket.connect(port[, host][, connectListener])` for TCP connections.
* Returns: `net.Socket` The socket itself.

This function is asynchronous. When the connection is established, the `'connect'` event will be emitted. If there is a problem connecting,
instead of a `'connect'` event, an `'error'` event will be emitted with
the error passed to the `'error'` listener.
The last parameter `connectListener`, if supplied, will be added as a listener
for the `'connect'` event **once**.

This function should only be used for reconnecting a socket after`'close'` has been emitted or otherwise it may lead to undefined
behavior.

###### Parameters

| Parameter | Type |
| ------ | ------ |
| `path` | `string` |
| `connectionListener`? | () => `void` |

###### Returns

`this`

##### destroy()

> **destroy**(`error`?: `Error`): `this`

Destroy the stream. Optionally emit an `'error'` event, and emit a `'close'` event. After this call, the readable
stream will release any internal resources and subsequent calls to `push()` will be ignored.

Once `destroy()` has been called any further calls will be a no-op and no
further errors except from `_destroy()` may be emitted as `'error'`.

Implementors should not override this method, but instead implement `readable._destroy()`.

###### Parameters

| Parameter | Type | Description |
| ------ | ------ | ------ |
| `error`? | `Error` | Error which will be passed as payload in `'error'` event |

###### Returns

`this`

###### Inherited from

[`DefaultDuplexStream`](stream.md#defaultduplexstream).[`destroy`](stream.md#destroy)

##### emit()

###### Call Signature

> **emit**(`event`: `string` \| `symbol`, ...`args`: `any`[]): `boolean`

Synchronously calls each of the listeners registered for the event named `eventName`, in the order they were registered, passing the supplied arguments
to each.

```js
import { EventEmitter } from 'events';
const myEmitter = new EventEmitter();

// First listener
myEmitter.on('event', function firstListener() {
  console.log('Helloooo! first listener');
});
// Second listener
myEmitter.on('event', function secondListener(arg1, arg2) {
  console.log(`event with parameters ${arg1}, ${arg2} in second listener`);
});
// Third listener
myEmitter.on('event', function thirdListener(...args) {
  const parameters = args.join(', ');
  console.log(`event with parameters ${parameters} in third listener`);
});

myEmitter.emit('event', 1, 2, 3, 4, 5);

// Prints:
// Helloooo! first listener
// event with parameters 1, 2 in second listener
// event with parameters 1, 2, 3, 4, 5 in third listener
```

###### Parameters

| Parameter | Type |
| ------ | ------ |
| `event` | `string` \| `symbol` |
| ...`args` | `any`[] |

###### Returns

`boolean`

###### Overrides

[`DefaultDuplexStream`](stream.md#defaultduplexstream).[`emit`](stream.md#emit)

###### Call Signature

> **emit**(`event`: `"close"`, `hadError`: `boolean`): `boolean`

###### Parameters

| Parameter | Type |
| ------ | ------ |
| `event` | `"close"` |
| `hadError` | `boolean` |

###### Returns

`boolean`

###### Overrides

[`DefaultDuplexStream`](stream.md#defaultduplexstream).[`emit`](stream.md#emit)

###### Call Signature

> **emit**(`event`: `"connect"`): `boolean`

###### Parameters

| Parameter | Type |
| ------ | ------ |
| `event` | `"connect"` |

###### Returns

`boolean`

###### Overrides

[`DefaultDuplexStream`](stream.md#defaultduplexstream).[`emit`](stream.md#emit)

###### Call Signature

> **emit**(`event`: `"data"`, `data`: [`Buffer`](buffer.md#buffer)): `boolean`

###### Parameters

| Parameter | Type |
| ------ | ------ |
| `event` | `"data"` |
| `data` | [`Buffer`](buffer.md#buffer) |

###### Returns

`boolean`

###### Overrides

[`DefaultDuplexStream`](stream.md#defaultduplexstream).[`emit`](stream.md#emit)

###### Call Signature

> **emit**(`event`: `"end"`): `boolean`

###### Parameters

| Parameter | Type |
| ------ | ------ |
| `event` | `"end"` |

###### Returns

`boolean`

###### Overrides

`Duplex.emit`

###### Call Signature

> **emit**(`event`: `"error"`, `err`: `Error`): `boolean`

###### Parameters

| Parameter | Type |
| ------ | ------ |
| `event` | `"error"` |
| `err` | `Error` |

###### Returns

`boolean`

###### Overrides

`Duplex.emit`

##### end()

> **end**(`callback`?: () => `void`): `this`

Half-closes the socket. i.e., it sends a FIN packet. It is possible the server will still send some data.

###### Parameters

| Parameter | Type | Description |
| ------ | ------ | ------ |
| `callback`? | () => `void` | Optional callback for when the socket is finished. |

###### Returns

`this`

The socket itself.

###### Overrides

[`DefaultDuplexStream`](stream.md#defaultduplexstream).[`end`](stream.md#end)

##### eventNames()

> **eventNames**(): [`EventKey`](dom-events.md#eventkey)[]

Returns an array listing the events for which the emitter has registered
listeners. The values in the array are strings or `Symbol`s.

```js
import { EventEmitter } from 'events';

const myEE = new EventEmitter();
myEE.on('foo', () => {});
myEE.on('bar', () => {});

const sym = Symbol('symbol');
myEE.on(sym, () => {});

console.log(myEE.eventNames());
// Prints: [ 'foo', 'bar', Symbol(symbol) ]
```

###### Returns

[`EventKey`](dom-events.md#eventkey)[]

###### Inherited from

[`DefaultDuplexStream`](stream.md#defaultduplexstream).[`eventNames`](stream.md#eventnames)

##### off()

> **off**\<`K`\>(`eventName`: [`EventKey`](dom-events.md#eventkey), `listener`: (...`args`: `any`[]) => `void`): `this`

Alias for `emitter.removeListener()`.

###### Type Parameters

| Type Parameter |
| ------ |
| `K` |

###### Parameters

| Parameter | Type |
| ------ | ------ |
| `eventName` | [`EventKey`](dom-events.md#eventkey) |
| `listener` | (...`args`: `any`[]) => `void` |

###### Returns

`this`

###### Inherited from

[`DefaultDuplexStream`](stream.md#defaultduplexstream).[`off`](stream.md#off)

##### on()

###### Call Signature

> **on**(`event`: `string`, `listener`: (...`args`: `any`[]) => `void`): `this`

Adds the `listener` function to the end of the listeners array for the event
named `eventName`. No checks are made to see if the `listener` has already
been added. Multiple calls passing the same combination of `eventName` and
`listener` will result in the `listener` being added, and called, multiple times.

```js
server.on('connection', (stream) => {
  console.log('someone connected!');
});
```

Returns a reference to the `EventEmitter`, so that calls can be chained.

By default, event listeners are invoked in the order they are added. The `emitter.prependListener()` method can be used as an alternative to add the
event listener to the beginning of the listeners array.

```js
import { EventEmitter } from 'events';
const myEE = new EventEmitter();
myEE.on('foo', () => console.log('a'));
myEE.prependListener('foo', () => console.log('b'));
myEE.emit('foo');
// Prints:
//   b
//   a
```

###### Parameters

| Parameter | Type | Description |
| ------ | ------ | ------ |
| `event` | `string` | - |
| `listener` | (...`args`: `any`[]) => `void` | The callback function |

###### Returns

`this`

###### Overrides

[`DefaultDuplexStream`](stream.md#defaultduplexstream).[`on`](stream.md#on)

###### Call Signature

> **on**(`event`: `"close"`, `listener`: (`hadError`: `boolean`) => `void`): `this`

###### Parameters

| Parameter | Type |
| ------ | ------ |
| `event` | `"close"` |
| `listener` | (`hadError`: `boolean`) => `void` |

###### Returns

`this`

###### Overrides

[`DefaultDuplexStream`](stream.md#defaultduplexstream).[`on`](stream.md#on)

###### Call Signature

> **on**(`event`: `"connect"`, `listener`: () => `void`): `this`

###### Parameters

| Parameter | Type |
| ------ | ------ |
| `event` | `"connect"` |
| `listener` | () => `void` |

###### Returns

`this`

###### Overrides

[`DefaultDuplexStream`](stream.md#defaultduplexstream).[`on`](stream.md#on)

###### Call Signature

> **on**(`event`: `"data"`, `listener`: (`data`: [`Buffer`](buffer.md#buffer)) => `void`): `this`

###### Parameters

| Parameter | Type |
| ------ | ------ |
| `event` | `"data"` |
| `listener` | (`data`: [`Buffer`](buffer.md#buffer)) => `void` |

###### Returns

`this`

###### Overrides

[`DefaultDuplexStream`](stream.md#defaultduplexstream).[`on`](stream.md#on)

###### Call Signature

> **on**(`event`: `"end"`, `listener`: () => `void`): `this`

###### Parameters

| Parameter | Type |
| ------ | ------ |
| `event` | `"end"` |
| `listener` | () => `void` |

###### Returns

`this`

###### Overrides

`Duplex.on`

###### Call Signature

> **on**(`event`: `"error"`, `listener`: (`err`: `Error`) => `void`): `this`

###### Parameters

| Parameter | Type |
| ------ | ------ |
| `event` | `"error"` |
| `listener` | (`err`: `Error`) => `void` |

###### Returns

`this`

###### Overrides

`Duplex.on`

##### once()

###### Call Signature

> **once**(`event`: `string`, `listener`: (...`args`: `any`[]) => `void`): `this`

Adds a **one-time** `listener` function for the event named `eventName`. The
next time `eventName` is triggered, this listener is removed and then invoked.

Returns a reference to the `EventEmitter`, so that calls can be chained.

By default, event listeners are invoked in the order they are added. The `emitter.prependOnceListener()` method can be used as an alternative to add the
event listener to the beginning of the listeners array.

```js
import { EventEmitter } from 'events';
const myEE = new EventEmitter();
myEE.once('foo', () => console.log('a'));
myEE.prependOnceListener('foo', () => console.log('b'));
myEE.emit('foo');
// Prints:
//   b
//   a
```

###### Parameters

| Parameter | Type | Description |
| ------ | ------ | ------ |
| `event` | `string` | - |
| `listener` | (...`args`: `any`[]) => `void` | The callback function |

###### Returns

`this`

###### Since

v0.3.0

###### Overrides

[`DefaultDuplexStream`](stream.md#defaultduplexstream).[`once`](stream.md#once)

###### Call Signature

> **once**(`event`: `"close"`, `listener`: (`hadError`: `boolean`) => `void`): `this`

###### Parameters

| Parameter | Type |
| ------ | ------ |
| `event` | `"close"` |
| `listener` | (`hadError`: `boolean`) => `void` |

###### Returns

`this`

###### Overrides

[`DefaultDuplexStream`](stream.md#defaultduplexstream).[`once`](stream.md#once)

###### Call Signature

> **once**(`event`: `"connect"`, `listener`: () => `void`): `this`

###### Parameters

| Parameter | Type |
| ------ | ------ |
| `event` | `"connect"` |
| `listener` | () => `void` |

###### Returns

`this`

###### Overrides

[`DefaultDuplexStream`](stream.md#defaultduplexstream).[`once`](stream.md#once)

###### Call Signature

> **once**(`event`: `"data"`, `listener`: (`data`: [`Buffer`](buffer.md#buffer)) => `void`): `this`

###### Parameters

| Parameter | Type |
| ------ | ------ |
| `event` | `"data"` |
| `listener` | (`data`: [`Buffer`](buffer.md#buffer)) => `void` |

###### Returns

`this`

###### Overrides

[`DefaultDuplexStream`](stream.md#defaultduplexstream).[`once`](stream.md#once)

###### Call Signature

> **once**(`event`: `"end"`, `listener`: () => `void`): `this`

###### Parameters

| Parameter | Type |
| ------ | ------ |
| `event` | `"end"` |
| `listener` | () => `void` |

###### Returns

`this`

###### Overrides

`Duplex.once`

###### Call Signature

> **once**(`event`: `"error"`, `listener`: (`err`: `Error`) => `void`): `this`

###### Parameters

| Parameter | Type |
| ------ | ------ |
| `event` | `"error"` |
| `listener` | (`err`: `Error`) => `void` |

###### Returns

`this`

###### Overrides

`Duplex.once`

##### prependListener()

###### Call Signature

> **prependListener**(`event`: `string`, `listener`: (...`args`: `any`[]) => `void`): `this`

Adds the `listener` function to the _beginning_ of the listeners array for the
event named `eventName`. No checks are made to see if the `listener` has
already been added. Multiple calls passing the same combination of `eventName`
and `listener` will result in the `listener` being added, and called, multiple times.

Returns a reference to the `EventEmitter`, so that calls can be chained.

###### Parameters

| Parameter | Type | Description |
| ------ | ------ | ------ |
| `event` | `string` | - |
| `listener` | (...`args`: `any`[]) => `void` | The callback function |

###### Returns

`this`

###### Overrides

[`DefaultDuplexStream`](stream.md#defaultduplexstream).[`prependListener`](stream.md#prependlistener)

###### Call Signature

> **prependListener**(`event`: `"close"`, `listener`: (`hadError`: `boolean`) => `void`): `this`

###### Parameters

| Parameter | Type |
| ------ | ------ |
| `event` | `"close"` |
| `listener` | (`hadError`: `boolean`) => `void` |

###### Returns

`this`

###### Overrides

[`DefaultDuplexStream`](stream.md#defaultduplexstream).[`prependListener`](stream.md#prependlistener)

###### Call Signature

> **prependListener**(`event`: `"connect"`, `listener`: () => `void`): `this`

###### Parameters

| Parameter | Type |
| ------ | ------ |
| `event` | `"connect"` |
| `listener` | () => `void` |

###### Returns

`this`

###### Overrides

[`DefaultDuplexStream`](stream.md#defaultduplexstream).[`prependListener`](stream.md#prependlistener)

###### Call Signature

> **prependListener**(`event`: `"data"`, `listener`: (`data`: [`Buffer`](buffer.md#buffer)) => `void`): `this`

###### Parameters

| Parameter | Type |
| ------ | ------ |
| `event` | `"data"` |
| `listener` | (`data`: [`Buffer`](buffer.md#buffer)) => `void` |

###### Returns

`this`

###### Overrides

[`DefaultDuplexStream`](stream.md#defaultduplexstream).[`prependListener`](stream.md#prependlistener)

###### Call Signature

> **prependListener**(`event`: `"end"`, `listener`: () => `void`): `this`

###### Parameters

| Parameter | Type |
| ------ | ------ |
| `event` | `"end"` |
| `listener` | () => `void` |

###### Returns

`this`

###### Overrides

`Duplex.prependListener`

###### Call Signature

> **prependListener**(`event`: `"error"`, `listener`: (`err`: `Error`) => `void`): `this`

###### Parameters

| Parameter | Type |
| ------ | ------ |
| `event` | `"error"` |
| `listener` | (`err`: `Error`) => `void` |

###### Returns

`this`

###### Overrides

`Duplex.prependListener`

##### prependOnceListener()

###### Call Signature

> **prependOnceListener**(`event`: `string`, `listener`: (...`args`: `any`[]) => `void`): `this`

Adds a **one-time**`listener` function for the event named `eventName` to the _beginning_ of the listeners array.
The next time `eventName` is triggered, this listener is removed, and then invoked.

Returns a reference to the `EventEmitter`, so that calls can be chained.

###### Parameters

| Parameter | Type | Description |
| ------ | ------ | ------ |
| `event` | `string` | - |
| `listener` | (...`args`: `any`[]) => `void` | The callback function |

###### Returns

`this`

###### Overrides

[`DefaultDuplexStream`](stream.md#defaultduplexstream).[`prependOnceListener`](stream.md#prependoncelistener)

###### Call Signature

> **prependOnceListener**(`event`: `"close"`, `listener`: (`hadError`: `boolean`) => `void`): `this`

###### Parameters

| Parameter | Type |
| ------ | ------ |
| `event` | `"close"` |
| `listener` | (`hadError`: `boolean`) => `void` |

###### Returns

`this`

###### Overrides

[`DefaultDuplexStream`](stream.md#defaultduplexstream).[`prependOnceListener`](stream.md#prependoncelistener)

###### Call Signature

> **prependOnceListener**(`event`: `"connect"`, `listener`: () => `void`): `this`

###### Parameters

| Parameter | Type |
| ------ | ------ |
| `event` | `"connect"` |
| `listener` | () => `void` |

###### Returns

`this`

###### Overrides

[`DefaultDuplexStream`](stream.md#defaultduplexstream).[`prependOnceListener`](stream.md#prependoncelistener)

###### Call Signature

> **prependOnceListener**(`event`: `"data"`, `listener`: (`data`: [`Buffer`](buffer.md#buffer)) => `void`): `this`

###### Parameters

| Parameter | Type |
| ------ | ------ |
| `event` | `"data"` |
| `listener` | (`data`: [`Buffer`](buffer.md#buffer)) => `void` |

###### Returns

`this`

###### Overrides

[`DefaultDuplexStream`](stream.md#defaultduplexstream).[`prependOnceListener`](stream.md#prependoncelistener)

###### Call Signature

> **prependOnceListener**(`event`: `"end"`, `listener`: () => `void`): `this`

###### Parameters

| Parameter | Type |
| ------ | ------ |
| `event` | `"end"` |
| `listener` | () => `void` |

###### Returns

`this`

###### Overrides

`Duplex.prependOnceListener`

###### Call Signature

> **prependOnceListener**(`event`: `"error"`, `listener`: (`err`: `Error`) => `void`): `this`

###### Parameters

| Parameter | Type |
| ------ | ------ |
| `event` | `"error"` |
| `listener` | (`err`: `Error`) => `void` |

###### Returns

`this`

###### Overrides

`Duplex.prependOnceListener`

##### read()

> **read**(`size`?: `number`): `null` \| [`Buffer`](buffer.md#buffer)

The `readable.read()` method reads data out of the internal buffer and
returns it. If no data is available to be read, `null` is returned. By default,
the data is returned as a `Buffer` object unless an encoding has been
specified using the `readable.setEncoding()` method or the stream is operating
in object mode.

The optional `size` argument specifies a specific number of bytes to read. If
`size` bytes are not available to be read, `null` will be returned _unless_ the
stream has ended, in which case all of the data remaining in the internal buffer
will be returned.

If the `size` argument is not specified, all of the data contained in the
internal buffer will be returned.

The `size` argument must be less than or equal to 1 GiB.

The `readable.read()` method should only be called on `Readable` streams
operating in paused mode. In flowing mode, `readable.read()` is called
automatically until the internal buffer is fully drained.

```js
const readable = getReadableStreamSomehow();

// 'readable' may be triggered multiple times as data is buffered in
readable.on('readable', () => {
  let chunk;
  console.log('Stream is readable (new data received in buffer)');
  // Use a loop to make sure we read all currently available data
  while (null !== (chunk = readable.read())) {
    console.log(`Read ${chunk.length} bytes of data...`);
  }
});

// 'end' will be triggered once when there is no more data available
readable.on('end', () => {
  console.log('Reached end of stream.');
});
```

Each call to `readable.read()` returns a chunk of data, or `null`. The chunks
are not concatenated. A `while` loop is necessary to consume all data
currently in the buffer. When reading a large file `.read()` may return `null`,
having consumed all buffered content so far, but there is still more data to
come not yet buffered. In this case a new `'readable'` event will be emitted
when there is more data in the buffer. Finally the `'end'` event will be
emitted when there is no more data to come.

Therefore to read a file's whole contents from a `readable`, it is necessary
to collect chunks across multiple `'readable'` events:

```js
const chunks = [];

readable.on('readable', () => {
  let chunk;
  while (null !== (chunk = readable.read())) {
    chunks.push(chunk);
  }
});

readable.on('end', () => {
  const content = chunks.join('');
});
```

A `Readable` stream in object mode will always return a single item from
a call to `readable.read(size)`, regardless of the value of the `size` argument.

If the `readable.read()` method returns a chunk of data, a `'data'` event will
also be emitted.

Calling [read](stream.md#read-2) after the `'end'` event has
been emitted will return `null`. No runtime error will be raised.

###### Parameters

| Parameter | Type | Description |
| ------ | ------ | ------ |
| `size`? | `number` | Optional argument to specify how much data to read. |

###### Returns

`null` \| [`Buffer`](buffer.md#buffer)

###### Inherited from

[`DefaultDuplexStream`](stream.md#defaultduplexstream).[`read`](stream.md#read)

##### removeListener()

###### Call Signature

> **removeListener**(`event`: [`EventKey`](dom-events.md#eventkey), `listener`: (...`args`: `any`[]) => `void`): `this`

Removes the specified `listener` from the listener array for the event named `eventName`.

`removeListener()` will remove, at most, one instance of a listener from the
listener array. If any single listener has been added multiple times to the
listener array for the specified `eventName`, then `removeListener()` must be
called multiple times to remove each instance.

Once an event is emitted, all listeners attached to it at the time of emitting are called in order.
This implies that any `removeListener()` calls _after_ emitting and _before_ the last listener finishes execution
will not remove them from `emit()` in progress. Subsequent events behave as expected.

```js
import { EventEmitter } from 'events';
class MyEmitter extends EventEmitter {}
const myEmitter = new MyEmitter();

const callbackA = () => {
  console.log('A');
  myEmitter.removeListener('event', callbackB);
};

const callbackB = () => {
  console.log('B');
};

myEmitter.on('event', callbackA);

myEmitter.on('event', callbackB);

// callbackA removes listener callbackB but it will still be called.
// Internal listener array at time of emit [callbackA, callbackB]
myEmitter.emit('event');
// Prints:
//   A
//   B

// callbackB is now removed.
// Internal listener array [callbackA]
myEmitter.emit('event');
// Prints:
//   A
```

Because listeners are managed using an internal array, calling this will
change the position indices of any listener registered _after_ the listener
being removed. This will not impact the order in which listeners are called,
but it means that any copies of the listener array as returned by
the `emitter.listeners()` method will need to be recreated.

When a single function has been added as a handler multiple times for a single
event (as in the example below), `removeListener()` will remove the most
recently added instance. In the example the `once('ping')` listener is removed:

```js
import { EventEmitter } from 'events';
const ee = new EventEmitter();

function pong() {
  console.log('pong');
}

ee.on('ping', pong);
ee.once('ping', pong);
ee.removeListener('ping', pong);

ee.emit('ping');
ee.emit('ping');
```

Returns a reference to the `EventEmitter`, so that calls can be chained.

###### Parameters

| Parameter | Type |
| ------ | ------ |
| `event` | [`EventKey`](dom-events.md#eventkey) |
| `listener` | (...`args`: `any`[]) => `void` |

###### Returns

`this`

###### Inherited from

[`DefaultDuplexStream`](stream.md#defaultduplexstream).[`removeListener`](stream.md#removelistener)

###### Call Signature

> **removeListener**(`event`: `"close"`, `listener`: () => `void`): `this`

###### Parameters

| Parameter | Type |
| ------ | ------ |
| `event` | `"close"` |
| `listener` | () => `void` |

###### Returns

`this`

###### Inherited from

[`DefaultDuplexStream`](stream.md#defaultduplexstream).[`removeListener`](stream.md#removelistener)

###### Call Signature

> **removeListener**(`event`: `"error"`, `listener`: (`err`: `Error`) => `void`): `this`

###### Parameters

| Parameter | Type |
| ------ | ------ |
| `event` | `"error"` |
| `listener` | (`err`: `Error`) => `void` |

###### Returns

`this`

###### Inherited from

[`DefaultDuplexStream`](stream.md#defaultduplexstream).[`removeListener`](stream.md#removelistener)

###### Call Signature

> **removeListener**(`event`: `"finish"`, `listener`: () => `void`): `this`

###### Parameters

| Parameter | Type |
| ------ | ------ |
| `event` | `"finish"` |
| `listener` | () => `void` |

###### Returns

`this`

###### Inherited from

[`DefaultDuplexStream`](stream.md#defaultduplexstream).[`removeListener`](stream.md#removelistener)

##### write()

> **write**(`chunk`: `string` \| `ArrayBuffer` \| `SharedArrayBuffer` \| [`ArrayBufferView`](globals/namespaces/QuickJS.md#arraybufferview) \| [`Buffer`](buffer.md#buffer), `callback`?: (`error`?: `null` \| `Error`) => `void`): `void`

The `writable.write()` method writes some data to the stream, and calls the
supplied `callback` once the data has been fully handled. If an error
occurs, the `callback` will be called with the error as its
first argument. The `callback` is usually called asynchronously and before `'error'`
is emitted.

```js
function write(data, cb) {
  if (!stream.write(data)) {
    stream.once('drain', cb);
  } else {
    process.nextTick(cb);
  }
}

// Wait for cb to be called before doing any other write.
write('hello', () => {
  console.log('Write completed, do more writes now.');
});
```

A `Writable` stream in object mode will always ignore the `encoding` argument.

###### Parameters

| Parameter | Type | Description |
| ------ | ------ | ------ |
| `chunk` | `string` \| `ArrayBuffer` \| `SharedArrayBuffer` \| [`ArrayBufferView`](globals/namespaces/QuickJS.md#arraybufferview) \| [`Buffer`](buffer.md#buffer) | Optional data to write. `chunk` must be a {string}, {Buffer}, {TypedArray} or {DataView}. |
| `callback`? | (`error`?: `null` \| `Error`) => `void` | Callback for when this chunk of data is flushed. |

###### Returns

`void`

`false` if the stream wishes for the calling code to wait for the `'drain'` event to be emitted before continuing to write additional data; otherwise `true`.

###### Since

v0.9.4

###### Inherited from

[`DefaultDuplexStream`](stream.md#defaultduplexstream).[`write`](stream.md#write)

## Interfaces

### AddressInfo

#### Properties

##### address

> **address**: `string`

##### family

> **family**: `string`

##### port

> **port**: `number`

***

### IpcSocketConnectOpts

#### Properties

##### path

> **path**: `string`

***

### ListenOptions

#### Properties

##### backlog?

> `optional` **backlog**: `number`

##### host?

> `optional` **host**: `string`

##### path?

> `optional` **path**: `string`

##### port?

> `optional` **port**: `number`

***

### ServerOpts

#### Properties

##### allowHalfOpen?

> `optional` **allowHalfOpen**: `boolean`

Indicates whether half-opened TCP connections are allowed.

###### Default

```ts
false
```

***

### SocketConstructorOpts

#### Properties

##### allowHalfOpen?

> `optional` **allowHalfOpen**: `boolean`

***

### TcpSocketConnectOpts

#### Properties

##### host?

> `optional` **host**: `string`

##### port

> **port**: `number`

## Type Aliases

### NetConnectOpts

> **NetConnectOpts**: [`TcpSocketConnectOpts`](net.md#tcpsocketconnectopts) \| [`IpcSocketConnectOpts`](net.md#ipcsocketconnectopts)

***

### SocketConnectOpts

> **SocketConnectOpts**: [`TcpSocketConnectOpts`](net.md#tcpsocketconnectopts) \| [`IpcSocketConnectOpts`](net.md#ipcsocketconnectopts)

***

### SocketReadyState

> **SocketReadyState**: `"opening"` \| `"open"` \| `"readOnly"` \| `"writeOnly"` \| `"closed"`

## Functions

### connect()

#### Call Signature

> **connect**(`options`: [`NetConnectOpts`](net.md#netconnectopts), `connectionListener`?: () => `void`): [`Socket`](net.md#socket)

Aliases to [createConnection](net.md#createconnection).

Possible signatures:

* [connect](net.md#connect-1)
* [connect](net.md#connect-1) for `IPC` connections.
* [connect](net.md#connect-1) for TCP connections.

##### Parameters

| Parameter | Type |
| ------ | ------ |
| `options` | [`NetConnectOpts`](net.md#netconnectopts) |
| `connectionListener`? | () => `void` |

##### Returns

[`Socket`](net.md#socket)

#### Call Signature

> **connect**(`port`: `number`, `host`: `string`, `connectionListener`?: () => `void`): [`Socket`](net.md#socket)

Aliases to [createConnection](net.md#createconnection).

Possible signatures:

* [connect](net.md#connect-1)
* [connect](net.md#connect-1) for `IPC` connections.
* [connect](net.md#connect-1) for TCP connections.

##### Parameters

| Parameter | Type |
| ------ | ------ |
| `port` | `number` |
| `host` | `string` |
| `connectionListener`? | () => `void` |

##### Returns

[`Socket`](net.md#socket)

#### Call Signature

> **connect**(`port`: `number`, `connectionListener`?: () => `void`): [`Socket`](net.md#socket)

Aliases to [createConnection](net.md#createconnection).

Possible signatures:

* [connect](net.md#connect-1)
* [connect](net.md#connect-1) for `IPC` connections.
* [connect](net.md#connect-1) for TCP connections.

##### Parameters

| Parameter | Type |
| ------ | ------ |
| `port` | `number` |
| `connectionListener`? | () => `void` |

##### Returns

[`Socket`](net.md#socket)

#### Call Signature

> **connect**(`path`: `string`, `connectionListener`?: () => `void`): [`Socket`](net.md#socket)

Aliases to [createConnection](net.md#createconnection).

Possible signatures:

* [connect](net.md#connect-1)
* [connect](net.md#connect-1) for `IPC` connections.
* [connect](net.md#connect-1) for TCP connections.

##### Parameters

| Parameter | Type |
| ------ | ------ |
| `path` | `string` |
| `connectionListener`? | () => `void` |

##### Returns

[`Socket`](net.md#socket)

***

### createConnection()

#### Call Signature

> **createConnection**(`options`: [`NetConnectOpts`](net.md#netconnectopts), `connectionListener`?: () => `void`): [`Socket`](net.md#socket)

A factory function, which creates a new [Socket](net.md#socket),
immediately initiates connection with `socket.connect()`,
then returns the `net.Socket` that starts the connection.

When the connection is established, a `'connect'` event will be emitted
on the returned socket. The last parameter `connectListener`, if supplied,
will be added as a listener for the `'connect'` event **once**.

Possible signatures:

* [createConnection](net.md#createconnection)
* [createConnection](net.md#createconnection) for `IPC` connections.
* [createConnection](net.md#createconnection) for TCP connections.

The [connect](net.md#connect-1) function is an alias to this function.

##### Parameters

| Parameter | Type |
| ------ | ------ |
| `options` | [`NetConnectOpts`](net.md#netconnectopts) |
| `connectionListener`? | () => `void` |

##### Returns

[`Socket`](net.md#socket)

#### Call Signature

> **createConnection**(`port`: `number`, `host`: `string`, `connectionListener`?: () => `void`): [`Socket`](net.md#socket)

A factory function, which creates a new [Socket](net.md#socket),
immediately initiates connection with `socket.connect()`,
then returns the `net.Socket` that starts the connection.

When the connection is established, a `'connect'` event will be emitted
on the returned socket. The last parameter `connectListener`, if supplied,
will be added as a listener for the `'connect'` event **once**.

Possible signatures:

* [createConnection](net.md#createconnection)
* [createConnection](net.md#createconnection) for `IPC` connections.
* [createConnection](net.md#createconnection) for TCP connections.

The [connect](net.md#connect-1) function is an alias to this function.

##### Parameters

| Parameter | Type |
| ------ | ------ |
| `port` | `number` |
| `host` | `string` |
| `connectionListener`? | () => `void` |

##### Returns

[`Socket`](net.md#socket)

#### Call Signature

> **createConnection**(`port`: `number`, `connectionListener`?: () => `void`): [`Socket`](net.md#socket)

A factory function, which creates a new [Socket](net.md#socket),
immediately initiates connection with `socket.connect()`,
then returns the `net.Socket` that starts the connection.

When the connection is established, a `'connect'` event will be emitted
on the returned socket. The last parameter `connectListener`, if supplied,
will be added as a listener for the `'connect'` event **once**.

Possible signatures:

* [createConnection](net.md#createconnection)
* [createConnection](net.md#createconnection) for `IPC` connections.
* [createConnection](net.md#createconnection) for TCP connections.

The [connect](net.md#connect-1) function is an alias to this function.

##### Parameters

| Parameter | Type |
| ------ | ------ |
| `port` | `number` |
| `connectionListener`? | () => `void` |

##### Returns

[`Socket`](net.md#socket)

#### Call Signature

> **createConnection**(`path`: `string`, `connectionListener`?: () => `void`): [`Socket`](net.md#socket)

A factory function, which creates a new [Socket](net.md#socket),
immediately initiates connection with `socket.connect()`,
then returns the `net.Socket` that starts the connection.

When the connection is established, a `'connect'` event will be emitted
on the returned socket. The last parameter `connectListener`, if supplied,
will be added as a listener for the `'connect'` event **once**.

Possible signatures:

* [createConnection](net.md#createconnection)
* [createConnection](net.md#createconnection) for `IPC` connections.
* [createConnection](net.md#createconnection) for TCP connections.

The [connect](net.md#connect-1) function is an alias to this function.

##### Parameters

| Parameter | Type |
| ------ | ------ |
| `path` | `string` |
| `connectionListener`? | () => `void` |

##### Returns

[`Socket`](net.md#socket)

***

### createServer()

#### Call Signature

> **createServer**(`connectionListener`?: (`socket`: [`Socket`](net.md#socket)) => `void`): [`Server`](net.md#server)

Creates a new TCP or `IPC` server.

If `allowHalfOpen` is set to `true`, when the other end of the socket
signals the end of transmission, the server will only send back the end of
transmission when `socket.end()` is explicitly called. For example, in the
context of TCP, when a FIN packed is received, a FIN packed is sent
back only when `socket.end()` is explicitly called. Until then the
connection is half-closed (non-readable but still writable). See `'end'` event and [RFC 1122](https://tools.ietf.org/html/rfc1122) (section 4.2.2.13) for more information.

If `pauseOnConnect` is set to `true`, then the socket associated with each
incoming connection will be paused, and no data will be read from its handle.
This allows connections to be passed between processes without any data being
read by the original process. To begin reading data from a paused socket, call `socket.resume()`.

The server can be a TCP server or an `IPC` server, depending on what it `listen()` to.

Here is an example of a TCP echo server which listens for connections
on port 8124:

```js
import * as net from 'net';
const server = net.createServer((c) => {
  // 'connection' listener.
  console.log('client connected');
  c.on('end', () => {
    console.log('client disconnected');
  });
  c.write('hello\r\n');

});
server.on('error', (err) => {
  throw err;
});
server.listen(8124, () => {
  console.log('server bound');
});
```

Test this by using `telnet`:

```bash
telnet localhost 8124
```

To listen on the socket `/tmp/echo.sock`:

```js
server.listen('/tmp/echo.sock', () => {
  console.log('server bound');
});
```

Use `nc` to connect to a Unix domain socket server:

```bash
nc -U /tmp/echo.sock
```

##### Parameters

| Parameter | Type | Description |
| ------ | ------ | ------ |
| `connectionListener`? | (`socket`: [`Socket`](net.md#socket)) => `void` | Automatically set as a listener for the 'connection' event. |

##### Returns

[`Server`](net.md#server)

#### Call Signature

> **createServer**(`options`?: [`ServerOpts`](net.md#serveropts), `connectionListener`?: (`socket`: [`Socket`](net.md#socket)) => `void`): [`Server`](net.md#server)

Creates a new TCP or `IPC` server.

If `allowHalfOpen` is set to `true`, when the other end of the socket
signals the end of transmission, the server will only send back the end of
transmission when `socket.end()` is explicitly called. For example, in the
context of TCP, when a FIN packed is received, a FIN packed is sent
back only when `socket.end()` is explicitly called. Until then the
connection is half-closed (non-readable but still writable). See `'end'` event and [RFC 1122](https://tools.ietf.org/html/rfc1122) (section 4.2.2.13) for more information.

If `pauseOnConnect` is set to `true`, then the socket associated with each
incoming connection will be paused, and no data will be read from its handle.
This allows connections to be passed between processes without any data being
read by the original process. To begin reading data from a paused socket, call `socket.resume()`.

The server can be a TCP server or an `IPC` server, depending on what it `listen()` to.

Here is an example of a TCP echo server which listens for connections
on port 8124:

```js
import * as net from 'net';
const server = net.createServer((c) => {
  // 'connection' listener.
  console.log('client connected');
  c.on('end', () => {
    console.log('client disconnected');
  });
  c.write('hello\r\n');

});
server.on('error', (err) => {
  throw err;
});
server.listen(8124, () => {
  console.log('server bound');
});
```

Test this by using `telnet`:

```bash
telnet localhost 8124
```

To listen on the socket `/tmp/echo.sock`:

```js
server.listen('/tmp/echo.sock', () => {
  console.log('server bound');
});
```

Use `nc` to connect to a Unix domain socket server:

```bash
nc -U /tmp/echo.sock
```

##### Parameters

| Parameter | Type | Description |
| ------ | ------ | ------ |
| `options`? | [`ServerOpts`](net.md#serveropts) | - |
| `connectionListener`? | (`socket`: [`Socket`](net.md#socket)) => `void` | Automatically set as a listener for the 'connection' event. |

##### Returns

[`Server`](net.md#server)



================================================
FILE: src/reference/modules/llrt/process.md
================================================
[@caido/quickjs-types](../index.md) / [llrt/process](process.md) / process

# process



================================================
FILE: src/reference/modules/llrt/stream.md
================================================
[@caido/quickjs-types](../index.md) / [llrt/stream](stream.md) / stream

# stream

## Classes

### DefaultDuplexStream

#### Extends

- [`DefaultReadableStream`](stream.md#defaultreadablestream)

#### Extended by

- [`Socket`](net.md#socket)

#### Implements

- [`DefaultWritableStream`](stream.md#defaultwritablestream)

#### Constructors

##### new DefaultDuplexStream()

> **new DefaultDuplexStream**(): [`DefaultDuplexStream`](stream.md#defaultduplexstream)

###### Returns

[`DefaultDuplexStream`](stream.md#defaultduplexstream)

###### Inherited from

[`DefaultReadableStream`](stream.md#defaultreadablestream).[`constructor`](stream.md#constructors-1)

#### Methods

##### \[dispose\]()

> **\[dispose\]**(): `void`

Calls `readable.destroy()`.

###### Returns

`void`

###### Inherited from

[`DefaultReadableStream`](stream.md#defaultreadablestream).[`[dispose]`](stream.md#dispose-1)

##### addListener()

###### Call Signature

> **addListener**(`event`: [`EventKey`](dom-events.md#eventkey), `listener`: (...`args`: `any`[]) => `void`): `this`

Event emitter
The defined events on documents including:
1. close
2. error
3. finish

###### Parameters

| Parameter | Type |
| ------ | ------ |
| `event` | [`EventKey`](dom-events.md#eventkey) |
| `listener` | (...`args`: `any`[]) => `void` |

###### Returns

`this`

###### Implementation of

[`DefaultWritableStream`](stream.md#defaultwritablestream).[`addListener`](stream.md#addlistener-2)

###### Overrides

[`DefaultReadableStream`](stream.md#defaultreadablestream).[`addListener`](stream.md#addlistener-1)

###### Call Signature

> **addListener**(`event`: `"close"`, `listener`: () => `void`): `this`

Event emitter
The defined events on documents including:
1. close
2. error
3. finish

###### Parameters

| Parameter | Type |
| ------ | ------ |
| `event` | `"close"` |
| `listener` | () => `void` |

###### Returns

`this`

###### Implementation of

[`DefaultWritableStream`](stream.md#defaultwritablestream).[`addListener`](stream.md#addlistener-2)

###### Overrides

[`DefaultReadableStream`](stream.md#defaultreadablestream).[`addListener`](stream.md#addlistener-1)

###### Call Signature

> **addListener**(`event`: `"error"`, `listener`: (`err`: `Error`) => `void`): `this`

Event emitter
The defined events on documents including:
1. close
2. error
3. finish

###### Parameters

| Parameter | Type |
| ------ | ------ |
| `event` | `"error"` |
| `listener` | (`err`: `Error`) => `void` |

###### Returns

`this`

###### Implementation of

[`DefaultWritableStream`](stream.md#defaultwritablestream).[`addListener`](stream.md#addlistener-2)

###### Overrides

[`DefaultReadableStream`](stream.md#defaultreadablestream).[`addListener`](stream.md#addlistener-1)

###### Call Signature

> **addListener**(`event`: `"finish"`, `listener`: () => `void`): `this`

Event emitter
The defined events on documents including:
1. close
2. error
3. finish

###### Parameters

| Parameter | Type |
| ------ | ------ |
| `event` | `"finish"` |
| `listener` | () => `void` |

###### Returns

`this`

###### Implementation of

[`DefaultWritableStream`](stream.md#defaultwritablestream).[`addListener`](stream.md#addlistener-2)

###### Overrides

[`DefaultReadableStream`](stream.md#defaultreadablestream).[`addListener`](stream.md#addlistener-1)

##### destroy()

> **destroy**(`error`?: `Error`): `this`

Destroy the stream. Optionally emit an `'error'` event, and emit a `'close'` event. After this call, the readable
stream will release any internal resources and subsequent calls to `push()` will be ignored.

Once `destroy()` has been called any further calls will be a no-op and no
further errors except from `_destroy()` may be emitted as `'error'`.

Implementors should not override this method, but instead implement `readable._destroy()`.

###### Parameters

| Parameter | Type | Description |
| ------ | ------ | ------ |
| `error`? | `Error` | Error which will be passed as payload in `'error'` event |

###### Returns

`this`

###### Inherited from

[`DefaultReadableStream`](stream.md#defaultreadablestream).[`destroy`](stream.md#destroy-1)

##### emit()

###### Call Signature

> **emit**(`event`: [`EventKey`](dom-events.md#eventkey), ...`args`: `any`[]): `boolean`

Synchronously calls each of the listeners registered for the event named `eventName`, in the order they were registered, passing the supplied arguments
to each.

```js
import { EventEmitter } from 'events';
const myEmitter = new EventEmitter();

// First listener
myEmitter.on('event', function firstListener() {
  console.log('Helloooo! first listener');
});
// Second listener
myEmitter.on('event', function secondListener(arg1, arg2) {
  console.log(`event with parameters ${arg1}, ${arg2} in second listener`);
});
// Third listener
myEmitter.on('event', function thirdListener(...args) {
  const parameters = args.join(', ');
  console.log(`event with parameters ${parameters} in third listener`);
});

myEmitter.emit('event', 1, 2, 3, 4, 5);

// Prints:
// Helloooo! first listener
// event with parameters 1, 2 in second listener
// event with parameters 1, 2, 3, 4, 5 in third listener
```

###### Parameters

| Parameter | Type |
| ------ | ------ |
| `event` | [`EventKey`](dom-events.md#eventkey) |
| ...`args` | `any`[] |

###### Returns

`boolean`

###### Implementation of

[`DefaultWritableStream`](stream.md#defaultwritablestream).[`emit`](stream.md#emit-2)

###### Overrides

[`DefaultReadableStream`](stream.md#defaultreadablestream).[`emit`](stream.md#emit-1)

###### Call Signature

> **emit**(`event`: `"close"`): `boolean`

###### Parameters

| Parameter | Type |
| ------ | ------ |
| `event` | `"close"` |

###### Returns

`boolean`

###### Implementation of

[`DefaultWritableStream`](stream.md#defaultwritablestream).[`emit`](stream.md#emit-2)

###### Overrides

[`DefaultReadableStream`](stream.md#defaultreadablestream).[`emit`](stream.md#emit-1)

###### Call Signature

> **emit**(`event`: `"error"`, `err`: `Error`): `boolean`

###### Parameters

| Parameter | Type |
| ------ | ------ |
| `event` | `"error"` |
| `err` | `Error` |

###### Returns

`boolean`

###### Implementation of

[`DefaultWritableStream`](stream.md#defaultwritablestream).[`emit`](stream.md#emit-2)

###### Overrides

[`DefaultReadableStream`](stream.md#defaultreadablestream).[`emit`](stream.md#emit-1)

###### Call Signature

> **emit**(`event`: `"finish"`): `boolean`

###### Parameters

| Parameter | Type |
| ------ | ------ |
| `event` | `"finish"` |

###### Returns

`boolean`

###### Implementation of

[`DefaultWritableStream`](stream.md#defaultwritablestream).[`emit`](stream.md#emit-2)

###### Overrides

[`DefaultReadableStream`](stream.md#defaultreadablestream).[`emit`](stream.md#emit-1)

##### end()

> **end**(): `this`

Calling the `writable.end()` method signals that no more data will be written
to the `Writable`.

Calling the [write](stream.md#write) method after calling [end](stream.md#end) will raise an error.

###### Returns

`this`

###### Implementation of

[`DefaultWritableStream`](stream.md#defaultwritablestream).[`end`](stream.md#end-1)

##### eventNames()

> **eventNames**(): [`EventKey`](dom-events.md#eventkey)[]

Returns an array listing the events for which the emitter has registered
listeners. The values in the array are strings or `Symbol`s.

```js
import { EventEmitter } from 'events';

const myEE = new EventEmitter();
myEE.on('foo', () => {});
myEE.on('bar', () => {});

const sym = Symbol('symbol');
myEE.on(sym, () => {});

console.log(myEE.eventNames());
// Prints: [ 'foo', 'bar', Symbol(symbol) ]
```

###### Returns

[`EventKey`](dom-events.md#eventkey)[]

###### Implementation of

[`DefaultWritableStream`](stream.md#defaultwritablestream).[`eventNames`](stream.md#eventnames-2)

###### Inherited from

[`DefaultReadableStream`](stream.md#defaultreadablestream).[`eventNames`](stream.md#eventnames-1)

##### off()

> **off**\<`K`\>(`eventName`: [`EventKey`](dom-events.md#eventkey), `listener`: (...`args`: `any`[]) => `void`): `this`

Alias for `emitter.removeListener()`.

###### Type Parameters

| Type Parameter |
| ------ |
| `K` |

###### Parameters

| Parameter | Type |
| ------ | ------ |
| `eventName` | [`EventKey`](dom-events.md#eventkey) |
| `listener` | (...`args`: `any`[]) => `void` |

###### Returns

`this`

###### Implementation of

[`DefaultWritableStream`](stream.md#defaultwritablestream).[`off`](stream.md#off-2)

###### Inherited from

[`DefaultReadableStream`](stream.md#defaultreadablestream).[`off`](stream.md#off-1)

##### on()

###### Call Signature

> **on**(`event`: [`EventKey`](dom-events.md#eventkey), `listener`: (...`args`: `any`[]) => `void`): `this`

Adds the `listener` function to the end of the listeners array for the event
named `eventName`. No checks are made to see if the `listener` has already
been added. Multiple calls passing the same combination of `eventName` and
`listener` will result in the `listener` being added, and called, multiple times.

```js
server.on('connection', (stream) => {
  console.log('someone connected!');
});
```

Returns a reference to the `EventEmitter`, so that calls can be chained.

By default, event listeners are invoked in the order they are added. The `emitter.prependListener()` method can be used as an alternative to add the
event listener to the beginning of the listeners array.

```js
import { EventEmitter } from 'events';
const myEE = new EventEmitter();
myEE.on('foo', () => console.log('a'));
myEE.prependListener('foo', () => console.log('b'));
myEE.emit('foo');
// Prints:
//   b
//   a
```

###### Parameters

| Parameter | Type | Description |
| ------ | ------ | ------ |
| `event` | [`EventKey`](dom-events.md#eventkey) | - |
| `listener` | (...`args`: `any`[]) => `void` | The callback function |

###### Returns

`this`

###### Implementation of

[`DefaultWritableStream`](stream.md#defaultwritablestream).[`on`](stream.md#on-2)

###### Overrides

[`DefaultReadableStream`](stream.md#defaultreadablestream).[`on`](stream.md#on-1)

###### Call Signature

> **on**(`event`: `"close"`, `listener`: () => `void`): `this`

###### Parameters

| Parameter | Type |
| ------ | ------ |
| `event` | `"close"` |
| `listener` | () => `void` |

###### Returns

`this`

###### Implementation of

[`DefaultWritableStream`](stream.md#defaultwritablestream).[`on`](stream.md#on-2)

###### Overrides

[`DefaultReadableStream`](stream.md#defaultreadablestream).[`on`](stream.md#on-1)

###### Call Signature

> **on**(`event`: `"error"`, `listener`: (`err`: `Error`) => `void`): `this`

###### Parameters

| Parameter | Type |
| ------ | ------ |
| `event` | `"error"` |
| `listener` | (`err`: `Error`) => `void` |

###### Returns

`this`

###### Implementation of

[`DefaultWritableStream`](stream.md#defaultwritablestream).[`on`](stream.md#on-2)

###### Overrides

[`DefaultReadableStream`](stream.md#defaultreadablestream).[`on`](stream.md#on-1)

###### Call Signature

> **on**(`event`: `"finish"`, `listener`: () => `void`): `this`

###### Parameters

| Parameter | Type |
| ------ | ------ |
| `event` | `"finish"` |
| `listener` | () => `void` |

###### Returns

`this`

###### Implementation of

[`DefaultWritableStream`](stream.md#defaultwritablestream).[`on`](stream.md#on-2)

###### Overrides

[`DefaultReadableStream`](stream.md#defaultreadablestream).[`on`](stream.md#on-1)

##### once()

###### Call Signature

> **once**(`event`: [`EventKey`](dom-events.md#eventkey), `listener`: (...`args`: `any`[]) => `void`): `this`

Adds a **one-time** `listener` function for the event named `eventName`. The
next time `eventName` is triggered, this listener is removed and then invoked.

Returns a reference to the `EventEmitter`, so that calls can be chained.

By default, event listeners are invoked in the order they are added. The `emitter.prependOnceListener()` method can be used as an alternative to add the
event listener to the beginning of the listeners array.

```js
import { EventEmitter } from 'events';
const myEE = new EventEmitter();
myEE.once('foo', () => console.log('a'));
myEE.prependOnceListener('foo', () => console.log('b'));
myEE.emit('foo');
// Prints:
//   b
//   a
```

###### Parameters

| Parameter | Type | Description |
| ------ | ------ | ------ |
| `event` | [`EventKey`](dom-events.md#eventkey) | - |
| `listener` | (...`args`: `any`[]) => `void` | The callback function |

###### Returns

`this`

###### Since

v0.3.0

###### Implementation of

[`DefaultWritableStream`](stream.md#defaultwritablestream).[`once`](stream.md#once-2)

###### Overrides

[`DefaultReadableStream`](stream.md#defaultreadablestream).[`once`](stream.md#once-1)

###### Call Signature

> **once**(`event`: `"close"`, `listener`: () => `void`): `this`

###### Parameters

| Parameter | Type |
| ------ | ------ |
| `event` | `"close"` |
| `listener` | () => `void` |

###### Returns

`this`

###### Implementation of

[`DefaultWritableStream`](stream.md#defaultwritablestream).[`once`](stream.md#once-2)

###### Overrides

[`DefaultReadableStream`](stream.md#defaultreadablestream).[`once`](stream.md#once-1)

###### Call Signature

> **once**(`event`: `"error"`, `listener`: (`err`: `Error`) => `void`): `this`

###### Parameters

| Parameter | Type |
| ------ | ------ |
| `event` | `"error"` |
| `listener` | (`err`: `Error`) => `void` |

###### Returns

`this`

###### Implementation of

[`DefaultWritableStream`](stream.md#defaultwritablestream).[`once`](stream.md#once-2)

###### Overrides

[`DefaultReadableStream`](stream.md#defaultreadablestream).[`once`](stream.md#once-1)

###### Call Signature

> **once**(`event`: `"finish"`, `listener`: () => `void`): `this`

###### Parameters

| Parameter | Type |
| ------ | ------ |
| `event` | `"finish"` |
| `listener` | () => `void` |

###### Returns

`this`

###### Implementation of

[`DefaultWritableStream`](stream.md#defaultwritablestream).[`once`](stream.md#once-2)

###### Overrides

[`DefaultReadableStream`](stream.md#defaultreadablestream).[`once`](stream.md#once-1)

##### prependListener()

###### Call Signature

> **prependListener**(`event`: [`EventKey`](dom-events.md#eventkey), `listener`: (...`args`: `any`[]) => `void`): `this`

Adds the `listener` function to the _beginning_ of the listeners array for the
event named `eventName`. No checks are made to see if the `listener` has
already been added. Multiple calls passing the same combination of `eventName`
and `listener` will result in the `listener` being added, and called, multiple times.

Returns a reference to the `EventEmitter`, so that calls can be chained.

###### Parameters

| Parameter | Type | Description |
| ------ | ------ | ------ |
| `event` | [`EventKey`](dom-events.md#eventkey) | - |
| `listener` | (...`args`: `any`[]) => `void` | The callback function |

###### Returns

`this`

###### Implementation of

[`DefaultWritableStream`](stream.md#defaultwritablestream).[`prependListener`](stream.md#prependlistener-2)

###### Overrides

[`DefaultReadableStream`](stream.md#defaultreadablestream).[`prependListener`](stream.md#prependlistener-1)

###### Call Signature

> **prependListener**(`event`: `"close"`, `listener`: () => `void`): `this`

###### Parameters

| Parameter | Type |
| ------ | ------ |
| `event` | `"close"` |
| `listener` | () => `void` |

###### Returns

`this`

###### Implementation of

[`DefaultWritableStream`](stream.md#defaultwritablestream).[`prependListener`](stream.md#prependlistener-2)

###### Overrides

[`DefaultReadableStream`](stream.md#defaultreadablestream).[`prependListener`](stream.md#prependlistener-1)

###### Call Signature

> **prependListener**(`event`: `"error"`, `listener`: (`err`: `Error`) => `void`): `this`

###### Parameters

| Parameter | Type |
| ------ | ------ |
| `event` | `"error"` |
| `listener` | (`err`: `Error`) => `void` |

###### Returns

`this`

###### Implementation of

[`DefaultWritableStream`](stream.md#defaultwritablestream).[`prependListener`](stream.md#prependlistener-2)

###### Overrides

[`DefaultReadableStream`](stream.md#defaultreadablestream).[`prependListener`](stream.md#prependlistener-1)

###### Call Signature

> **prependListener**(`event`: `"finish"`, `listener`: () => `void`): `this`

###### Parameters

| Parameter | Type |
| ------ | ------ |
| `event` | `"finish"` |
| `listener` | () => `void` |

###### Returns

`this`

###### Implementation of

[`DefaultWritableStream`](stream.md#defaultwritablestream).[`prependListener`](stream.md#prependlistener-2)

###### Overrides

[`DefaultReadableStream`](stream.md#defaultreadablestream).[`prependListener`](stream.md#prependlistener-1)

##### prependOnceListener()

###### Call Signature

> **prependOnceListener**(`event`: [`EventKey`](dom-events.md#eventkey), `listener`: (...`args`: `any`[]) => `void`): `this`

Adds a **one-time**`listener` function for the event named `eventName` to the _beginning_ of the listeners array.
The next time `eventName` is triggered, this listener is removed, and then invoked.

Returns a reference to the `EventEmitter`, so that calls can be chained.

###### Parameters

| Parameter | Type | Description |
| ------ | ------ | ------ |
| `event` | [`EventKey`](dom-events.md#eventkey) | - |
| `listener` | (...`args`: `any`[]) => `void` | The callback function |

###### Returns

`this`

###### Implementation of

[`DefaultWritableStream`](stream.md#defaultwritablestream).[`prependOnceListener`](stream.md#prependoncelistener-2)

###### Overrides

[`DefaultReadableStream`](stream.md#defaultreadablestream).[`prependOnceListener`](stream.md#prependoncelistener-1)

###### Call Signature

> **prependOnceListener**(`event`: `"close"`, `listener`: () => `void`): `this`

###### Parameters

| Parameter | Type |
| ------ | ------ |
| `event` | `"close"` |
| `listener` | () => `void` |

###### Returns

`this`

###### Implementation of

[`DefaultWritableStream`](stream.md#defaultwritablestream).[`prependOnceListener`](stream.md#prependoncelistener-2)

###### Overrides

[`DefaultReadableStream`](stream.md#defaultreadablestream).[`prependOnceListener`](stream.md#prependoncelistener-1)

###### Call Signature

> **prependOnceListener**(`event`: `"error"`, `listener`: (`err`: `Error`) => `void`): `this`

###### Parameters

| Parameter | Type |
| ------ | ------ |
| `event` | `"error"` |
| `listener` | (`err`: `Error`) => `void` |

###### Returns

`this`

###### Implementation of

[`DefaultWritableStream`](stream.md#defaultwritablestream).[`prependOnceListener`](stream.md#prependoncelistener-2)

###### Overrides

[`DefaultReadableStream`](stream.md#defaultreadablestream).[`prependOnceListener`](stream.md#prependoncelistener-1)

###### Call Signature

> **prependOnceListener**(`event`: `"finish"`, `listener`: () => `void`): `this`

###### Parameters

| Parameter | Type |
| ------ | ------ |
| `event` | `"finish"` |
| `listener` | () => `void` |

###### Returns

`this`

###### Implementation of

[`DefaultWritableStream`](stream.md#defaultwritablestream).[`prependOnceListener`](stream.md#prependoncelistener-2)

###### Overrides

[`DefaultReadableStream`](stream.md#defaultreadablestream).[`prependOnceListener`](stream.md#prependoncelistener-1)

##### read()

> **read**(`size`?: `number`): `null` \| [`Buffer`](buffer.md#buffer)

The `readable.read()` method reads data out of the internal buffer and
returns it. If no data is available to be read, `null` is returned. By default,
the data is returned as a `Buffer` object unless an encoding has been
specified using the `readable.setEncoding()` method or the stream is operating
in object mode.

The optional `size` argument specifies a specific number of bytes to read. If
`size` bytes are not available to be read, `null` will be returned _unless_ the
stream has ended, in which case all of the data remaining in the internal buffer
will be returned.

If the `size` argument is not specified, all of the data contained in the
internal buffer will be returned.

The `size` argument must be less than or equal to 1 GiB.

The `readable.read()` method should only be called on `Readable` streams
operating in paused mode. In flowing mode, `readable.read()` is called
automatically until the internal buffer is fully drained.

```js
const readable = getReadableStreamSomehow();

// 'readable' may be triggered multiple times as data is buffered in
readable.on('readable', () => {
  let chunk;
  console.log('Stream is readable (new data received in buffer)');
  // Use a loop to make sure we read all currently available data
  while (null !== (chunk = readable.read())) {
    console.log(`Read ${chunk.length} bytes of data...`);
  }
});

// 'end' will be triggered once when there is no more data available
readable.on('end', () => {
  console.log('Reached end of stream.');
});
```

Each call to `readable.read()` returns a chunk of data, or `null`. The chunks
are not concatenated. A `while` loop is necessary to consume all data
currently in the buffer. When reading a large file `.read()` may return `null`,
having consumed all buffered content so far, but there is still more data to
come not yet buffered. In this case a new `'readable'` event will be emitted
when there is more data in the buffer. Finally the `'end'` event will be
emitted when there is no more data to come.

Therefore to read a file's whole contents from a `readable`, it is necessary
to collect chunks across multiple `'readable'` events:

```js
const chunks = [];

readable.on('readable', () => {
  let chunk;
  while (null !== (chunk = readable.read())) {
    chunks.push(chunk);
  }
});

readable.on('end', () => {
  const content = chunks.join('');
});
```

A `Readable` stream in object mode will always return a single item from
a call to `readable.read(size)`, regardless of the value of the `size` argument.

If the `readable.read()` method returns a chunk of data, a `'data'` event will
also be emitted.

Calling [read](stream.md#read-2) after the `'end'` event has
been emitted will return `null`. No runtime error will be raised.

###### Parameters

| Parameter | Type | Description |
| ------ | ------ | ------ |
| `size`? | `number` | Optional argument to specify how much data to read. |

###### Returns

`null` \| [`Buffer`](buffer.md#buffer)

###### Inherited from

[`DefaultReadableStream`](stream.md#defaultreadablestream).[`read`](stream.md#read-1)

##### removeListener()

###### Call Signature

> **removeListener**(`event`: [`EventKey`](dom-events.md#eventkey), `listener`: (...`args`: `any`[]) => `void`): `this`

Removes the specified `listener` from the listener array for the event named `eventName`.

`removeListener()` will remove, at most, one instance of a listener from the
listener array. If any single listener has been added multiple times to the
listener array for the specified `eventName`, then `removeListener()` must be
called multiple times to remove each instance.

Once an event is emitted, all listeners attached to it at the time of emitting are called in order.
This implies that any `removeListener()` calls _after_ emitting and _before_ the last listener finishes execution
will not remove them from `emit()` in progress. Subsequent events behave as expected.

```js
import { EventEmitter } from 'events';
class MyEmitter extends EventEmitter {}
const myEmitter = new MyEmitter();

const callbackA = () => {
  console.log('A');
  myEmitter.removeListener('event', callbackB);
};

const callbackB = () => {
  console.log('B');
};

myEmitter.on('event', callbackA);

myEmitter.on('event', callbackB);

// callbackA removes listener callbackB but it will still be called.
// Internal listener array at time of emit [callbackA, callbackB]
myEmitter.emit('event');
// Prints:
//   A
//   B

// callbackB is now removed.
// Internal listener array [callbackA]
myEmitter.emit('event');
// Prints:
//   A
```

Because listeners are managed using an internal array, calling this will
change the position indices of any listener registered _after_ the listener
being removed. This will not impact the order in which listeners are called,
but it means that any copies of the listener array as returned by
the `emitter.listeners()` method will need to be recreated.

When a single function has been added as a handler multiple times for a single
event (as in the example below), `removeListener()` will remove the most
recently added instance. In the example the `once('ping')` listener is removed:

```js
import { EventEmitter } from 'events';
const ee = new EventEmitter();

function pong() {
  console.log('pong');
}

ee.on('ping', pong);
ee.once('ping', pong);
ee.removeListener('ping', pong);

ee.emit('ping');
ee.emit('ping');
```

Returns a reference to the `EventEmitter`, so that calls can be chained.

###### Parameters

| Parameter | Type |
| ------ | ------ |
| `event` | [`EventKey`](dom-events.md#eventkey) |
| `listener` | (...`args`: `any`[]) => `void` |

###### Returns

`this`

###### Implementation of

[`DefaultWritableStream`](stream.md#defaultwritablestream).[`removeListener`](stream.md#removelistener-2)

###### Overrides

[`DefaultReadableStream`](stream.md#defaultreadablestream).[`removeListener`](stream.md#removelistener-1)

###### Call Signature

> **removeListener**(`event`: `"close"`, `listener`: () => `void`): `this`

###### Parameters

| Parameter | Type |
| ------ | ------ |
| `event` | `"close"` |
| `listener` | () => `void` |

###### Returns

`this`

###### Implementation of

[`DefaultWritableStream`](stream.md#defaultwritablestream).[`removeListener`](stream.md#removelistener-2)

###### Overrides

[`DefaultReadableStream`](stream.md#defaultreadablestream).[`removeListener`](stream.md#removelistener-1)

###### Call Signature

> **removeListener**(`event`: `"error"`, `listener`: (`err`: `Error`) => `void`): `this`

###### Parameters

| Parameter | Type |
| ------ | ------ |
| `event` | `"error"` |
| `listener` | (`err`: `Error`) => `void` |

###### Returns

`this`

###### Implementation of

[`DefaultWritableStream`](stream.md#defaultwritablestream).[`removeListener`](stream.md#removelistener-2)

###### Overrides

[`DefaultReadableStream`](stream.md#defaultreadablestream).[`removeListener`](stream.md#removelistener-1)

###### Call Signature

> **removeListener**(`event`: `"finish"`, `listener`: () => `void`): `this`

###### Parameters

| Parameter | Type |
| ------ | ------ |
| `event` | `"finish"` |
| `listener` | () => `void` |

###### Returns

`this`

###### Implementation of

[`DefaultWritableStream`](stream.md#defaultwritablestream).[`removeListener`](stream.md#removelistener-2)

###### Overrides

[`DefaultReadableStream`](stream.md#defaultreadablestream).[`removeListener`](stream.md#removelistener-1)

##### write()

> **write**(`chunk`: `string` \| `ArrayBuffer` \| `SharedArrayBuffer` \| [`ArrayBufferView`](globals/namespaces/QuickJS.md#arraybufferview) \| [`Buffer`](buffer.md#buffer), `callback`?: (`error`?: `null` \| `Error`) => `void`): `void`

The `writable.write()` method writes some data to the stream, and calls the
supplied `callback` once the data has been fully handled. If an error
occurs, the `callback` will be called with the error as its
first argument. The `callback` is usually called asynchronously and before `'error'`
is emitted.

```js
function write(data, cb) {
  if (!stream.write(data)) {
    stream.once('drain', cb);
  } else {
    process.nextTick(cb);
  }
}

// Wait for cb to be called before doing any other write.
write('hello', () => {
  console.log('Write completed, do more writes now.');
});
```

A `Writable` stream in object mode will always ignore the `encoding` argument.

###### Parameters

| Parameter | Type | Description |
| ------ | ------ | ------ |
| `chunk` | `string` \| `ArrayBuffer` \| `SharedArrayBuffer` \| [`ArrayBufferView`](globals/namespaces/QuickJS.md#arraybufferview) \| [`Buffer`](buffer.md#buffer) | Optional data to write. `chunk` must be a {string}, {Buffer}, {TypedArray} or {DataView}. |
| `callback`? | (`error`?: `null` \| `Error`) => `void` | Callback for when this chunk of data is flushed. |

###### Returns

`void`

`false` if the stream wishes for the calling code to wait for the `'drain'` event to be emitted before continuing to write additional data; otherwise `true`.

###### Since

v0.9.4

###### Implementation of

[`DefaultWritableStream`](stream.md#defaultwritablestream).[`write`](stream.md#write-1)

***

### DefaultReadableStream

#### Extends

- [`ReadableStreamInner`](stream.md#readablestreaminner)

#### Extended by

- [`DefaultDuplexStream`](stream.md#defaultduplexstream)

#### Constructors

##### new DefaultReadableStream()

> **new DefaultReadableStream**(): [`DefaultReadableStream`](stream.md#defaultreadablestream)

###### Returns

[`DefaultReadableStream`](stream.md#defaultreadablestream)

###### Inherited from

[`ReadableStreamInner`](stream.md#readablestreaminner).[`constructor`](stream.md#constructors-3)

#### Methods

##### \[dispose\]()

> **\[dispose\]**(): `void`

Calls `readable.destroy()`.

###### Returns

`void`

###### Inherited from

[`ReadableStreamInner`](stream.md#readablestreaminner).[`[dispose]`](stream.md#dispose-2)

##### addListener()

###### Call Signature

> **addListener**(`event`: [`EventKey`](dom-events.md#eventkey), `listener`: (...`args`: `any`[]) => `void`): `this`

Event emitter
The defined events on documents including:
1. close
2. data
3. end
4. error
5. readable

###### Parameters

| Parameter | Type |
| ------ | ------ |
| `event` | [`EventKey`](dom-events.md#eventkey) |
| `listener` | (...`args`: `any`[]) => `void` |

###### Returns

`this`

###### Inherited from

[`ReadableStreamInner`](stream.md#readablestreaminner).[`addListener`](stream.md#addlistener-3)

###### Call Signature

> **addListener**(`event`: `"close"`, `listener`: () => `void`): `this`

Event emitter
The defined events on documents including:
1. close
2. data
3. end
4. error
5. readable

###### Parameters

| Parameter | Type |
| ------ | ------ |
| `event` | `"close"` |
| `listener` | () => `void` |

###### Returns

`this`

###### Inherited from

[`ReadableStreamInner`](stream.md#readablestreaminner).[`addListener`](stream.md#addlistener-3)

###### Call Signature

> **addListener**(`event`: `"data"`, `listener`: (`chunk`: [`Buffer`](buffer.md#buffer)) => `void`): `this`

Event emitter
The defined events on documents including:
1. close
2. data
3. end
4. error
5. readable

###### Parameters

| Parameter | Type |
| ------ | ------ |
| `event` | `"data"` |
| `listener` | (`chunk`: [`Buffer`](buffer.md#buffer)) => `void` |

###### Returns

`this`

###### Inherited from

[`ReadableStreamInner`](stream.md#readablestreaminner).[`addListener`](stream.md#addlistener-3)

###### Call Signature

> **addListener**(`event`: `"end"`, `listener`: () => `void`): `this`

Event emitter
The defined events on documents including:
1. close
2. data
3. end
4. error
5. readable

###### Parameters

| Parameter | Type |
| ------ | ------ |
| `event` | `"end"` |
| `listener` | () => `void` |

###### Returns

`this`

###### Inherited from

[`ReadableStreamInner`](stream.md#readablestreaminner).[`addListener`](stream.md#addlistener-3)

###### Call Signature

> **addListener**(`event`: `"error"`, `listener`: (`err`: `Error`) => `void`): `this`

Event emitter
The defined events on documents including:
1. close
2. data
3. end
4. error
5. readable

###### Parameters

| Parameter | Type |
| ------ | ------ |
| `event` | `"error"` |
| `listener` | (`err`: `Error`) => `void` |

###### Returns

`this`

###### Inherited from

[`ReadableStreamInner`](stream.md#readablestreaminner).[`addListener`](stream.md#addlistener-3)

###### Call Signature

> **addListener**(`event`: `"readable"`, `listener`: () => `void`): `this`

Event emitter
The defined events on documents including:
1. close
2. data
3. end
4. error
5. readable

###### Parameters

| Parameter | Type |
| ------ | ------ |
| `event` | `"readable"` |
| `listener` | () => `void` |

###### Returns

`this`

###### Inherited from

[`ReadableStreamInner`](stream.md#readablestreaminner).[`addListener`](stream.md#addlistener-3)

##### destroy()

> **destroy**(`error`?: `Error`): `this`

Destroy the stream. Optionally emit an `'error'` event, and emit a `'close'` event. After this call, the readable
stream will release any internal resources and subsequent calls to `push()` will be ignored.

Once `destroy()` has been called any further calls will be a no-op and no
further errors except from `_destroy()` may be emitted as `'error'`.

Implementors should not override this method, but instead implement `readable._destroy()`.

###### Parameters

| Parameter | Type | Description |
| ------ | ------ | ------ |
| `error`? | `Error` | Error which will be passed as payload in `'error'` event |

###### Returns

`this`

###### Inherited from

[`ReadableStreamInner`](stream.md#readablestreaminner).[`destroy`](stream.md#destroy-2)

##### emit()

###### Call Signature

> **emit**(`event`: [`EventKey`](dom-events.md#eventkey), ...`args`: `any`[]): `boolean`

Synchronously calls each of the listeners registered for the event named `eventName`, in the order they were registered, passing the supplied arguments
to each.

```js
import { EventEmitter } from 'events';
const myEmitter = new EventEmitter();

// First listener
myEmitter.on('event', function firstListener() {
  console.log('Helloooo! first listener');
});
// Second listener
myEmitter.on('event', function secondListener(arg1, arg2) {
  console.log(`event with parameters ${arg1}, ${arg2} in second listener`);
});
// Third listener
myEmitter.on('event', function thirdListener(...args) {
  const parameters = args.join(', ');
  console.log(`event with parameters ${parameters} in third listener`);
});

myEmitter.emit('event', 1, 2, 3, 4, 5);

// Prints:
// Helloooo! first listener
// event with parameters 1, 2 in second listener
// event with parameters 1, 2, 3, 4, 5 in third listener
```

###### Parameters

| Parameter | Type |
| ------ | ------ |
| `event` | [`EventKey`](dom-events.md#eventkey) |
| ...`args` | `any`[] |

###### Returns

`boolean`

###### Inherited from

[`ReadableStreamInner`](stream.md#readablestreaminner).[`emit`](stream.md#emit-3)

###### Call Signature

> **emit**(`event`: `"close"`): `boolean`

###### Parameters

| Parameter | Type |
| ------ | ------ |
| `event` | `"close"` |

###### Returns

`boolean`

###### Inherited from

[`ReadableStreamInner`](stream.md#readablestreaminner).[`emit`](stream.md#emit-3)

###### Call Signature

> **emit**(`event`: `"data"`, `chunk`: [`Buffer`](buffer.md#buffer)): `boolean`

###### Parameters

| Parameter | Type |
| ------ | ------ |
| `event` | `"data"` |
| `chunk` | [`Buffer`](buffer.md#buffer) |

###### Returns

`boolean`

###### Inherited from

[`ReadableStreamInner`](stream.md#readablestreaminner).[`emit`](stream.md#emit-3)

###### Call Signature

> **emit**(`event`: `"end"`): `boolean`

###### Parameters

| Parameter | Type |
| ------ | ------ |
| `event` | `"end"` |

###### Returns

`boolean`

###### Inherited from

[`ReadableStreamInner`](stream.md#readablestreaminner).[`emit`](stream.md#emit-3)

###### Call Signature

> **emit**(`event`: `"error"`, `err`: `Error`): `boolean`

###### Parameters

| Parameter | Type |
| ------ | ------ |
| `event` | `"error"` |
| `err` | `Error` |

###### Returns

`boolean`

###### Inherited from

[`ReadableStreamInner`](stream.md#readablestreaminner).[`emit`](stream.md#emit-3)

###### Call Signature

> **emit**(`event`: `"readable"`): `boolean`

###### Parameters

| Parameter | Type |
| ------ | ------ |
| `event` | `"readable"` |

###### Returns

`boolean`

###### Inherited from

[`ReadableStreamInner`](stream.md#readablestreaminner).[`emit`](stream.md#emit-3)

##### eventNames()

> **eventNames**(): [`EventKey`](dom-events.md#eventkey)[]

Returns an array listing the events for which the emitter has registered
listeners. The values in the array are strings or `Symbol`s.

```js
import { EventEmitter } from 'events';

const myEE = new EventEmitter();
myEE.on('foo', () => {});
myEE.on('bar', () => {});

const sym = Symbol('symbol');
myEE.on(sym, () => {});

console.log(myEE.eventNames());
// Prints: [ 'foo', 'bar', Symbol(symbol) ]
```

###### Returns

[`EventKey`](dom-events.md#eventkey)[]

###### Inherited from

[`ReadableStreamInner`](stream.md#readablestreaminner).[`eventNames`](stream.md#eventnames-3)

##### off()

> **off**\<`K`\>(`eventName`: [`EventKey`](dom-events.md#eventkey), `listener`: (...`args`: `any`[]) => `void`): `this`

Alias for `emitter.removeListener()`.

###### Type Parameters

| Type Parameter |
| ------ |
| `K` |

###### Parameters

| Parameter | Type |
| ------ | ------ |
| `eventName` | [`EventKey`](dom-events.md#eventkey) |
| `listener` | (...`args`: `any`[]) => `void` |

###### Returns

`this`

###### Inherited from

[`ReadableStreamInner`](stream.md#readablestreaminner).[`off`](stream.md#off-3)

##### on()

###### Call Signature

> **on**(`event`: [`EventKey`](dom-events.md#eventkey), `listener`: (...`args`: `any`[]) => `void`): `this`

Adds the `listener` function to the end of the listeners array for the event
named `eventName`. No checks are made to see if the `listener` has already
been added. Multiple calls passing the same combination of `eventName` and
`listener` will result in the `listener` being added, and called, multiple times.

```js
server.on('connection', (stream) => {
  console.log('someone connected!');
});
```

Returns a reference to the `EventEmitter`, so that calls can be chained.

By default, event listeners are invoked in the order they are added. The `emitter.prependListener()` method can be used as an alternative to add the
event listener to the beginning of the listeners array.

```js
import { EventEmitter } from 'events';
const myEE = new EventEmitter();
myEE.on('foo', () => console.log('a'));
myEE.prependListener('foo', () => console.log('b'));
myEE.emit('foo');
// Prints:
//   b
//   a
```

###### Parameters

| Parameter | Type | Description |
| ------ | ------ | ------ |
| `event` | [`EventKey`](dom-events.md#eventkey) | - |
| `listener` | (...`args`: `any`[]) => `void` | The callback function |

###### Returns

`this`

###### Inherited from

[`ReadableStreamInner`](stream.md#readablestreaminner).[`on`](stream.md#on-3)

###### Call Signature

> **on**(`event`: `"close"`, `listener`: () => `void`): `this`

###### Parameters

| Parameter | Type |
| ------ | ------ |
| `event` | `"close"` |
| `listener` | () => `void` |

###### Returns

`this`

###### Inherited from

[`ReadableStreamInner`](stream.md#readablestreaminner).[`on`](stream.md#on-3)

###### Call Signature

> **on**(`event`: `"data"`, `listener`: (`chunk`: [`Buffer`](buffer.md#buffer)) => `void`): `this`

###### Parameters

| Parameter | Type |
| ------ | ------ |
| `event` | `"data"` |
| `listener` | (`chunk`: [`Buffer`](buffer.md#buffer)) => `void` |

###### Returns

`this`

###### Inherited from

[`ReadableStreamInner`](stream.md#readablestreaminner).[`on`](stream.md#on-3)

###### Call Signature

> **on**(`event`: `"end"`, `listener`: () => `void`): `this`

###### Parameters

| Parameter | Type |
| ------ | ------ |
| `event` | `"end"` |
| `listener` | () => `void` |

###### Returns

`this`

###### Inherited from

[`ReadableStreamInner`](stream.md#readablestreaminner).[`on`](stream.md#on-3)

###### Call Signature

> **on**(`event`: `"error"`, `listener`: (`err`: `Error`) => `void`): `this`

###### Parameters

| Parameter | Type |
| ------ | ------ |
| `event` | `"error"` |
| `listener` | (`err`: `Error`) => `void` |

###### Returns

`this`

###### Inherited from

[`ReadableStreamInner`](stream.md#readablestreaminner).[`on`](stream.md#on-3)

###### Call Signature

> **on**(`event`: `"readable"`, `listener`: () => `void`): `this`

###### Parameters

| Parameter | Type |
| ------ | ------ |
| `event` | `"readable"` |
| `listener` | () => `void` |

###### Returns

`this`

###### Inherited from

[`ReadableStreamInner`](stream.md#readablestreaminner).[`on`](stream.md#on-3)

##### once()

###### Call Signature

> **once**(`event`: [`EventKey`](dom-events.md#eventkey), `listener`: (...`args`: `any`[]) => `void`): `this`

Adds a **one-time** `listener` function for the event named `eventName`. The
next time `eventName` is triggered, this listener is removed and then invoked.

Returns a reference to the `EventEmitter`, so that calls can be chained.

By default, event listeners are invoked in the order they are added. The `emitter.prependOnceListener()` method can be used as an alternative to add the
event listener to the beginning of the listeners array.

```js
import { EventEmitter } from 'events';
const myEE = new EventEmitter();
myEE.once('foo', () => console.log('a'));
myEE.prependOnceListener('foo', () => console.log('b'));
myEE.emit('foo');
// Prints:
//   b
//   a
```

###### Parameters

| Parameter | Type | Description |
| ------ | ------ | ------ |
| `event` | [`EventKey`](dom-events.md#eventkey) | - |
| `listener` | (...`args`: `any`[]) => `void` | The callback function |

###### Returns

`this`

###### Since

v0.3.0

###### Inherited from

[`ReadableStreamInner`](stream.md#readablestreaminner).[`once`](stream.md#once-3)

###### Call Signature

> **once**(`event`: `"close"`, `listener`: () => `void`): `this`

###### Parameters

| Parameter | Type |
| ------ | ------ |
| `event` | `"close"` |
| `listener` | () => `void` |

###### Returns

`this`

###### Inherited from

[`ReadableStreamInner`](stream.md#readablestreaminner).[`once`](stream.md#once-3)

###### Call Signature

> **once**(`event`: `"data"`, `listener`: (`chunk`: [`Buffer`](buffer.md#buffer)) => `void`): `this`

###### Parameters

| Parameter | Type |
| ------ | ------ |
| `event` | `"data"` |
| `listener` | (`chunk`: [`Buffer`](buffer.md#buffer)) => `void` |

###### Returns

`this`

###### Inherited from

[`ReadableStreamInner`](stream.md#readablestreaminner).[`once`](stream.md#once-3)

###### Call Signature

> **once**(`event`: `"end"`, `listener`: () => `void`): `this`

###### Parameters

| Parameter | Type |
| ------ | ------ |
| `event` | `"end"` |
| `listener` | () => `void` |

###### Returns

`this`

###### Inherited from

[`ReadableStreamInner`](stream.md#readablestreaminner).[`once`](stream.md#once-3)

###### Call Signature

> **once**(`event`: `"error"`, `listener`: (`err`: `Error`) => `void`): `this`

###### Parameters

| Parameter | Type |
| ------ | ------ |
| `event` | `"error"` |
| `listener` | (`err`: `Error`) => `void` |

###### Returns

`this`

###### Inherited from

[`ReadableStreamInner`](stream.md#readablestreaminner).[`once`](stream.md#once-3)

###### Call Signature

> **once**(`event`: `"readable"`, `listener`: () => `void`): `this`

###### Parameters

| Parameter | Type |
| ------ | ------ |
| `event` | `"readable"` |
| `listener` | () => `void` |

###### Returns

`this`

###### Inherited from

[`ReadableStreamInner`](stream.md#readablestreaminner).[`once`](stream.md#once-3)

##### prependListener()

###### Call Signature

> **prependListener**(`event`: [`EventKey`](dom-events.md#eventkey), `listener`: (...`args`: `any`[]) => `void`): `this`

Adds the `listener` function to the _beginning_ of the listeners array for the
event named `eventName`. No checks are made to see if the `listener` has
already been added. Multiple calls passing the same combination of `eventName`
and `listener` will result in the `listener` being added, and called, multiple times.

Returns a reference to the `EventEmitter`, so that calls can be chained.

###### Parameters

| Parameter | Type | Description |
| ------ | ------ | ------ |
| `event` | [`EventKey`](dom-events.md#eventkey) | - |
| `listener` | (...`args`: `any`[]) => `void` | The callback function |

###### Returns

`this`

###### Inherited from

[`ReadableStreamInner`](stream.md#readablestreaminner).[`prependListener`](stream.md#prependlistener-3)

###### Call Signature

> **prependListener**(`event`: `"close"`, `listener`: () => `void`): `this`

###### Parameters

| Parameter | Type |
| ------ | ------ |
| `event` | `"close"` |
| `listener` | () => `void` |

###### Returns

`this`

###### Inherited from

[`ReadableStreamInner`](stream.md#readablestreaminner).[`prependListener`](stream.md#prependlistener-3)

###### Call Signature

> **prependListener**(`event`: `"data"`, `listener`: (`chunk`: [`Buffer`](buffer.md#buffer)) => `void`): `this`

###### Parameters

| Parameter | Type |
| ------ | ------ |
| `event` | `"data"` |
| `listener` | (`chunk`: [`Buffer`](buffer.md#buffer)) => `void` |

###### Returns

`this`

###### Inherited from

[`ReadableStreamInner`](stream.md#readablestreaminner).[`prependListener`](stream.md#prependlistener-3)

###### Call Signature

> **prependListener**(`event`: `"end"`, `listener`: () => `void`): `this`

###### Parameters

| Parameter | Type |
| ------ | ------ |
| `event` | `"end"` |
| `listener` | () => `void` |

###### Returns

`this`

###### Inherited from

[`ReadableStreamInner`](stream.md#readablestreaminner).[`prependListener`](stream.md#prependlistener-3)

###### Call Signature

> **prependListener**(`event`: `"error"`, `listener`: (`err`: `Error`) => `void`): `this`

###### Parameters

| Parameter | Type |
| ------ | ------ |
| `event` | `"error"` |
| `listener` | (`err`: `Error`) => `void` |

###### Returns

`this`

###### Inherited from

[`ReadableStreamInner`](stream.md#readablestreaminner).[`prependListener`](stream.md#prependlistener-3)

###### Call Signature

> **prependListener**(`event`: `"readable"`, `listener`: () => `void`): `this`

###### Parameters

| Parameter | Type |
| ------ | ------ |
| `event` | `"readable"` |
| `listener` | () => `void` |

###### Returns

`this`

###### Inherited from

[`ReadableStreamInner`](stream.md#readablestreaminner).[`prependListener`](stream.md#prependlistener-3)

##### prependOnceListener()

###### Call Signature

> **prependOnceListener**(`event`: [`EventKey`](dom-events.md#eventkey), `listener`: (...`args`: `any`[]) => `void`): `this`

Adds a **one-time**`listener` function for the event named `eventName` to the _beginning_ of the listeners array.
The next time `eventName` is triggered, this listener is removed, and then invoked.

Returns a reference to the `EventEmitter`, so that calls can be chained.

###### Parameters

| Parameter | Type | Description |
| ------ | ------ | ------ |
| `event` | [`EventKey`](dom-events.md#eventkey) | - |
| `listener` | (...`args`: `any`[]) => `void` | The callback function |

###### Returns

`this`

###### Inherited from

[`ReadableStreamInner`](stream.md#readablestreaminner).[`prependOnceListener`](stream.md#prependoncelistener-3)

###### Call Signature

> **prependOnceListener**(`event`: `"close"`, `listener`: () => `void`): `this`

###### Parameters

| Parameter | Type |
| ------ | ------ |
| `event` | `"close"` |
| `listener` | () => `void` |

###### Returns

`this`

###### Inherited from

[`ReadableStreamInner`](stream.md#readablestreaminner).[`prependOnceListener`](stream.md#prependoncelistener-3)

###### Call Signature

> **prependOnceListener**(`event`: `"data"`, `listener`: (`chunk`: [`Buffer`](buffer.md#buffer)) => `void`): `this`

###### Parameters

| Parameter | Type |
| ------ | ------ |
| `event` | `"data"` |
| `listener` | (`chunk`: [`Buffer`](buffer.md#buffer)) => `void` |

###### Returns

`this`

###### Inherited from

[`ReadableStreamInner`](stream.md#readablestreaminner).[`prependOnceListener`](stream.md#prependoncelistener-3)

###### Call Signature

> **prependOnceListener**(`event`: `"end"`, `listener`: () => `void`): `this`

###### Parameters

| Parameter | Type |
| ------ | ------ |
| `event` | `"end"` |
| `listener` | () => `void` |

###### Returns

`this`

###### Inherited from

[`ReadableStreamInner`](stream.md#readablestreaminner).[`prependOnceListener`](stream.md#prependoncelistener-3)

###### Call Signature

> **prependOnceListener**(`event`: `"error"`, `listener`: (`err`: `Error`) => `void`): `this`

###### Parameters

| Parameter | Type |
| ------ | ------ |
| `event` | `"error"` |
| `listener` | (`err`: `Error`) => `void` |

###### Returns

`this`

###### Inherited from

[`ReadableStreamInner`](stream.md#readablestreaminner).[`prependOnceListener`](stream.md#prependoncelistener-3)

###### Call Signature

> **prependOnceListener**(`event`: `"readable"`, `listener`: () => `void`): `this`

###### Parameters

| Parameter | Type |
| ------ | ------ |
| `event` | `"readable"` |
| `listener` | () => `void` |

###### Returns

`this`

###### Inherited from

[`ReadableStreamInner`](stream.md#readablestreaminner).[`prependOnceListener`](stream.md#prependoncelistener-3)

##### read()

> **read**(`size`?: `number`): `null` \| [`Buffer`](buffer.md#buffer)

The `readable.read()` method reads data out of the internal buffer and
returns it. If no data is available to be read, `null` is returned. By default,
the data is returned as a `Buffer` object unless an encoding has been
specified using the `readable.setEncoding()` method or the stream is operating
in object mode.

The optional `size` argument specifies a specific number of bytes to read. If
`size` bytes are not available to be read, `null` will be returned _unless_ the
stream has ended, in which case all of the data remaining in the internal buffer
will be returned.

If the `size` argument is not specified, all of the data contained in the
internal buffer will be returned.

The `size` argument must be less than or equal to 1 GiB.

The `readable.read()` method should only be called on `Readable` streams
operating in paused mode. In flowing mode, `readable.read()` is called
automatically until the internal buffer is fully drained.

```js
const readable = getReadableStreamSomehow();

// 'readable' may be triggered multiple times as data is buffered in
readable.on('readable', () => {
  let chunk;
  console.log('Stream is readable (new data received in buffer)');
  // Use a loop to make sure we read all currently available data
  while (null !== (chunk = readable.read())) {
    console.log(`Read ${chunk.length} bytes of data...`);
  }
});

// 'end' will be triggered once when there is no more data available
readable.on('end', () => {
  console.log('Reached end of stream.');
});
```

Each call to `readable.read()` returns a chunk of data, or `null`. The chunks
are not concatenated. A `while` loop is necessary to consume all data
currently in the buffer. When reading a large file `.read()` may return `null`,
having consumed all buffered content so far, but there is still more data to
come not yet buffered. In this case a new `'readable'` event will be emitted
when there is more data in the buffer. Finally the `'end'` event will be
emitted when there is no more data to come.

Therefore to read a file's whole contents from a `readable`, it is necessary
to collect chunks across multiple `'readable'` events:

```js
const chunks = [];

readable.on('readable', () => {
  let chunk;
  while (null !== (chunk = readable.read())) {
    chunks.push(chunk);
  }
});

readable.on('end', () => {
  const content = chunks.join('');
});
```

A `Readable` stream in object mode will always return a single item from
a call to `readable.read(size)`, regardless of the value of the `size` argument.

If the `readable.read()` method returns a chunk of data, a `'data'` event will
also be emitted.

Calling [read](stream.md#read-2) after the `'end'` event has
been emitted will return `null`. No runtime error will be raised.

###### Parameters

| Parameter | Type | Description |
| ------ | ------ | ------ |
| `size`? | `number` | Optional argument to specify how much data to read. |

###### Returns

`null` \| [`Buffer`](buffer.md#buffer)

###### Inherited from

[`ReadableStreamInner`](stream.md#readablestreaminner).[`read`](stream.md#read-2)

##### removeListener()

###### Call Signature

> **removeListener**(`event`: [`EventKey`](dom-events.md#eventkey), `listener`: (...`args`: `any`[]) => `void`): `this`

Removes the specified `listener` from the listener array for the event named `eventName`.

`removeListener()` will remove, at most, one instance of a listener from the
listener array. If any single listener has been added multiple times to the
listener array for the specified `eventName`, then `removeListener()` must be
called multiple times to remove each instance.

Once an event is emitted, all listeners attached to it at the time of emitting are called in order.
This implies that any `removeListener()` calls _after_ emitting and _before_ the last listener finishes execution
will not remove them from `emit()` in progress. Subsequent events behave as expected.

```js
import { EventEmitter } from 'events';
class MyEmitter extends EventEmitter {}
const myEmitter = new MyEmitter();

const callbackA = () => {
  console.log('A');
  myEmitter.removeListener('event', callbackB);
};

const callbackB = () => {
  console.log('B');
};

myEmitter.on('event', callbackA);

myEmitter.on('event', callbackB);

// callbackA removes listener callbackB but it will still be called.
// Internal listener array at time of emit [callbackA, callbackB]
myEmitter.emit('event');
// Prints:
//   A
//   B

// callbackB is now removed.
// Internal listener array [callbackA]
myEmitter.emit('event');
// Prints:
//   A
```

Because listeners are managed using an internal array, calling this will
change the position indices of any listener registered _after_ the listener
being removed. This will not impact the order in which listeners are called,
but it means that any copies of the listener array as returned by
the `emitter.listeners()` method will need to be recreated.

When a single function has been added as a handler multiple times for a single
event (as in the example below), `removeListener()` will remove the most
recently added instance. In the example the `once('ping')` listener is removed:

```js
import { EventEmitter } from 'events';
const ee = new EventEmitter();

function pong() {
  console.log('pong');
}

ee.on('ping', pong);
ee.once('ping', pong);
ee.removeListener('ping', pong);

ee.emit('ping');
ee.emit('ping');
```

Returns a reference to the `EventEmitter`, so that calls can be chained.

###### Parameters

| Parameter | Type |
| ------ | ------ |
| `event` | [`EventKey`](dom-events.md#eventkey) |
| `listener` | (...`args`: `any`[]) => `void` |

###### Returns

`this`

###### Inherited from

[`ReadableStreamInner`](stream.md#readablestreaminner).[`removeListener`](stream.md#removelistener-3)

###### Call Signature

> **removeListener**(`event`: `"close"`, `listener`: () => `void`): `this`

###### Parameters

| Parameter | Type |
| ------ | ------ |
| `event` | `"close"` |
| `listener` | () => `void` |

###### Returns

`this`

###### Inherited from

[`ReadableStreamInner`](stream.md#readablestreaminner).[`removeListener`](stream.md#removelistener-3)

###### Call Signature

> **removeListener**(`event`: `"data"`, `listener`: (`chunk`: [`Buffer`](buffer.md#buffer)) => `void`): `this`

###### Parameters

| Parameter | Type |
| ------ | ------ |
| `event` | `"data"` |
| `listener` | (`chunk`: [`Buffer`](buffer.md#buffer)) => `void` |

###### Returns

`this`

###### Inherited from

[`ReadableStreamInner`](stream.md#readablestreaminner).[`removeListener`](stream.md#removelistener-3)

###### Call Signature

> **removeListener**(`event`: `"end"`, `listener`: () => `void`): `this`

###### Parameters

| Parameter | Type |
| ------ | ------ |
| `event` | `"end"` |
| `listener` | () => `void` |

###### Returns

`this`

###### Inherited from

[`ReadableStreamInner`](stream.md#readablestreaminner).[`removeListener`](stream.md#removelistener-3)

###### Call Signature

> **removeListener**(`event`: `"error"`, `listener`: (`err`: `Error`) => `void`): `this`

###### Parameters

| Parameter | Type |
| ------ | ------ |
| `event` | `"error"` |
| `listener` | (`err`: `Error`) => `void` |

###### Returns

`this`

###### Inherited from

[`ReadableStreamInner`](stream.md#readablestreaminner).[`removeListener`](stream.md#removelistener-3)

###### Call Signature

> **removeListener**(`event`: `"readable"`, `listener`: () => `void`): `this`

###### Parameters

| Parameter | Type |
| ------ | ------ |
| `event` | `"readable"` |
| `listener` | () => `void` |

###### Returns

`this`

###### Inherited from

[`ReadableStreamInner`](stream.md#readablestreaminner).[`removeListener`](stream.md#removelistener-3)

***

### DefaultWritableStream

#### Extends

- [`WritableStreamInner`](stream.md#writablestreaminner)

#### Constructors

##### new DefaultWritableStream()

> **new DefaultWritableStream**(): [`DefaultWritableStream`](stream.md#defaultwritablestream)

###### Returns

[`DefaultWritableStream`](stream.md#defaultwritablestream)

###### Inherited from

[`WritableStreamInner`](stream.md#writablestreaminner).[`constructor`](stream.md#constructors-4)

#### Methods

##### addListener()

###### Call Signature

> **addListener**(`event`: [`EventKey`](dom-events.md#eventkey), `listener`: (...`args`: `any`[]) => `void`): `this`

Event emitter
The defined events on documents including:
1. close
2. error
3. finish

###### Parameters

| Parameter | Type |
| ------ | ------ |
| `event` | [`EventKey`](dom-events.md#eventkey) |
| `listener` | (...`args`: `any`[]) => `void` |

###### Returns

`this`

###### Inherited from

[`WritableStreamInner`](stream.md#writablestreaminner).[`addListener`](stream.md#addlistener-4)

###### Call Signature

> **addListener**(`event`: `"close"`, `listener`: () => `void`): `this`

Event emitter
The defined events on documents including:
1. close
2. error
3. finish

###### Parameters

| Parameter | Type |
| ------ | ------ |
| `event` | `"close"` |
| `listener` | () => `void` |

###### Returns

`this`

###### Inherited from

[`WritableStreamInner`](stream.md#writablestreaminner).[`addListener`](stream.md#addlistener-4)

###### Call Signature

> **addListener**(`event`: `"error"`, `listener`: (`err`: `Error`) => `void`): `this`

Event emitter
The defined events on documents including:
1. close
2. error
3. finish

###### Parameters

| Parameter | Type |
| ------ | ------ |
| `event` | `"error"` |
| `listener` | (`err`: `Error`) => `void` |

###### Returns

`this`

###### Inherited from

[`WritableStreamInner`](stream.md#writablestreaminner).[`addListener`](stream.md#addlistener-4)

###### Call Signature

> **addListener**(`event`: `"finish"`, `listener`: () => `void`): `this`

Event emitter
The defined events on documents including:
1. close
2. error
3. finish

###### Parameters

| Parameter | Type |
| ------ | ------ |
| `event` | `"finish"` |
| `listener` | () => `void` |

###### Returns

`this`

###### Inherited from

[`WritableStreamInner`](stream.md#writablestreaminner).[`addListener`](stream.md#addlistener-4)

##### emit()

###### Call Signature

> **emit**(`event`: [`EventKey`](dom-events.md#eventkey), ...`args`: `any`[]): `boolean`

Synchronously calls each of the listeners registered for the event named `eventName`, in the order they were registered, passing the supplied arguments
to each.

```js
import { EventEmitter } from 'events';
const myEmitter = new EventEmitter();

// First listener
myEmitter.on('event', function firstListener() {
  console.log('Helloooo! first listener');
});
// Second listener
myEmitter.on('event', function secondListener(arg1, arg2) {
  console.log(`event with parameters ${arg1}, ${arg2} in second listener`);
});
// Third listener
myEmitter.on('event', function thirdListener(...args) {
  const parameters = args.join(', ');
  console.log(`event with parameters ${parameters} in third listener`);
});

myEmitter.emit('event', 1, 2, 3, 4, 5);

// Prints:
// Helloooo! first listener
// event with parameters 1, 2 in second listener
// event with parameters 1, 2, 3, 4, 5 in third listener
```

###### Parameters

| Parameter | Type |
| ------ | ------ |
| `event` | [`EventKey`](dom-events.md#eventkey) |
| ...`args` | `any`[] |

###### Returns

`boolean`

###### Inherited from

[`WritableStreamInner`](stream.md#writablestreaminner).[`emit`](stream.md#emit-4)

###### Call Signature

> **emit**(`event`: `"close"`): `boolean`

###### Parameters

| Parameter | Type |
| ------ | ------ |
| `event` | `"close"` |

###### Returns

`boolean`

###### Inherited from

[`WritableStreamInner`](stream.md#writablestreaminner).[`emit`](stream.md#emit-4)

###### Call Signature

> **emit**(`event`: `"error"`, `err`: `Error`): `boolean`

###### Parameters

| Parameter | Type |
| ------ | ------ |
| `event` | `"error"` |
| `err` | `Error` |

###### Returns

`boolean`

###### Inherited from

[`WritableStreamInner`](stream.md#writablestreaminner).[`emit`](stream.md#emit-4)

###### Call Signature

> **emit**(`event`: `"finish"`): `boolean`

###### Parameters

| Parameter | Type |
| ------ | ------ |
| `event` | `"finish"` |

###### Returns

`boolean`

###### Inherited from

[`WritableStreamInner`](stream.md#writablestreaminner).[`emit`](stream.md#emit-4)

##### end()

> **end**(): `this`

Calling the `writable.end()` method signals that no more data will be written
to the `Writable`.

Calling the [write](stream.md#write-2) method after calling [end](stream.md#end-2) will raise an error.

###### Returns

`this`

###### Inherited from

[`WritableStreamInner`](stream.md#writablestreaminner).[`end`](stream.md#end-2)

##### eventNames()

> **eventNames**(): [`EventKey`](dom-events.md#eventkey)[]

Returns an array listing the events for which the emitter has registered
listeners. The values in the array are strings or `Symbol`s.

```js
import { EventEmitter } from 'events';

const myEE = new EventEmitter();
myEE.on('foo', () => {});
myEE.on('bar', () => {});

const sym = Symbol('symbol');
myEE.on(sym, () => {});

console.log(myEE.eventNames());
// Prints: [ 'foo', 'bar', Symbol(symbol) ]
```

###### Returns

[`EventKey`](dom-events.md#eventkey)[]

###### Inherited from

[`WritableStreamInner`](stream.md#writablestreaminner).[`eventNames`](stream.md#eventnames-4)

##### off()

> **off**\<`K`\>(`eventName`: [`EventKey`](dom-events.md#eventkey), `listener`: (...`args`: `any`[]) => `void`): `this`

Alias for `emitter.removeListener()`.

###### Type Parameters

| Type Parameter |
| ------ |
| `K` |

###### Parameters

| Parameter | Type |
| ------ | ------ |
| `eventName` | [`EventKey`](dom-events.md#eventkey) |
| `listener` | (...`args`: `any`[]) => `void` |

###### Returns

`this`

###### Inherited from

[`WritableStreamInner`](stream.md#writablestreaminner).[`off`](stream.md#off-4)

##### on()

###### Call Signature

> **on**(`event`: [`EventKey`](dom-events.md#eventkey), `listener`: (...`args`: `any`[]) => `void`): `this`

Adds the `listener` function to the end of the listeners array for the event
named `eventName`. No checks are made to see if the `listener` has already
been added. Multiple calls passing the same combination of `eventName` and
`listener` will result in the `listener` being added, and called, multiple times.

```js
server.on('connection', (stream) => {
  console.log('someone connected!');
});
```

Returns a reference to the `EventEmitter`, so that calls can be chained.

By default, event listeners are invoked in the order they are added. The `emitter.prependListener()` method can be used as an alternative to add the
event listener to the beginning of the listeners array.

```js
import { EventEmitter } from 'events';
const myEE = new EventEmitter();
myEE.on('foo', () => console.log('a'));
myEE.prependListener('foo', () => console.log('b'));
myEE.emit('foo');
// Prints:
//   b
//   a
```

###### Parameters

| Parameter | Type | Description |
| ------ | ------ | ------ |
| `event` | [`EventKey`](dom-events.md#eventkey) | - |
| `listener` | (...`args`: `any`[]) => `void` | The callback function |

###### Returns

`this`

###### Inherited from

[`WritableStreamInner`](stream.md#writablestreaminner).[`on`](stream.md#on-4)

###### Call Signature

> **on**(`event`: `"close"`, `listener`: () => `void`): `this`

###### Parameters

| Parameter | Type |
| ------ | ------ |
| `event` | `"close"` |
| `listener` | () => `void` |

###### Returns

`this`

###### Inherited from

[`WritableStreamInner`](stream.md#writablestreaminner).[`on`](stream.md#on-4)

###### Call Signature

> **on**(`event`: `"error"`, `listener`: (`err`: `Error`) => `void`): `this`

###### Parameters

| Parameter | Type |
| ------ | ------ |
| `event` | `"error"` |
| `listener` | (`err`: `Error`) => `void` |

###### Returns

`this`

###### Inherited from

[`WritableStreamInner`](stream.md#writablestreaminner).[`on`](stream.md#on-4)

###### Call Signature

> **on**(`event`: `"finish"`, `listener`: () => `void`): `this`

###### Parameters

| Parameter | Type |
| ------ | ------ |
| `event` | `"finish"` |
| `listener` | () => `void` |

###### Returns

`this`

###### Inherited from

[`WritableStreamInner`](stream.md#writablestreaminner).[`on`](stream.md#on-4)

##### once()

###### Call Signature

> **once**(`event`: [`EventKey`](dom-events.md#eventkey), `listener`: (...`args`: `any`[]) => `void`): `this`

Adds a **one-time** `listener` function for the event named `eventName`. The
next time `eventName` is triggered, this listener is removed and then invoked.

Returns a reference to the `EventEmitter`, so that calls can be chained.

By default, event listeners are invoked in the order they are added. The `emitter.prependOnceListener()` method can be used as an alternative to add the
event listener to the beginning of the listeners array.

```js
import { EventEmitter } from 'events';
const myEE = new EventEmitter();
myEE.once('foo', () => console.log('a'));
myEE.prependOnceListener('foo', () => console.log('b'));
myEE.emit('foo');
// Prints:
//   b
//   a
```

###### Parameters

| Parameter | Type | Description |
| ------ | ------ | ------ |
| `event` | [`EventKey`](dom-events.md#eventkey) | - |
| `listener` | (...`args`: `any`[]) => `void` | The callback function |

###### Returns

`this`

###### Since

v0.3.0

###### Inherited from

[`WritableStreamInner`](stream.md#writablestreaminner).[`once`](stream.md#once-4)

###### Call Signature

> **once**(`event`: `"close"`, `listener`: () => `void`): `this`

###### Parameters

| Parameter | Type |
| ------ | ------ |
| `event` | `"close"` |
| `listener` | () => `void` |

###### Returns

`this`

###### Inherited from

[`WritableStreamInner`](stream.md#writablestreaminner).[`once`](stream.md#once-4)

###### Call Signature

> **once**(`event`: `"error"`, `listener`: (`err`: `Error`) => `void`): `this`

###### Parameters

| Parameter | Type |
| ------ | ------ |
| `event` | `"error"` |
| `listener` | (`err`: `Error`) => `void` |

###### Returns

`this`

###### Inherited from

[`WritableStreamInner`](stream.md#writablestreaminner).[`once`](stream.md#once-4)

###### Call Signature

> **once**(`event`: `"finish"`, `listener`: () => `void`): `this`

###### Parameters

| Parameter | Type |
| ------ | ------ |
| `event` | `"finish"` |
| `listener` | () => `void` |

###### Returns

`this`

###### Inherited from

[`WritableStreamInner`](stream.md#writablestreaminner).[`once`](stream.md#once-4)

##### prependListener()

###### Call Signature

> **prependListener**(`event`: [`EventKey`](dom-events.md#eventkey), `listener`: (...`args`: `any`[]) => `void`): `this`

Adds the `listener` function to the _beginning_ of the listeners array for the
event named `eventName`. No checks are made to see if the `listener` has
already been added. Multiple calls passing the same combination of `eventName`
and `listener` will result in the `listener` being added, and called, multiple times.

Returns a reference to the `EventEmitter`, so that calls can be chained.

###### Parameters

| Parameter | Type | Description |
| ------ | ------ | ------ |
| `event` | [`EventKey`](dom-events.md#eventkey) | - |
| `listener` | (...`args`: `any`[]) => `void` | The callback function |

###### Returns

`this`

###### Inherited from

[`WritableStreamInner`](stream.md#writablestreaminner).[`prependListener`](stream.md#prependlistener-4)

###### Call Signature

> **prependListener**(`event`: `"close"`, `listener`: () => `void`): `this`

###### Parameters

| Parameter | Type |
| ------ | ------ |
| `event` | `"close"` |
| `listener` | () => `void` |

###### Returns

`this`

###### Inherited from

[`WritableStreamInner`](stream.md#writablestreaminner).[`prependListener`](stream.md#prependlistener-4)

###### Call Signature

> **prependListener**(`event`: `"error"`, `listener`: (`err`: `Error`) => `void`): `this`

###### Parameters

| Parameter | Type |
| ------ | ------ |
| `event` | `"error"` |
| `listener` | (`err`: `Error`) => `void` |

###### Returns

`this`

###### Inherited from

[`WritableStreamInner`](stream.md#writablestreaminner).[`prependListener`](stream.md#prependlistener-4)

###### Call Signature

> **prependListener**(`event`: `"finish"`, `listener`: () => `void`): `this`

###### Parameters

| Parameter | Type |
| ------ | ------ |
| `event` | `"finish"` |
| `listener` | () => `void` |

###### Returns

`this`

###### Inherited from

[`WritableStreamInner`](stream.md#writablestreaminner).[`prependListener`](stream.md#prependlistener-4)

##### prependOnceListener()

###### Call Signature

> **prependOnceListener**(`event`: [`EventKey`](dom-events.md#eventkey), `listener`: (...`args`: `any`[]) => `void`): `this`

Adds a **one-time**`listener` function for the event named `eventName` to the _beginning_ of the listeners array.
The next time `eventName` is triggered, this listener is removed, and then invoked.

Returns a reference to the `EventEmitter`, so that calls can be chained.

###### Parameters

| Parameter | Type | Description |
| ------ | ------ | ------ |
| `event` | [`EventKey`](dom-events.md#eventkey) | - |
| `listener` | (...`args`: `any`[]) => `void` | The callback function |

###### Returns

`this`

###### Inherited from

[`WritableStreamInner`](stream.md#writablestreaminner).[`prependOnceListener`](stream.md#prependoncelistener-4)

###### Call Signature

> **prependOnceListener**(`event`: `"close"`, `listener`: () => `void`): `this`

###### Parameters

| Parameter | Type |
| ------ | ------ |
| `event` | `"close"` |
| `listener` | () => `void` |

###### Returns

`this`

###### Inherited from

[`WritableStreamInner`](stream.md#writablestreaminner).[`prependOnceListener`](stream.md#prependoncelistener-4)

###### Call Signature

> **prependOnceListener**(`event`: `"error"`, `listener`: (`err`: `Error`) => `void`): `this`

###### Parameters

| Parameter | Type |
| ------ | ------ |
| `event` | `"error"` |
| `listener` | (`err`: `Error`) => `void` |

###### Returns

`this`

###### Inherited from

[`WritableStreamInner`](stream.md#writablestreaminner).[`prependOnceListener`](stream.md#prependoncelistener-4)

###### Call Signature

> **prependOnceListener**(`event`: `"finish"`, `listener`: () => `void`): `this`

###### Parameters

| Parameter | Type |
| ------ | ------ |
| `event` | `"finish"` |
| `listener` | () => `void` |

###### Returns

`this`

###### Inherited from

[`WritableStreamInner`](stream.md#writablestreaminner).[`prependOnceListener`](stream.md#prependoncelistener-4)

##### removeListener()

###### Call Signature

> **removeListener**(`event`: [`EventKey`](dom-events.md#eventkey), `listener`: (...`args`: `any`[]) => `void`): `this`

Removes the specified `listener` from the listener array for the event named `eventName`.

`removeListener()` will remove, at most, one instance of a listener from the
listener array. If any single listener has been added multiple times to the
listener array for the specified `eventName`, then `removeListener()` must be
called multiple times to remove each instance.

Once an event is emitted, all listeners attached to it at the time of emitting are called in order.
This implies that any `removeListener()` calls _after_ emitting and _before_ the last listener finishes execution
will not remove them from `emit()` in progress. Subsequent events behave as expected.

```js
import { EventEmitter } from 'events';
class MyEmitter extends EventEmitter {}
const myEmitter = new MyEmitter();

const callbackA = () => {
  console.log('A');
  myEmitter.removeListener('event', callbackB);
};

const callbackB = () => {
  console.log('B');
};

myEmitter.on('event', callbackA);

myEmitter.on('event', callbackB);

// callbackA removes listener callbackB but it will still be called.
// Internal listener array at time of emit [callbackA, callbackB]
myEmitter.emit('event');
// Prints:
//   A
//   B

// callbackB is now removed.
// Internal listener array [callbackA]
myEmitter.emit('event');
// Prints:
//   A
```

Because listeners are managed using an internal array, calling this will
change the position indices of any listener registered _after_ the listener
being removed. This will not impact the order in which listeners are called,
but it means that any copies of the listener array as returned by
the `emitter.listeners()` method will need to be recreated.

When a single function has been added as a handler multiple times for a single
event (as in the example below), `removeListener()` will remove the most
recently added instance. In the example the `once('ping')` listener is removed:

```js
import { EventEmitter } from 'events';
const ee = new EventEmitter();

function pong() {
  console.log('pong');
}

ee.on('ping', pong);
ee.once('ping', pong);
ee.removeListener('ping', pong);

ee.emit('ping');
ee.emit('ping');
```

Returns a reference to the `EventEmitter`, so that calls can be chained.

###### Parameters

| Parameter | Type |
| ------ | ------ |
| `event` | [`EventKey`](dom-events.md#eventkey) |
| `listener` | (...`args`: `any`[]) => `void` |

###### Returns

`this`

###### Inherited from

[`WritableStreamInner`](stream.md#writablestreaminner).[`removeListener`](stream.md#removelistener-4)

###### Call Signature

> **removeListener**(`event`: `"close"`, `listener`: () => `void`): `this`

###### Parameters

| Parameter | Type |
| ------ | ------ |
| `event` | `"close"` |
| `listener` | () => `void` |

###### Returns

`this`

###### Inherited from

[`WritableStreamInner`](stream.md#writablestreaminner).[`removeListener`](stream.md#removelistener-4)

###### Call Signature

> **removeListener**(`event`: `"error"`, `listener`: (`err`: `Error`) => `void`): `this`

###### Parameters

| Parameter | Type |
| ------ | ------ |
| `event` | `"error"` |
| `listener` | (`err`: `Error`) => `void` |

###### Returns

`this`

###### Inherited from

[`WritableStreamInner`](stream.md#writablestreaminner).[`removeListener`](stream.md#removelistener-4)

###### Call Signature

> **removeListener**(`event`: `"finish"`, `listener`: () => `void`): `this`

###### Parameters

| Parameter | Type |
| ------ | ------ |
| `event` | `"finish"` |
| `listener` | () => `void` |

###### Returns

`this`

###### Inherited from

[`WritableStreamInner`](stream.md#writablestreaminner).[`removeListener`](stream.md#removelistener-4)

##### write()

> **write**(`chunk`: `string` \| `ArrayBuffer` \| `SharedArrayBuffer` \| [`ArrayBufferView`](globals/namespaces/QuickJS.md#arraybufferview) \| [`Buffer`](buffer.md#buffer), `callback`?: (`error`?: `null` \| `Error`) => `void`): `void`

The `writable.write()` method writes some data to the stream, and calls the
supplied `callback` once the data has been fully handled. If an error
occurs, the `callback` will be called with the error as its
first argument. The `callback` is usually called asynchronously and before `'error'`
is emitted.

```js
function write(data, cb) {
  if (!stream.write(data)) {
    stream.once('drain', cb);
  } else {
    process.nextTick(cb);
  }
}

// Wait for cb to be called before doing any other write.
write('hello', () => {
  console.log('Write completed, do more writes now.');
});
```

A `Writable` stream in object mode will always ignore the `encoding` argument.

###### Parameters

| Parameter | Type | Description |
| ------ | ------ | ------ |
| `chunk` | `string` \| `ArrayBuffer` \| `SharedArrayBuffer` \| [`ArrayBufferView`](globals/namespaces/QuickJS.md#arraybufferview) \| [`Buffer`](buffer.md#buffer) | Optional data to write. `chunk` must be a {string}, {Buffer}, {TypedArray} or {DataView}. |
| `callback`? | (`error`?: `null` \| `Error`) => `void` | Callback for when this chunk of data is flushed. |

###### Returns

`void`

`false` if the stream wishes for the calling code to wait for the `'drain'` event to be emitted before continuing to write additional data; otherwise `true`.

###### Since

v0.9.4

###### Inherited from

[`WritableStreamInner`](stream.md#writablestreaminner).[`write`](stream.md#write-2)

***

### ReadableStreamInner

#### Extends

- [`EventEmitter`](globals/index.md#eventemittert)

#### Extended by

- [`DefaultReadableStream`](stream.md#defaultreadablestream)

#### Implements

- [`ReadableStream`](globals/namespaces/QuickJS.md#readablestream)

#### Constructors

##### new ReadableStreamInner()

> **new ReadableStreamInner**(): [`ReadableStreamInner`](stream.md#readablestreaminner)

###### Returns

[`ReadableStreamInner`](stream.md#readablestreaminner)

###### Inherited from

[`EventEmitter`](globals/index.md#eventemittert).[`constructor`](globals/index.md#constructors)

#### Methods

##### \[dispose\]()

> **\[dispose\]**(): `void`

Calls `readable.destroy()`.

###### Returns

`void`

##### addListener()

###### Call Signature

> **addListener**(`event`: [`EventKey`](dom-events.md#eventkey), `listener`: (...`args`: `any`[]) => `void`): `this`

Event emitter
The defined events on documents including:
1. close
2. data
3. end
4. error
5. readable

###### Parameters

| Parameter | Type |
| ------ | ------ |
| `event` | [`EventKey`](dom-events.md#eventkey) |
| `listener` | (...`args`: `any`[]) => `void` |

###### Returns

`this`

###### Implementation of

[`ReadableStream`](globals/namespaces/QuickJS.md#readablestream).[`addListener`](globals/namespaces/QuickJS.md#addlistener)

###### Overrides

[`EventEmitter`](globals/index.md#eventemittert).[`addListener`](globals/index.md#addlistener)

###### Call Signature

> **addListener**(`event`: `"close"`, `listener`: () => `void`): `this`

Event emitter
The defined events on documents including:
1. close
2. data
3. end
4. error
5. readable

###### Parameters

| Parameter | Type |
| ------ | ------ |
| `event` | `"close"` |
| `listener` | () => `void` |

###### Returns

`this`

###### Implementation of

`QuickJS.ReadableStream.addListener`

###### Overrides

`EventEmitter.addListener`

###### Call Signature

> **addListener**(`event`: `"data"`, `listener`: (`chunk`: [`Buffer`](buffer.md#buffer)) => `void`): `this`

Event emitter
The defined events on documents including:
1. close
2. data
3. end
4. error
5. readable

###### Parameters

| Parameter | Type |
| ------ | ------ |
| `event` | `"data"` |
| `listener` | (`chunk`: [`Buffer`](buffer.md#buffer)) => `void` |

###### Returns

`this`

###### Implementation of

`QuickJS.ReadableStream.addListener`

###### Overrides

`EventEmitter.addListener`

###### Call Signature

> **addListener**(`event`: `"end"`, `listener`: () => `void`): `this`

Event emitter
The defined events on documents including:
1. close
2. data
3. end
4. error
5. readable

###### Parameters

| Parameter | Type |
| ------ | ------ |
| `event` | `"end"` |
| `listener` | () => `void` |

###### Returns

`this`

###### Implementation of

`QuickJS.ReadableStream.addListener`

###### Overrides

`EventEmitter.addListener`

###### Call Signature

> **addListener**(`event`: `"error"`, `listener`: (`err`: `Error`) => `void`): `this`

Event emitter
The defined events on documents including:
1. close
2. data
3. end
4. error
5. readable

###### Parameters

| Parameter | Type |
| ------ | ------ |
| `event` | `"error"` |
| `listener` | (`err`: `Error`) => `void` |

###### Returns

`this`

###### Implementation of

`QuickJS.ReadableStream.addListener`

###### Overrides

`EventEmitter.addListener`

###### Call Signature

> **addListener**(`event`: `"readable"`, `listener`: () => `void`): `this`

Event emitter
The defined events on documents including:
1. close
2. data
3. end
4. error
5. readable

###### Parameters

| Parameter | Type |
| ------ | ------ |
| `event` | `"readable"` |
| `listener` | () => `void` |

###### Returns

`this`

###### Implementation of

`QuickJS.ReadableStream.addListener`

###### Overrides

`EventEmitter.addListener`

##### destroy()

> **destroy**(`error`?: `Error`): `this`

Destroy the stream. Optionally emit an `'error'` event, and emit a `'close'` event. After this call, the readable
stream will release any internal resources and subsequent calls to `push()` will be ignored.

Once `destroy()` has been called any further calls will be a no-op and no
further errors except from `_destroy()` may be emitted as `'error'`.

Implementors should not override this method, but instead implement `readable._destroy()`.

###### Parameters

| Parameter | Type | Description |
| ------ | ------ | ------ |
| `error`? | `Error` | Error which will be passed as payload in `'error'` event |

###### Returns

`this`

##### emit()

###### Call Signature

> **emit**(`event`: [`EventKey`](dom-events.md#eventkey), ...`args`: `any`[]): `boolean`

Synchronously calls each of the listeners registered for the event named `eventName`, in the order they were registered, passing the supplied arguments
to each.

```js
import { EventEmitter } from 'events';
const myEmitter = new EventEmitter();

// First listener
myEmitter.on('event', function firstListener() {
  console.log('Helloooo! first listener');
});
// Second listener
myEmitter.on('event', function secondListener(arg1, arg2) {
  console.log(`event with parameters ${arg1}, ${arg2} in second listener`);
});
// Third listener
myEmitter.on('event', function thirdListener(...args) {
  const parameters = args.join(', ');
  console.log(`event with parameters ${parameters} in third listener`);
});

myEmitter.emit('event', 1, 2, 3, 4, 5);

// Prints:
// Helloooo! first listener
// event with parameters 1, 2 in second listener
// event with parameters 1, 2, 3, 4, 5 in third listener
```

###### Parameters

| Parameter | Type |
| ------ | ------ |
| `event` | [`EventKey`](dom-events.md#eventkey) |
| ...`args` | `any`[] |

###### Returns

`boolean`

###### Implementation of

[`ReadableStream`](globals/namespaces/QuickJS.md#readablestream).[`emit`](globals/namespaces/QuickJS.md#emit)

###### Overrides

[`EventEmitter`](globals/index.md#eventemittert).[`emit`](globals/index.md#emit)

###### Call Signature

> **emit**(`event`: `"close"`): `boolean`

###### Parameters

| Parameter | Type |
| ------ | ------ |
| `event` | `"close"` |

###### Returns

`boolean`

###### Implementation of

`QuickJS.ReadableStream.emit`

###### Overrides

`EventEmitter.emit`

###### Call Signature

> **emit**(`event`: `"data"`, `chunk`: [`Buffer`](buffer.md#buffer)): `boolean`

###### Parameters

| Parameter | Type |
| ------ | ------ |
| `event` | `"data"` |
| `chunk` | [`Buffer`](buffer.md#buffer) |

###### Returns

`boolean`

###### Implementation of

`QuickJS.ReadableStream.emit`

###### Overrides

`EventEmitter.emit`

###### Call Signature

> **emit**(`event`: `"end"`): `boolean`

###### Parameters

| Parameter | Type |
| ------ | ------ |
| `event` | `"end"` |

###### Returns

`boolean`

###### Implementation of

`QuickJS.ReadableStream.emit`

###### Overrides

`EventEmitter.emit`

###### Call Signature

> **emit**(`event`: `"error"`, `err`: `Error`): `boolean`

###### Parameters

| Parameter | Type |
| ------ | ------ |
| `event` | `"error"` |
| `err` | `Error` |

###### Returns

`boolean`

###### Implementation of

`QuickJS.ReadableStream.emit`

###### Overrides

`EventEmitter.emit`

###### Call Signature

> **emit**(`event`: `"readable"`): `boolean`

###### Parameters

| Parameter | Type |
| ------ | ------ |
| `event` | `"readable"` |

###### Returns

`boolean`

###### Implementation of

`QuickJS.ReadableStream.emit`

###### Overrides

`EventEmitter.emit`

##### eventNames()

> **eventNames**(): [`EventKey`](dom-events.md#eventkey)[]

Returns an array listing the events for which the emitter has registered
listeners. The values in the array are strings or `Symbol`s.

```js
import { EventEmitter } from 'events';

const myEE = new EventEmitter();
myEE.on('foo', () => {});
myEE.on('bar', () => {});

const sym = Symbol('symbol');
myEE.on(sym, () => {});

console.log(myEE.eventNames());
// Prints: [ 'foo', 'bar', Symbol(symbol) ]
```

###### Returns

[`EventKey`](dom-events.md#eventkey)[]

###### Implementation of

[`ReadableStream`](globals/namespaces/QuickJS.md#readablestream).[`eventNames`](globals/namespaces/QuickJS.md#eventnames)

###### Inherited from

[`EventEmitter`](globals/index.md#eventemittert).[`eventNames`](globals/index.md#eventnames)

##### off()

> **off**\<`K`\>(`eventName`: [`EventKey`](dom-events.md#eventkey), `listener`: (...`args`: `any`[]) => `void`): `this`

Alias for `emitter.removeListener()`.

###### Type Parameters

| Type Parameter |
| ------ |
| `K` |

###### Parameters

| Parameter | Type |
| ------ | ------ |
| `eventName` | [`EventKey`](dom-events.md#eventkey) |
| `listener` | (...`args`: `any`[]) => `void` |

###### Returns

`this`

###### Implementation of

[`ReadableStream`](globals/namespaces/QuickJS.md#readablestream).[`off`](globals/namespaces/QuickJS.md#off)

###### Inherited from

[`EventEmitter`](globals/index.md#eventemittert).[`off`](globals/index.md#off)

##### on()

###### Call Signature

> **on**(`event`: [`EventKey`](dom-events.md#eventkey), `listener`: (...`args`: `any`[]) => `void`): `this`

Adds the `listener` function to the end of the listeners array for the event
named `eventName`. No checks are made to see if the `listener` has already
been added. Multiple calls passing the same combination of `eventName` and
`listener` will result in the `listener` being added, and called, multiple times.

```js
server.on('connection', (stream) => {
  console.log('someone connected!');
});
```

Returns a reference to the `EventEmitter`, so that calls can be chained.

By default, event listeners are invoked in the order they are added. The `emitter.prependListener()` method can be used as an alternative to add the
event listener to the beginning of the listeners array.

```js
import { EventEmitter } from 'events';
const myEE = new EventEmitter();
myEE.on('foo', () => console.log('a'));
myEE.prependListener('foo', () => console.log('b'));
myEE.emit('foo');
// Prints:
//   b
//   a
```

###### Parameters

| Parameter | Type | Description |
| ------ | ------ | ------ |
| `event` | [`EventKey`](dom-events.md#eventkey) | - |
| `listener` | (...`args`: `any`[]) => `void` | The callback function |

###### Returns

`this`

###### Implementation of

[`ReadableStream`](globals/namespaces/QuickJS.md#readablestream).[`on`](globals/namespaces/QuickJS.md#on)

###### Overrides

[`EventEmitter`](globals/index.md#eventemittert).[`on`](globals/index.md#on)

###### Call Signature

> **on**(`event`: `"close"`, `listener`: () => `void`): `this`

###### Parameters

| Parameter | Type |
| ------ | ------ |
| `event` | `"close"` |
| `listener` | () => `void` |

###### Returns

`this`

###### Implementation of

`QuickJS.ReadableStream.on`

###### Overrides

`EventEmitter.on`

###### Call Signature

> **on**(`event`: `"data"`, `listener`: (`chunk`: [`Buffer`](buffer.md#buffer)) => `void`): `this`

###### Parameters

| Parameter | Type |
| ------ | ------ |
| `event` | `"data"` |
| `listener` | (`chunk`: [`Buffer`](buffer.md#buffer)) => `void` |

###### Returns

`this`

###### Implementation of

`QuickJS.ReadableStream.on`

###### Overrides

`EventEmitter.on`

###### Call Signature

> **on**(`event`: `"end"`, `listener`: () => `void`): `this`

###### Parameters

| Parameter | Type |
| ------ | ------ |
| `event` | `"end"` |
| `listener` | () => `void` |

###### Returns

`this`

###### Implementation of

`QuickJS.ReadableStream.on`

###### Overrides

`EventEmitter.on`

###### Call Signature

> **on**(`event`: `"error"`, `listener`: (`err`: `Error`) => `void`): `this`

###### Parameters

| Parameter | Type |
| ------ | ------ |
| `event` | `"error"` |
| `listener` | (`err`: `Error`) => `void` |

###### Returns

`this`

###### Implementation of

`QuickJS.ReadableStream.on`

###### Overrides

`EventEmitter.on`

###### Call Signature

> **on**(`event`: `"readable"`, `listener`: () => `void`): `this`

###### Parameters

| Parameter | Type |
| ------ | ------ |
| `event` | `"readable"` |
| `listener` | () => `void` |

###### Returns

`this`

###### Implementation of

`QuickJS.ReadableStream.on`

###### Overrides

`EventEmitter.on`

##### once()

###### Call Signature

> **once**(`event`: [`EventKey`](dom-events.md#eventkey), `listener`: (...`args`: `any`[]) => `void`): `this`

Adds a **one-time** `listener` function for the event named `eventName`. The
next time `eventName` is triggered, this listener is removed and then invoked.

Returns a reference to the `EventEmitter`, so that calls can be chained.

By default, event listeners are invoked in the order they are added. The `emitter.prependOnceListener()` method can be used as an alternative to add the
event listener to the beginning of the listeners array.

```js
import { EventEmitter } from 'events';
const myEE = new EventEmitter();
myEE.once('foo', () => console.log('a'));
myEE.prependOnceListener('foo', () => console.log('b'));
myEE.emit('foo');
// Prints:
//   b
//   a
```

###### Parameters

| Parameter | Type | Description |
| ------ | ------ | ------ |
| `event` | [`EventKey`](dom-events.md#eventkey) | - |
| `listener` | (...`args`: `any`[]) => `void` | The callback function |

###### Returns

`this`

###### Since

v0.3.0

###### Implementation of

[`ReadableStream`](globals/namespaces/QuickJS.md#readablestream).[`once`](globals/namespaces/QuickJS.md#once)

###### Overrides

[`EventEmitter`](globals/index.md#eventemittert).[`once`](globals/index.md#once)

###### Call Signature

> **once**(`event`: `"close"`, `listener`: () => `void`): `this`

###### Parameters

| Parameter | Type |
| ------ | ------ |
| `event` | `"close"` |
| `listener` | () => `void` |

###### Returns

`this`

###### Implementation of

`QuickJS.ReadableStream.once`

###### Overrides

`EventEmitter.once`

###### Call Signature

> **once**(`event`: `"data"`, `listener`: (`chunk`: [`Buffer`](buffer.md#buffer)) => `void`): `this`

###### Parameters

| Parameter | Type |
| ------ | ------ |
| `event` | `"data"` |
| `listener` | (`chunk`: [`Buffer`](buffer.md#buffer)) => `void` |

###### Returns

`this`

###### Implementation of

`QuickJS.ReadableStream.once`

###### Overrides

`EventEmitter.once`

###### Call Signature

> **once**(`event`: `"end"`, `listener`: () => `void`): `this`

###### Parameters

| Parameter | Type |
| ------ | ------ |
| `event` | `"end"` |
| `listener` | () => `void` |

###### Returns

`this`

###### Implementation of

`QuickJS.ReadableStream.once`

###### Overrides

`EventEmitter.once`

###### Call Signature

> **once**(`event`: `"error"`, `listener`: (`err`: `Error`) => `void`): `this`

###### Parameters

| Parameter | Type |
| ------ | ------ |
| `event` | `"error"` |
| `listener` | (`err`: `Error`) => `void` |

###### Returns

`this`

###### Implementation of

`QuickJS.ReadableStream.once`

###### Overrides

`EventEmitter.once`

###### Call Signature

> **once**(`event`: `"readable"`, `listener`: () => `void`): `this`

###### Parameters

| Parameter | Type |
| ------ | ------ |
| `event` | `"readable"` |
| `listener` | () => `void` |

###### Returns

`this`

###### Implementation of

`QuickJS.ReadableStream.once`

###### Overrides

`EventEmitter.once`

##### prependListener()

###### Call Signature

> **prependListener**(`event`: [`EventKey`](dom-events.md#eventkey), `listener`: (...`args`: `any`[]) => `void`): `this`

Adds the `listener` function to the _beginning_ of the listeners array for the
event named `eventName`. No checks are made to see if the `listener` has
already been added. Multiple calls passing the same combination of `eventName`
and `listener` will result in the `listener` being added, and called, multiple times.

Returns a reference to the `EventEmitter`, so that calls can be chained.

###### Parameters

| Parameter | Type | Description |
| ------ | ------ | ------ |
| `event` | [`EventKey`](dom-events.md#eventkey) | - |
| `listener` | (...`args`: `any`[]) => `void` | The callback function |

###### Returns

`this`

###### Implementation of

[`ReadableStream`](globals/namespaces/QuickJS.md#readablestream).[`prependListener`](globals/namespaces/QuickJS.md#prependlistener)

###### Overrides

[`EventEmitter`](globals/index.md#eventemittert).[`prependListener`](globals/index.md#prependlistener)

###### Call Signature

> **prependListener**(`event`: `"close"`, `listener`: () => `void`): `this`

###### Parameters

| Parameter | Type |
| ------ | ------ |
| `event` | `"close"` |
| `listener` | () => `void` |

###### Returns

`this`

###### Implementation of

`QuickJS.ReadableStream.prependListener`

###### Overrides

`EventEmitter.prependListener`

###### Call Signature

> **prependListener**(`event`: `"data"`, `listener`: (`chunk`: [`Buffer`](buffer.md#buffer)) => `void`): `this`

###### Parameters

| Parameter | Type |
| ------ | ------ |
| `event` | `"data"` |
| `listener` | (`chunk`: [`Buffer`](buffer.md#buffer)) => `void` |

###### Returns

`this`

###### Implementation of

`QuickJS.ReadableStream.prependListener`

###### Overrides

`EventEmitter.prependListener`

###### Call Signature

> **prependListener**(`event`: `"end"`, `listener`: () => `void`): `this`

###### Parameters

| Parameter | Type |
| ------ | ------ |
| `event` | `"end"` |
| `listener` | () => `void` |

###### Returns

`this`

###### Implementation of

`QuickJS.ReadableStream.prependListener`

###### Overrides

`EventEmitter.prependListener`

###### Call Signature

> **prependListener**(`event`: `"error"`, `listener`: (`err`: `Error`) => `void`): `this`

###### Parameters

| Parameter | Type |
| ------ | ------ |
| `event` | `"error"` |
| `listener` | (`err`: `Error`) => `void` |

###### Returns

`this`

###### Implementation of

`QuickJS.ReadableStream.prependListener`

###### Overrides

`EventEmitter.prependListener`

###### Call Signature

> **prependListener**(`event`: `"readable"`, `listener`: () => `void`): `this`

###### Parameters

| Parameter | Type |
| ------ | ------ |
| `event` | `"readable"` |
| `listener` | () => `void` |

###### Returns

`this`

###### Implementation of

`QuickJS.ReadableStream.prependListener`

###### Overrides

`EventEmitter.prependListener`

##### prependOnceListener()

###### Call Signature

> **prependOnceListener**(`event`: [`EventKey`](dom-events.md#eventkey), `listener`: (...`args`: `any`[]) => `void`): `this`

Adds a **one-time**`listener` function for the event named `eventName` to the _beginning_ of the listeners array.
The next time `eventName` is triggered, this listener is removed, and then invoked.

Returns a reference to the `EventEmitter`, so that calls can be chained.

###### Parameters

| Parameter | Type | Description |
| ------ | ------ | ------ |
| `event` | [`EventKey`](dom-events.md#eventkey) | - |
| `listener` | (...`args`: `any`[]) => `void` | The callback function |

###### Returns

`this`

###### Implementation of

[`ReadableStream`](globals/namespaces/QuickJS.md#readablestream).[`prependOnceListener`](globals/namespaces/QuickJS.md#prependoncelistener)

###### Overrides

[`EventEmitter`](globals/index.md#eventemittert).[`prependOnceListener`](globals/index.md#prependoncelistener)

###### Call Signature

> **prependOnceListener**(`event`: `"close"`, `listener`: () => `void`): `this`

###### Parameters

| Parameter | Type |
| ------ | ------ |
| `event` | `"close"` |
| `listener` | () => `void` |

###### Returns

`this`

###### Implementation of

`QuickJS.ReadableStream.prependOnceListener`

###### Overrides

`EventEmitter.prependOnceListener`

###### Call Signature

> **prependOnceListener**(`event`: `"data"`, `listener`: (`chunk`: [`Buffer`](buffer.md#buffer)) => `void`): `this`

###### Parameters

| Parameter | Type |
| ------ | ------ |
| `event` | `"data"` |
| `listener` | (`chunk`: [`Buffer`](buffer.md#buffer)) => `void` |

###### Returns

`this`

###### Implementation of

`QuickJS.ReadableStream.prependOnceListener`

###### Overrides

`EventEmitter.prependOnceListener`

###### Call Signature

> **prependOnceListener**(`event`: `"end"`, `listener`: () => `void`): `this`

###### Parameters

| Parameter | Type |
| ------ | ------ |
| `event` | `"end"` |
| `listener` | () => `void` |

###### Returns

`this`

###### Implementation of

`QuickJS.ReadableStream.prependOnceListener`

###### Overrides

`EventEmitter.prependOnceListener`

###### Call Signature

> **prependOnceListener**(`event`: `"error"`, `listener`: (`err`: `Error`) => `void`): `this`

###### Parameters

| Parameter | Type |
| ------ | ------ |
| `event` | `"error"` |
| `listener` | (`err`: `Error`) => `void` |

###### Returns

`this`

###### Implementation of

`QuickJS.ReadableStream.prependOnceListener`

###### Overrides

`EventEmitter.prependOnceListener`

###### Call Signature

> **prependOnceListener**(`event`: `"readable"`, `listener`: () => `void`): `this`

###### Parameters

| Parameter | Type |
| ------ | ------ |
| `event` | `"readable"` |
| `listener` | () => `void` |

###### Returns

`this`

###### Implementation of

`QuickJS.ReadableStream.prependOnceListener`

###### Overrides

`EventEmitter.prependOnceListener`

##### read()

> **read**(`size`?: `number`): `null` \| [`Buffer`](buffer.md#buffer)

The `readable.read()` method reads data out of the internal buffer and
returns it. If no data is available to be read, `null` is returned. By default,
the data is returned as a `Buffer` object unless an encoding has been
specified using the `readable.setEncoding()` method or the stream is operating
in object mode.

The optional `size` argument specifies a specific number of bytes to read. If
`size` bytes are not available to be read, `null` will be returned _unless_ the
stream has ended, in which case all of the data remaining in the internal buffer
will be returned.

If the `size` argument is not specified, all of the data contained in the
internal buffer will be returned.

The `size` argument must be less than or equal to 1 GiB.

The `readable.read()` method should only be called on `Readable` streams
operating in paused mode. In flowing mode, `readable.read()` is called
automatically until the internal buffer is fully drained.

```js
const readable = getReadableStreamSomehow();

// 'readable' may be triggered multiple times as data is buffered in
readable.on('readable', () => {
  let chunk;
  console.log('Stream is readable (new data received in buffer)');
  // Use a loop to make sure we read all currently available data
  while (null !== (chunk = readable.read())) {
    console.log(`Read ${chunk.length} bytes of data...`);
  }
});

// 'end' will be triggered once when there is no more data available
readable.on('end', () => {
  console.log('Reached end of stream.');
});
```

Each call to `readable.read()` returns a chunk of data, or `null`. The chunks
are not concatenated. A `while` loop is necessary to consume all data
currently in the buffer. When reading a large file `.read()` may return `null`,
having consumed all buffered content so far, but there is still more data to
come not yet buffered. In this case a new `'readable'` event will be emitted
when there is more data in the buffer. Finally the `'end'` event will be
emitted when there is no more data to come.

Therefore to read a file's whole contents from a `readable`, it is necessary
to collect chunks across multiple `'readable'` events:

```js
const chunks = [];

readable.on('readable', () => {
  let chunk;
  while (null !== (chunk = readable.read())) {
    chunks.push(chunk);
  }
});

readable.on('end', () => {
  const content = chunks.join('');
});
```

A `Readable` stream in object mode will always return a single item from
a call to `readable.read(size)`, regardless of the value of the `size` argument.

If the `readable.read()` method returns a chunk of data, a `'data'` event will
also be emitted.

Calling [read](stream.md#read-2) after the `'end'` event has
been emitted will return `null`. No runtime error will be raised.

###### Parameters

| Parameter | Type | Description |
| ------ | ------ | ------ |
| `size`? | `number` | Optional argument to specify how much data to read. |

###### Returns

`null` \| [`Buffer`](buffer.md#buffer)

###### Implementation of

[`ReadableStream`](globals/namespaces/QuickJS.md#readablestream).[`read`](globals/namespaces/QuickJS.md#read)

##### removeListener()

###### Call Signature

> **removeListener**(`event`: [`EventKey`](dom-events.md#eventkey), `listener`: (...`args`: `any`[]) => `void`): `this`

Removes the specified `listener` from the listener array for the event named `eventName`.

`removeListener()` will remove, at most, one instance of a listener from the
listener array. If any single listener has been added multiple times to the
listener array for the specified `eventName`, then `removeListener()` must be
called multiple times to remove each instance.

Once an event is emitted, all listeners attached to it at the time of emitting are called in order.
This implies that any `removeListener()` calls _after_ emitting and _before_ the last listener finishes execution
will not remove them from `emit()` in progress. Subsequent events behave as expected.

```js
import { EventEmitter } from 'events';
class MyEmitter extends EventEmitter {}
const myEmitter = new MyEmitter();

const callbackA = () => {
  console.log('A');
  myEmitter.removeListener('event', callbackB);
};

const callbackB = () => {
  console.log('B');
};

myEmitter.on('event', callbackA);

myEmitter.on('event', callbackB);

// callbackA removes listener callbackB but it will still be called.
// Internal listener array at time of emit [callbackA, callbackB]
myEmitter.emit('event');
// Prints:
//   A
//   B

// callbackB is now removed.
// Internal listener array [callbackA]
myEmitter.emit('event');
// Prints:
//   A
```

Because listeners are managed using an internal array, calling this will
change the position indices of any listener registered _after_ the listener
being removed. This will not impact the order in which listeners are called,
but it means that any copies of the listener array as returned by
the `emitter.listeners()` method will need to be recreated.

When a single function has been added as a handler multiple times for a single
event (as in the example below), `removeListener()` will remove the most
recently added instance. In the example the `once('ping')` listener is removed:

```js
import { EventEmitter } from 'events';
const ee = new EventEmitter();

function pong() {
  console.log('pong');
}

ee.on('ping', pong);
ee.once('ping', pong);
ee.removeListener('ping', pong);

ee.emit('ping');
ee.emit('ping');
```

Returns a reference to the `EventEmitter`, so that calls can be chained.

###### Parameters

| Parameter | Type |
| ------ | ------ |
| `event` | [`EventKey`](dom-events.md#eventkey) |
| `listener` | (...`args`: `any`[]) => `void` |

###### Returns

`this`

###### Implementation of

[`ReadableStream`](globals/namespaces/QuickJS.md#readablestream).[`removeListener`](globals/namespaces/QuickJS.md#removelistener)

###### Overrides

[`EventEmitter`](globals/index.md#eventemittert).[`removeListener`](globals/index.md#removelistener)

###### Call Signature

> **removeListener**(`event`: `"close"`, `listener`: () => `void`): `this`

###### Parameters

| Parameter | Type |
| ------ | ------ |
| `event` | `"close"` |
| `listener` | () => `void` |

###### Returns

`this`

###### Implementation of

`QuickJS.ReadableStream.removeListener`

###### Overrides

`EventEmitter.removeListener`

###### Call Signature

> **removeListener**(`event`: `"data"`, `listener`: (`chunk`: [`Buffer`](buffer.md#buffer)) => `void`): `this`

###### Parameters

| Parameter | Type |
| ------ | ------ |
| `event` | `"data"` |
| `listener` | (`chunk`: [`Buffer`](buffer.md#buffer)) => `void` |

###### Returns

`this`

###### Implementation of

`QuickJS.ReadableStream.removeListener`

###### Overrides

`EventEmitter.removeListener`

###### Call Signature

> **removeListener**(`event`: `"end"`, `listener`: () => `void`): `this`

###### Parameters

| Parameter | Type |
| ------ | ------ |
| `event` | `"end"` |
| `listener` | () => `void` |

###### Returns

`this`

###### Implementation of

`QuickJS.ReadableStream.removeListener`

###### Overrides

`EventEmitter.removeListener`

###### Call Signature

> **removeListener**(`event`: `"error"`, `listener`: (`err`: `Error`) => `void`): `this`

###### Parameters

| Parameter | Type |
| ------ | ------ |
| `event` | `"error"` |
| `listener` | (`err`: `Error`) => `void` |

###### Returns

`this`

###### Implementation of

`QuickJS.ReadableStream.removeListener`

###### Overrides

`EventEmitter.removeListener`

###### Call Signature

> **removeListener**(`event`: `"readable"`, `listener`: () => `void`): `this`

###### Parameters

| Parameter | Type |
| ------ | ------ |
| `event` | `"readable"` |
| `listener` | () => `void` |

###### Returns

`this`

###### Implementation of

`QuickJS.ReadableStream.removeListener`

###### Overrides

`EventEmitter.removeListener`

***

### WritableStreamInner

#### Extends

- [`EventEmitter`](globals/index.md#eventemittert)

#### Extended by

- [`DefaultWritableStream`](stream.md#defaultwritablestream)

#### Implements

- [`WritableStream`](globals/namespaces/QuickJS.md#writablestream)

#### Constructors

##### new WritableStreamInner()

> **new WritableStreamInner**(): [`WritableStreamInner`](stream.md#writablestreaminner)

###### Returns

[`WritableStreamInner`](stream.md#writablestreaminner)

###### Inherited from

[`EventEmitter`](globals/index.md#eventemittert).[`constructor`](globals/index.md#constructors)

#### Methods

##### addListener()

###### Call Signature

> **addListener**(`event`: [`EventKey`](dom-events.md#eventkey), `listener`: (...`args`: `any`[]) => `void`): `this`

Event emitter
The defined events on documents including:
1. close
2. error
3. finish

###### Parameters

| Parameter | Type |
| ------ | ------ |
| `event` | [`EventKey`](dom-events.md#eventkey) |
| `listener` | (...`args`: `any`[]) => `void` |

###### Returns

`this`

###### Implementation of

[`WritableStream`](globals/namespaces/QuickJS.md#writablestream).[`addListener`](globals/namespaces/QuickJS.md#addlistener-1)

###### Overrides

[`EventEmitter`](globals/index.md#eventemittert).[`addListener`](globals/index.md#addlistener)

###### Call Signature

> **addListener**(`event`: `"close"`, `listener`: () => `void`): `this`

Event emitter
The defined events on documents including:
1. close
2. error
3. finish

###### Parameters

| Parameter | Type |
| ------ | ------ |
| `event` | `"close"` |
| `listener` | () => `void` |

###### Returns

`this`

###### Implementation of

`QuickJS.WritableStream.addListener`

###### Overrides

`EventEmitter.addListener`

###### Call Signature

> **addListener**(`event`: `"error"`, `listener`: (`err`: `Error`) => `void`): `this`

Event emitter
The defined events on documents including:
1. close
2. error
3. finish

###### Parameters

| Parameter | Type |
| ------ | ------ |
| `event` | `"error"` |
| `listener` | (`err`: `Error`) => `void` |

###### Returns

`this`

###### Implementation of

`QuickJS.WritableStream.addListener`

###### Overrides

`EventEmitter.addListener`

###### Call Signature

> **addListener**(`event`: `"finish"`, `listener`: () => `void`): `this`

Event emitter
The defined events on documents including:
1. close
2. error
3. finish

###### Parameters

| Parameter | Type |
| ------ | ------ |
| `event` | `"finish"` |
| `listener` | () => `void` |

###### Returns

`this`

###### Implementation of

`QuickJS.WritableStream.addListener`

###### Overrides

`EventEmitter.addListener`

##### emit()

###### Call Signature

> **emit**(`event`: [`EventKey`](dom-events.md#eventkey), ...`args`: `any`[]): `boolean`

Synchronously calls each of the listeners registered for the event named `eventName`, in the order they were registered, passing the supplied arguments
to each.

```js
import { EventEmitter } from 'events';
const myEmitter = new EventEmitter();

// First listener
myEmitter.on('event', function firstListener() {
  console.log('Helloooo! first listener');
});
// Second listener
myEmitter.on('event', function secondListener(arg1, arg2) {
  console.log(`event with parameters ${arg1}, ${arg2} in second listener`);
});
// Third listener
myEmitter.on('event', function thirdListener(...args) {
  const parameters = args.join(', ');
  console.log(`event with parameters ${parameters} in third listener`);
});

myEmitter.emit('event', 1, 2, 3, 4, 5);

// Prints:
// Helloooo! first listener
// event with parameters 1, 2 in second listener
// event with parameters 1, 2, 3, 4, 5 in third listener
```

###### Parameters

| Parameter | Type |
| ------ | ------ |
| `event` | [`EventKey`](dom-events.md#eventkey) |
| ...`args` | `any`[] |

###### Returns

`boolean`

###### Implementation of

[`WritableStream`](globals/namespaces/QuickJS.md#writablestream).[`emit`](globals/namespaces/QuickJS.md#emit-1)

###### Overrides

[`EventEmitter`](globals/index.md#eventemittert).[`emit`](globals/index.md#emit)

###### Call Signature

> **emit**(`event`: `"close"`): `boolean`

###### Parameters

| Parameter | Type |
| ------ | ------ |
| `event` | `"close"` |

###### Returns

`boolean`

###### Implementation of

`QuickJS.WritableStream.emit`

###### Overrides

`EventEmitter.emit`

###### Call Signature

> **emit**(`event`: `"error"`, `err`: `Error`): `boolean`

###### Parameters

| Parameter | Type |
| ------ | ------ |
| `event` | `"error"` |
| `err` | `Error` |

###### Returns

`boolean`

###### Implementation of

`QuickJS.WritableStream.emit`

###### Overrides

`EventEmitter.emit`

###### Call Signature

> **emit**(`event`: `"finish"`): `boolean`

###### Parameters

| Parameter | Type |
| ------ | ------ |
| `event` | `"finish"` |

###### Returns

`boolean`

###### Implementation of

`QuickJS.WritableStream.emit`

###### Overrides

`EventEmitter.emit`

##### end()

> **end**(): `this`

Calling the `writable.end()` method signals that no more data will be written
to the `Writable`.

Calling the [write](stream.md#write-2) method after calling [end](stream.md#end-2) will raise an error.

###### Returns

`this`

###### Implementation of

[`WritableStream`](globals/namespaces/QuickJS.md#writablestream).[`end`](globals/namespaces/QuickJS.md#end)

##### eventNames()

> **eventNames**(): [`EventKey`](dom-events.md#eventkey)[]

Returns an array listing the events for which the emitter has registered
listeners. The values in the array are strings or `Symbol`s.

```js
import { EventEmitter } from 'events';

const myEE = new EventEmitter();
myEE.on('foo', () => {});
myEE.on('bar', () => {});

const sym = Symbol('symbol');
myEE.on(sym, () => {});

console.log(myEE.eventNames());
// Prints: [ 'foo', 'bar', Symbol(symbol) ]
```

###### Returns

[`EventKey`](dom-events.md#eventkey)[]

###### Implementation of

[`WritableStream`](globals/namespaces/QuickJS.md#writablestream).[`eventNames`](globals/namespaces/QuickJS.md#eventnames-1)

###### Inherited from

[`EventEmitter`](globals/index.md#eventemittert).[`eventNames`](globals/index.md#eventnames)

##### off()

> **off**\<`K`\>(`eventName`: [`EventKey`](dom-events.md#eventkey), `listener`: (...`args`: `any`[]) => `void`): `this`

Alias for `emitter.removeListener()`.

###### Type Parameters

| Type Parameter |
| ------ |
| `K` |

###### Parameters

| Parameter | Type |
| ------ | ------ |
| `eventName` | [`EventKey`](dom-events.md#eventkey) |
| `listener` | (...`args`: `any`[]) => `void` |

###### Returns

`this`

###### Implementation of

[`WritableStream`](globals/namespaces/QuickJS.md#writablestream).[`off`](globals/namespaces/QuickJS.md#off-1)

###### Inherited from

[`EventEmitter`](globals/index.md#eventemittert).[`off`](globals/index.md#off)

##### on()

###### Call Signature

> **on**(`event`: [`EventKey`](dom-events.md#eventkey), `listener`: (...`args`: `any`[]) => `void`): `this`

Adds the `listener` function to the end of the listeners array for the event
named `eventName`. No checks are made to see if the `listener` has already
been added. Multiple calls passing the same combination of `eventName` and
`listener` will result in the `listener` being added, and called, multiple times.

```js
server.on('connection', (stream) => {
  console.log('someone connected!');
});
```

Returns a reference to the `EventEmitter`, so that calls can be chained.

By default, event listeners are invoked in the order they are added. The `emitter.prependListener()` method can be used as an alternative to add the
event listener to the beginning of the listeners array.

```js
import { EventEmitter } from 'events';
const myEE = new EventEmitter();
myEE.on('foo', () => console.log('a'));
myEE.prependListener('foo', () => console.log('b'));
myEE.emit('foo');
// Prints:
//   b
//   a
```

###### Parameters

| Parameter | Type | Description |
| ------ | ------ | ------ |
| `event` | [`EventKey`](dom-events.md#eventkey) | - |
| `listener` | (...`args`: `any`[]) => `void` | The callback function |

###### Returns

`this`

###### Implementation of

[`WritableStream`](globals/namespaces/QuickJS.md#writablestream).[`on`](globals/namespaces/QuickJS.md#on-1)

###### Overrides

[`EventEmitter`](globals/index.md#eventemittert).[`on`](globals/index.md#on)

###### Call Signature

> **on**(`event`: `"close"`, `listener`: () => `void`): `this`

###### Parameters

| Parameter | Type |
| ------ | ------ |
| `event` | `"close"` |
| `listener` | () => `void` |

###### Returns

`this`

###### Implementation of

`QuickJS.WritableStream.on`

###### Overrides

`EventEmitter.on`

###### Call Signature

> **on**(`event`: `"error"`, `listener`: (`err`: `Error`) => `void`): `this`

###### Parameters

| Parameter | Type |
| ------ | ------ |
| `event` | `"error"` |
| `listener` | (`err`: `Error`) => `void` |

###### Returns

`this`

###### Implementation of

`QuickJS.WritableStream.on`

###### Overrides

`EventEmitter.on`

###### Call Signature

> **on**(`event`: `"finish"`, `listener`: () => `void`): `this`

###### Parameters

| Parameter | Type |
| ------ | ------ |
| `event` | `"finish"` |
| `listener` | () => `void` |

###### Returns

`this`

###### Implementation of

`QuickJS.WritableStream.on`

###### Overrides

`EventEmitter.on`

##### once()

###### Call Signature

> **once**(`event`: [`EventKey`](dom-events.md#eventkey), `listener`: (...`args`: `any`[]) => `void`): `this`

Adds a **one-time** `listener` function for the event named `eventName`. The
next time `eventName` is triggered, this listener is removed and then invoked.

Returns a reference to the `EventEmitter`, so that calls can be chained.

By default, event listeners are invoked in the order they are added. The `emitter.prependOnceListener()` method can be used as an alternative to add the
event listener to the beginning of the listeners array.

```js
import { EventEmitter } from 'events';
const myEE = new EventEmitter();
myEE.once('foo', () => console.log('a'));
myEE.prependOnceListener('foo', () => console.log('b'));
myEE.emit('foo');
// Prints:
//   b
//   a
```

###### Parameters

| Parameter | Type | Description |
| ------ | ------ | ------ |
| `event` | [`EventKey`](dom-events.md#eventkey) | - |
| `listener` | (...`args`: `any`[]) => `void` | The callback function |

###### Returns

`this`

###### Since

v0.3.0

###### Implementation of

[`WritableStream`](globals/namespaces/QuickJS.md#writablestream).[`once`](globals/namespaces/QuickJS.md#once-1)

###### Overrides

[`EventEmitter`](globals/index.md#eventemittert).[`once`](globals/index.md#once)

###### Call Signature

> **once**(`event`: `"close"`, `listener`: () => `void`): `this`

###### Parameters

| Parameter | Type |
| ------ | ------ |
| `event` | `"close"` |
| `listener` | () => `void` |

###### Returns

`this`

###### Implementation of

`QuickJS.WritableStream.once`

###### Overrides

`EventEmitter.once`

###### Call Signature

> **once**(`event`: `"error"`, `listener`: (`err`: `Error`) => `void`): `this`

###### Parameters

| Parameter | Type |
| ------ | ------ |
| `event` | `"error"` |
| `listener` | (`err`: `Error`) => `void` |

###### Returns

`this`

###### Implementation of

`QuickJS.WritableStream.once`

###### Overrides

`EventEmitter.once`

###### Call Signature

> **once**(`event`: `"finish"`, `listener`: () => `void`): `this`

###### Parameters

| Parameter | Type |
| ------ | ------ |
| `event` | `"finish"` |
| `listener` | () => `void` |

###### Returns

`this`

###### Implementation of

`QuickJS.WritableStream.once`

###### Overrides

`EventEmitter.once`

##### prependListener()

###### Call Signature

> **prependListener**(`event`: [`EventKey`](dom-events.md#eventkey), `listener`: (...`args`: `any`[]) => `void`): `this`

Adds the `listener` function to the _beginning_ of the listeners array for the
event named `eventName`. No checks are made to see if the `listener` has
already been added. Multiple calls passing the same combination of `eventName`
and `listener` will result in the `listener` being added, and called, multiple times.

Returns a reference to the `EventEmitter`, so that calls can be chained.

###### Parameters

| Parameter | Type | Description |
| ------ | ------ | ------ |
| `event` | [`EventKey`](dom-events.md#eventkey) | - |
| `listener` | (...`args`: `any`[]) => `void` | The callback function |

###### Returns

`this`

###### Implementation of

[`WritableStream`](globals/namespaces/QuickJS.md#writablestream).[`prependListener`](globals/namespaces/QuickJS.md#prependlistener-1)

###### Overrides

[`EventEmitter`](globals/index.md#eventemittert).[`prependListener`](globals/index.md#prependlistener)

###### Call Signature

> **prependListener**(`event`: `"close"`, `listener`: () => `void`): `this`

###### Parameters

| Parameter | Type |
| ------ | ------ |
| `event` | `"close"` |
| `listener` | () => `void` |

###### Returns

`this`

###### Implementation of

`QuickJS.WritableStream.prependListener`

###### Overrides

`EventEmitter.prependListener`

###### Call Signature

> **prependListener**(`event`: `"error"`, `listener`: (`err`: `Error`) => `void`): `this`

###### Parameters

| Parameter | Type |
| ------ | ------ |
| `event` | `"error"` |
| `listener` | (`err`: `Error`) => `void` |

###### Returns

`this`

###### Implementation of

`QuickJS.WritableStream.prependListener`

###### Overrides

`EventEmitter.prependListener`

###### Call Signature

> **prependListener**(`event`: `"finish"`, `listener`: () => `void`): `this`

###### Parameters

| Parameter | Type |
| ------ | ------ |
| `event` | `"finish"` |
| `listener` | () => `void` |

###### Returns

`this`

###### Implementation of

`QuickJS.WritableStream.prependListener`

###### Overrides

`EventEmitter.prependListener`

##### prependOnceListener()

###### Call Signature

> **prependOnceListener**(`event`: [`EventKey`](dom-events.md#eventkey), `listener`: (...`args`: `any`[]) => `void`): `this`

Adds a **one-time**`listener` function for the event named `eventName` to the _beginning_ of the listeners array.
The next time `eventName` is triggered, this listener is removed, and then invoked.

Returns a reference to the `EventEmitter`, so that calls can be chained.

###### Parameters

| Parameter | Type | Description |
| ------ | ------ | ------ |
| `event` | [`EventKey`](dom-events.md#eventkey) | - |
| `listener` | (...`args`: `any`[]) => `void` | The callback function |

###### Returns

`this`

###### Implementation of

[`WritableStream`](globals/namespaces/QuickJS.md#writablestream).[`prependOnceListener`](globals/namespaces/QuickJS.md#prependoncelistener-1)

###### Overrides

[`EventEmitter`](globals/index.md#eventemittert).[`prependOnceListener`](globals/index.md#prependoncelistener)

###### Call Signature

> **prependOnceListener**(`event`: `"close"`, `listener`: () => `void`): `this`

###### Parameters

| Parameter | Type |
| ------ | ------ |
| `event` | `"close"` |
| `listener` | () => `void` |

###### Returns

`this`

###### Implementation of

`QuickJS.WritableStream.prependOnceListener`

###### Overrides

`EventEmitter.prependOnceListener`

###### Call Signature

> **prependOnceListener**(`event`: `"error"`, `listener`: (`err`: `Error`) => `void`): `this`

###### Parameters

| Parameter | Type |
| ------ | ------ |
| `event` | `"error"` |
| `listener` | (`err`: `Error`) => `void` |

###### Returns

`this`

###### Implementation of

`QuickJS.WritableStream.prependOnceListener`

###### Overrides

`EventEmitter.prependOnceListener`

###### Call Signature

> **prependOnceListener**(`event`: `"finish"`, `listener`: () => `void`): `this`

###### Parameters

| Parameter | Type |
| ------ | ------ |
| `event` | `"finish"` |
| `listener` | () => `void` |

###### Returns

`this`

###### Implementation of

`QuickJS.WritableStream.prependOnceListener`

###### Overrides

`EventEmitter.prependOnceListener`

##### removeListener()

###### Call Signature

> **removeListener**(`event`: [`EventKey`](dom-events.md#eventkey), `listener`: (...`args`: `any`[]) => `void`): `this`

Removes the specified `listener` from the listener array for the event named `eventName`.

`removeListener()` will remove, at most, one instance of a listener from the
listener array. If any single listener has been added multiple times to the
listener array for the specified `eventName`, then `removeListener()` must be
called multiple times to remove each instance.

Once an event is emitted, all listeners attached to it at the time of emitting are called in order.
This implies that any `removeListener()` calls _after_ emitting and _before_ the last listener finishes execution
will not remove them from `emit()` in progress. Subsequent events behave as expected.

```js
import { EventEmitter } from 'events';
class MyEmitter extends EventEmitter {}
const myEmitter = new MyEmitter();

const callbackA = () => {
  console.log('A');
  myEmitter.removeListener('event', callbackB);
};

const callbackB = () => {
  console.log('B');
};

myEmitter.on('event', callbackA);

myEmitter.on('event', callbackB);

// callbackA removes listener callbackB but it will still be called.
// Internal listener array at time of emit [callbackA, callbackB]
myEmitter.emit('event');
// Prints:
//   A
//   B

// callbackB is now removed.
// Internal listener array [callbackA]
myEmitter.emit('event');
// Prints:
//   A
```

Because listeners are managed using an internal array, calling this will
change the position indices of any listener registered _after_ the listener
being removed. This will not impact the order in which listeners are called,
but it means that any copies of the listener array as returned by
the `emitter.listeners()` method will need to be recreated.

When a single function has been added as a handler multiple times for a single
event (as in the example below), `removeListener()` will remove the most
recently added instance. In the example the `once('ping')` listener is removed:

```js
import { EventEmitter } from 'events';
const ee = new EventEmitter();

function pong() {
  console.log('pong');
}

ee.on('ping', pong);
ee.once('ping', pong);
ee.removeListener('ping', pong);

ee.emit('ping');
ee.emit('ping');
```

Returns a reference to the `EventEmitter`, so that calls can be chained.

###### Parameters

| Parameter | Type |
| ------ | ------ |
| `event` | [`EventKey`](dom-events.md#eventkey) |
| `listener` | (...`args`: `any`[]) => `void` |

###### Returns

`this`

###### Implementation of

[`WritableStream`](globals/namespaces/QuickJS.md#writablestream).[`removeListener`](globals/namespaces/QuickJS.md#removelistener-1)

###### Overrides

[`EventEmitter`](globals/index.md#eventemittert).[`removeListener`](globals/index.md#removelistener)

###### Call Signature

> **removeListener**(`event`: `"close"`, `listener`: () => `void`): `this`

###### Parameters

| Parameter | Type |
| ------ | ------ |
| `event` | `"close"` |
| `listener` | () => `void` |

###### Returns

`this`

###### Implementation of

`QuickJS.WritableStream.removeListener`

###### Overrides

`EventEmitter.removeListener`

###### Call Signature

> **removeListener**(`event`: `"error"`, `listener`: (`err`: `Error`) => `void`): `this`

###### Parameters

| Parameter | Type |
| ------ | ------ |
| `event` | `"error"` |
| `listener` | (`err`: `Error`) => `void` |

###### Returns

`this`

###### Implementation of

`QuickJS.WritableStream.removeListener`

###### Overrides

`EventEmitter.removeListener`

###### Call Signature

> **removeListener**(`event`: `"finish"`, `listener`: () => `void`): `this`

###### Parameters

| Parameter | Type |
| ------ | ------ |
| `event` | `"finish"` |
| `listener` | () => `void` |

###### Returns

`this`

###### Implementation of

`QuickJS.WritableStream.removeListener`

###### Overrides

`EventEmitter.removeListener`

##### write()

> **write**(`chunk`: `string` \| `ArrayBuffer` \| `SharedArrayBuffer` \| [`ArrayBufferView`](globals/namespaces/QuickJS.md#arraybufferview) \| [`Buffer`](buffer.md#buffer), `callback`?: (`error`?: `null` \| `Error`) => `void`): `void`

The `writable.write()` method writes some data to the stream, and calls the
supplied `callback` once the data has been fully handled. If an error
occurs, the `callback` will be called with the error as its
first argument. The `callback` is usually called asynchronously and before `'error'`
is emitted.

```js
function write(data, cb) {
  if (!stream.write(data)) {
    stream.once('drain', cb);
  } else {
    process.nextTick(cb);
  }
}

// Wait for cb to be called before doing any other write.
write('hello', () => {
  console.log('Write completed, do more writes now.');
});
```

A `Writable` stream in object mode will always ignore the `encoding` argument.

###### Parameters

| Parameter | Type | Description |
| ------ | ------ | ------ |
| `chunk` | `string` \| `ArrayBuffer` \| `SharedArrayBuffer` \| [`ArrayBufferView`](globals/namespaces/QuickJS.md#arraybufferview) \| [`Buffer`](buffer.md#buffer) | Optional data to write. `chunk` must be a {string}, {Buffer}, {TypedArray} or {DataView}. |
| `callback`? | (`error`?: `null` \| `Error`) => `void` | Callback for when this chunk of data is flushed. |

###### Returns

`void`

`false` if the stream wishes for the calling code to wait for the `'drain'` event to be emitted before continuing to write additional data; otherwise `true`.

###### Since

v0.9.4

###### Implementation of

[`WritableStream`](globals/namespaces/QuickJS.md#writablestream).[`write`](globals/namespaces/QuickJS.md#write)



================================================
FILE: src/reference/modules/llrt/fs/index.md
================================================
[@caido/quickjs-types](../../index.md) / llrt/fs

# llrt/fs

## Modules

| Module | Description |
| ------ | ------ |
| [fs/promises](fs/promises.md) | - |

## Namespaces

| Namespace | Description |
| ------ | ------ |
| [constants](namespaces/constants.md) | - |

## Classes

### Dirent

A representation of a directory entry, which can be a file or a subdirectory
within the directory. A directory entry is a combination of the file name and file type pairs.

Additionally, when [promises.readdir](fs/promises.md#readdir) or [readdirSync](index.md#readdirsync) is called with
the `withFileTypes` option set to `true`, the resulting array is filled with `fs.Dirent` objects, rather than strings.

#### Constructors

##### new Dirent()

> **new Dirent**(): [`Dirent`](index.md#dirent)

###### Returns

[`Dirent`](index.md#dirent)

#### Properties

##### name

> **name**: `string`

The file name that this `fs.Dirent` object refers to.

##### parentPath

> **parentPath**: `string`

The base path that this `fs.Dirent` object refers to.

#### Methods

##### isBlockDevice()

> **isBlockDevice**(): `boolean`

Returns `true` if the `fs.Dirent` object describes a block device.

###### Returns

`boolean`

##### isCharacterDevice()

> **isCharacterDevice**(): `boolean`

Returns `true` if the `fs.Dirent` object describes a character device.

###### Returns

`boolean`

##### isDirectory()

> **isDirectory**(): `boolean`

Returns `true` if the `fs.Dirent` object describes a file system
directory.

###### Returns

`boolean`

##### isFIFO()

> **isFIFO**(): `boolean`

Returns `true` if the `fs.Dirent` object describes a first-in-first-out
(FIFO) pipe.

###### Returns

`boolean`

##### isFile()

> **isFile**(): `boolean`

Returns `true` if the `fs.Dirent` object describes a regular file.

###### Returns

`boolean`

##### isSocket()

> **isSocket**(): `boolean`

Returns `true` if the `fs.Dirent` object describes a socket.

###### Returns

`boolean`

##### isSymbolicLink()

> **isSymbolicLink**(): `boolean`

Returns `true` if the `fs.Dirent` object describes a symbolic link.

###### Returns

`boolean`

***

### Stats

A `fs.Stats` object provides information about a file.

`Stat` objects are not to be created directly using the `new` keyword.

```console
Stats {
  dev: 2114,
  ino: 48064969,
  mode: 33188,
  nlink: 1,
  uid: 85,
  gid: 100,
  rdev: 0,
  size: 527,
  blksize: 4096,
  blocks: 8,
  atimeMs: 1318289051000.1,
  mtimeMs: 1318289051000.1,
  ctimeMs: 1318289051000.1,
  birthtimeMs: 1318289051000.1,
  atime: Mon, 10 Oct 2011 23:24:11 GMT,
  mtime: Mon, 10 Oct 2011 23:24:11 GMT,
  ctime: Mon, 10 Oct 2011 23:24:11 GMT,
  birthtime: Mon, 10 Oct 2011 23:24:11 GMT }
```

#### Extends

- [`StatsBase`](index.md#statsbaset)\<`number`\>

#### Constructors

##### new Stats()

> **new Stats**(): [`Stats`](index.md#stats)

###### Returns

[`Stats`](index.md#stats)

###### Inherited from

`StatsBase<number>.constructor`

#### Properties

##### atime

> **atime**: `Date`

###### Inherited from

[`StatsBase`](index.md#statsbaset).[`atime`](index.md#atime-1)

##### atimeMs

> **atimeMs**: `number`

###### Inherited from

[`StatsBase`](index.md#statsbaset).[`atimeMs`](index.md#atimems-1)

##### birthtime

> **birthtime**: `Date`

###### Inherited from

[`StatsBase`](index.md#statsbaset).[`birthtime`](index.md#birthtime-1)

##### birthtimeMs

> **birthtimeMs**: `number`

###### Inherited from

[`StatsBase`](index.md#statsbaset).[`birthtimeMs`](index.md#birthtimems-1)

##### blksize

> **blksize**: `number`

###### Inherited from

[`StatsBase`](index.md#statsbaset).[`blksize`](index.md#blksize-1)

##### blocks

> **blocks**: `number`

###### Inherited from

[`StatsBase`](index.md#statsbaset).[`blocks`](index.md#blocks-1)

##### ctime

> **ctime**: `Date`

###### Inherited from

[`StatsBase`](index.md#statsbaset).[`ctime`](index.md#ctime-1)

##### ctimeMs

> **ctimeMs**: `number`

###### Inherited from

[`StatsBase`](index.md#statsbaset).[`ctimeMs`](index.md#ctimems-1)

##### dev

> **dev**: `number`

###### Inherited from

[`StatsBase`](index.md#statsbaset).[`dev`](index.md#dev-1)

##### gid

> **gid**: `number`

###### Inherited from

[`StatsBase`](index.md#statsbaset).[`gid`](index.md#gid-1)

##### ino

> **ino**: `number`

###### Inherited from

[`StatsBase`](index.md#statsbaset).[`ino`](index.md#ino-1)

##### mode

> **mode**: `number`

###### Inherited from

[`StatsBase`](index.md#statsbaset).[`mode`](index.md#mode-2)

##### mtime

> **mtime**: `Date`

###### Inherited from

[`StatsBase`](index.md#statsbaset).[`mtime`](index.md#mtime-1)

##### mtimeMs

> **mtimeMs**: `number`

###### Inherited from

[`StatsBase`](index.md#statsbaset).[`mtimeMs`](index.md#mtimems-1)

##### nlink

> **nlink**: `number`

###### Inherited from

[`StatsBase`](index.md#statsbaset).[`nlink`](index.md#nlink-1)

##### rdev

> **rdev**: `number`

###### Inherited from

[`StatsBase`](index.md#statsbaset).[`rdev`](index.md#rdev-1)

##### size

> **size**: `number`

###### Inherited from

[`StatsBase`](index.md#statsbaset).[`size`](index.md#size-1)

##### uid

> **uid**: `number`

###### Inherited from

[`StatsBase`](index.md#statsbaset).[`uid`](index.md#uid-1)

#### Methods

##### isBlockDevice()

> **isBlockDevice**(): `boolean`

###### Returns

`boolean`

###### Inherited from

[`StatsBase`](index.md#statsbaset).[`isBlockDevice`](index.md#isblockdevice-2)

##### isCharacterDevice()

> **isCharacterDevice**(): `boolean`

###### Returns

`boolean`

###### Inherited from

[`StatsBase`](index.md#statsbaset).[`isCharacterDevice`](index.md#ischaracterdevice-2)

##### isDirectory()

> **isDirectory**(): `boolean`

###### Returns

`boolean`

###### Inherited from

[`StatsBase`](index.md#statsbaset).[`isDirectory`](index.md#isdirectory-2)

##### isFIFO()

> **isFIFO**(): `boolean`

###### Returns

`boolean`

###### Inherited from

[`StatsBase`](index.md#statsbaset).[`isFIFO`](index.md#isfifo-2)

##### isFile()

> **isFile**(): `boolean`

###### Returns

`boolean`

###### Inherited from

[`StatsBase`](index.md#statsbaset).[`isFile`](index.md#isfile-2)

##### isSocket()

> **isSocket**(): `boolean`

###### Returns

`boolean`

###### Inherited from

[`StatsBase`](index.md#statsbaset).[`isSocket`](index.md#issocket-2)

##### isSymbolicLink()

> **isSymbolicLink**(): `boolean`

###### Returns

`boolean`

###### Inherited from

[`StatsBase`](index.md#statsbaset).[`isSymbolicLink`](index.md#issymboliclink-2)

## Interfaces

### MakeDirectoryOptions

#### Properties

##### mode?

> `optional` **mode**: `number`

A file mode. If not specified

###### Default

```ts
0o777
```

##### recursive?

> `optional` **recursive**: `boolean`

Indicates whether parent folders should be created.
If a folder was created, the path to the first created folder will be returned.

###### Default

```ts
false
```

***

### RmDirOptions

#### Properties

##### ~~recursive?~~

> `optional` **recursive**: `boolean`

###### Deprecated

Use `fs.rm(path, { recursive: true, force: true })` instead.

If `true`, perform a recursive directory removal. In
recursive mode, operations are retried on failure.

###### Default

```ts
false
```

***

### RmOptions

#### Properties

##### force?

> `optional` **force**: `boolean`

When `true`, exceptions will be ignored if `path` does not exist.

###### Default

```ts
false
```

##### recursive?

> `optional` **recursive**: `boolean`

If `true`, perform a recursive directory removal. In
recursive mode, operations are retried on failure.

###### Default

```ts
false
```

***

### StatsBase\<T\>

#### Extended by

- [`Stats`](index.md#stats)

#### Type Parameters

| Type Parameter |
| ------ |
| `T` |

#### Properties

##### atime

> **atime**: `Date`

##### atimeMs

> **atimeMs**: `T`

##### birthtime

> **birthtime**: `Date`

##### birthtimeMs

> **birthtimeMs**: `T`

##### blksize

> **blksize**: `T`

##### blocks

> **blocks**: `T`

##### ctime

> **ctime**: `Date`

##### ctimeMs

> **ctimeMs**: `T`

##### dev

> **dev**: `T`

##### gid

> **gid**: `T`

##### ino

> **ino**: `T`

##### mode

> **mode**: `T`

##### mtime

> **mtime**: `Date`

##### mtimeMs

> **mtimeMs**: `T`

##### nlink

> **nlink**: `T`

##### rdev

> **rdev**: `T`

##### size

> **size**: `T`

##### uid

> **uid**: `T`

#### Methods

##### isBlockDevice()

> **isBlockDevice**(): `boolean`

###### Returns

`boolean`

##### isCharacterDevice()

> **isCharacterDevice**(): `boolean`

###### Returns

`boolean`

##### isDirectory()

> **isDirectory**(): `boolean`

###### Returns

`boolean`

##### isFIFO()

> **isFIFO**(): `boolean`

###### Returns

`boolean`

##### isFile()

> **isFile**(): `boolean`

###### Returns

`boolean`

##### isSocket()

> **isSocket**(): `boolean`

###### Returns

`boolean`

##### isSymbolicLink()

> **isSymbolicLink**(): `boolean`

###### Returns

`boolean`

***

### StatSyncFn()

#### Extends

- `Function`

> **StatSyncFn**(`path`: `string`): [`Stats`](index.md#stats)

#### Parameters

| Parameter | Type |
| ------ | ------ |
| `path` | `string` |

#### Returns

[`Stats`](index.md#stats)

## Type Aliases

### Mode

> **Mode**: `number`

***

### PathLike

> **PathLike**: `string`

Valid types for path values in "fs".

## Functions

### accessSync()

> **accessSync**(`path`: `string`, `mode`?: `number`): `void`

Synchronously tests a user's permissions for the file or directory specified
by `path`. The `mode` argument is an optional integer that specifies the
accessibility checks to be performed. `mode` should be either the value `fs.constants.F_OK` or a mask consisting of the bitwise OR of any of `fs.constants.R_OK`, `fs.constants.W_OK`, and
`fs.constants.X_OK` (e.g.`fs.constants.W_OK | fs.constants.R_OK`). Check `File access constants` for
possible values of `mode`.

If any of the accessibility checks fail, an `Error` will be thrown. Otherwise,
the method will return `undefined`.

```js
import { accessSync, constants } from 'fs';

try {
  accessSync('etc/passwd', constants.R_OK | constants.W_OK);
  console.log('can read/write');
} catch (err) {
  console.error('no access!');
}
```

#### Parameters

| Parameter | Type | Description |
| ------ | ------ | ------ |
| `path` | `string` | - |
| `mode`? | `number` |  |

#### Returns

`void`

***

### chmodSync()

> **chmodSync**(`path`: `string`, `mode`: `number`): `void`

For detailed information, see the documentation of the asynchronous version of
this API: chmod.

See the POSIX [`chmod(2)`](http://man7.org/linux/man-pages/man2/chmod.2.html) documentation for more detail.

#### Parameters

| Parameter | Type |
| ------ | ------ |
| `path` | `string` |
| `mode` | `number` |

#### Returns

`void`

***

### mkdirSync()

> **mkdirSync**(`path`: `string`, `options`?: [`MakeDirectoryOptions`](index.md#makedirectoryoptions)): `string`

Synchronously creates a directory. Returns the `path`.

See the POSIX [`mkdir(2)`](http://man7.org/linux/man-pages/man2/mkdir.2.html) documentation for more details.

#### Parameters

| Parameter | Type |
| ------ | ------ |
| `path` | `string` |
| `options`? | [`MakeDirectoryOptions`](index.md#makedirectoryoptions) |

#### Returns

`string`

***

### mkdtempSync()

> **mkdtempSync**(`prefix`: `string`): `string`

Returns the created directory path.

For detailed information, see the documentation of the asynchronous version of
this API: [promises.mkdtemp](fs/promises.md#mkdtemp).

#### Parameters

| Parameter | Type |
| ------ | ------ |
| `prefix` | `string` |

#### Returns

`string`

***

### readdirSync()

#### Call Signature

> **readdirSync**(`path`: `string`, `options`?: `object`): `string`[]

Reads the contents of the directory.

See the POSIX [`readdir(3)`](http://man7.org/linux/man-pages/man3/readdir.3.html) documentation for more details.

If `options.withFileTypes` is set to `true`, the result will contain `fs.Dirent` objects.

##### Parameters

| Parameter | Type |
| ------ | ------ |
| `path` | `string` |
| `options`? | \{ `recursive`: `boolean`; `withFileTypes`: `false`; \} |
| `options.recursive`? | `boolean` |
| `options.withFileTypes`? | `false` |

##### Returns

`string`[]

#### Call Signature

> **readdirSync**(`path`: `string`, `options`: `object`): [`Dirent`](index.md#dirent)[]

Synchronous readdir (2) - read a directory.

##### Parameters

| Parameter | Type | Description |
| ------ | ------ | ------ |
| `path` | `string` | A path to a file. If a URL is provided, it must use the `file:` protocol. |
| `options` | \{ `recursive`: `boolean`; `withFileTypes`: `true`; \} | If called with `withFileTypes: true` the result data will be an array of Dirent. |
| `options.recursive`? | `boolean` | - |
| `options.withFileTypes` | `true` | - |

##### Returns

[`Dirent`](index.md#dirent)[]

***

### readFileSync()

#### Call Signature

> **readFileSync**(`path`: `string`, `options`?: `null` \| \{ `encoding`: `null`; \}): [`Buffer`](../buffer.md#buffer)

Returns the contents of the `path`.

For detailed information, see the documentation of the asynchronous version of
this API: [promises.readFile](fs/promises.md#readfile-1).

If the `encoding` option is specified then this function returns a
string. Otherwise it returns a buffer.

##### Parameters

| Parameter | Type | Description |
| ------ | ------ | ------ |
| `path` | `string` | A path to a file. |
| `options`? | `null` \| \{ `encoding`: `null`; \} | - |

##### Returns

[`Buffer`](../buffer.md#buffer)

#### Call Signature

> **readFileSync**(`path`: `string`, `options`: [`BufferEncoding`](../buffer.md#bufferencoding) \| \{ `encoding`: [`BufferEncoding`](../buffer.md#bufferencoding); \}): `string`

Synchronously reads the entire contents of a file.

##### Parameters

| Parameter | Type | Description |
| ------ | ------ | ------ |
| `path` | `string` | A path to a file. |
| `options` | [`BufferEncoding`](../buffer.md#bufferencoding) \| \{ `encoding`: [`BufferEncoding`](../buffer.md#bufferencoding); \} | Either the encoding for the result, or an object that contains the encoding. |

##### Returns

`string`

***

### renameSync()

> **renameSync**(`oldPath`: `string`, `newPath`: `string`): `void`

Synchronously renames a file or directory from `oldPath` to `newPath`.

For detailed information, see the documentation of the asynchronous version of
this API: [promises.rename](fs/promises.md#rename).

#### Parameters

| Parameter | Type |
| ------ | ------ |
| `oldPath` | `string` |
| `newPath` | `string` |

#### Returns

`void`

***

### rmdirSync()

> **rmdirSync**(`path`: `string`, `options`?: [`RmDirOptions`](index.md#rmdiroptions)): `void`

Synchronous [`rmdir(2)`](http://man7.org/linux/man-pages/man2/rmdir.2.html). Returns `undefined`.

Using `fs.rmdirSync()` on a file (not a directory) results in an `ENOENT` error
on Windows and an `ENOTDIR` error on POSIX.

To get a behavior similar to the `rm -rf` Unix command, use [rmSync](index.md#rmsync) with options `{ recursive: true, force: true }`.

#### Parameters

| Parameter | Type |
| ------ | ------ |
| `path` | `string` |
| `options`? | [`RmDirOptions`](index.md#rmdiroptions) |

#### Returns

`void`

***

### rmSync()

> **rmSync**(`path`: `string`, `options`?: [`RmOptions`](index.md#rmoptions)): `void`

Synchronously removes files and directories (modeled on the standard POSIX `rm` utility). Returns `undefined`.

#### Parameters

| Parameter | Type |
| ------ | ------ |
| `path` | `string` |
| `options`? | [`RmOptions`](index.md#rmoptions) |

#### Returns

`void`

***

### statSync()

> **statSync**(`path`: `string`): [`Stats`](index.md#stats)

Synchronous stat - Get file status.

#### Parameters

| Parameter | Type | Description |
| ------ | ------ | ------ |
| `path` | `string` | A path to a file. |

#### Returns

[`Stats`](index.md#stats)

***

### writeFileSync()

> **writeFileSync**(`file`: `string`, `data`: `string` \| `ArrayBuffer` \| `SharedArrayBuffer` \| [`ArrayBufferView`](../globals/namespaces/QuickJS.md#arraybufferview) \| [`Buffer`](../buffer.md#buffer)): `void`

Returns `undefined`.

For detailed information, see the documentation of the asynchronous version of
this API: [promises.writeFile](fs/promises.md#writefile-1).

#### Parameters

| Parameter | Type | Description |
| ------ | ------ | ------ |
| `file` | `string` | A path to a file. |
| `data` | `string` \| `ArrayBuffer` \| `SharedArrayBuffer` \| [`ArrayBufferView`](../globals/namespaces/QuickJS.md#arraybufferview) \| [`Buffer`](../buffer.md#buffer) | - |

#### Returns

`void`



================================================
FILE: src/reference/modules/llrt/fs/fs/promises.md
================================================
[@caido/quickjs-types](../../../index.md) / [llrt/fs](../index.md) / fs/promises

# fs/promises

## Classes

### FileHandle

#### Constructors

##### new FileHandle()

> **new FileHandle**(): [`FileHandle`](promises.md#filehandle)

###### Returns

[`FileHandle`](promises.md#filehandle)

#### Properties

##### fd

> `readonly` **fd**: `number`

The numeric file descriptor managed by the {FileHandle} object.

#### Methods

##### chmod()

> **chmod**(`mode`: `number`): `Promise`\<`void`\>

Modifies the permissions on the file. See [`chmod(2)`](http://man7.org/linux/man-pages/man2/chmod.2.html).

###### Parameters

| Parameter | Type | Description |
| ------ | ------ | ------ |
| `mode` | `number` | the file mode bit mask. |

###### Returns

`Promise`\<`void`\>

Fulfills with `undefined` upon success.

##### chown()

> **chown**(`uid`: `number`, `gid`: `number`): `Promise`\<`void`\>

Changes the ownership of the file. A wrapper for [`chown(2)`](http://man7.org/linux/man-pages/man2/chown.2.html).

###### Parameters

| Parameter | Type | Description |
| ------ | ------ | ------ |
| `uid` | `number` | The file's new owner's user id. |
| `gid` | `number` | The file's new group's group id. |

###### Returns

`Promise`\<`void`\>

Fulfills with `undefined` upon success.

##### close()

> **close**(): `Promise`\<`void`\>

Closes the file handle after waiting for any pending operation on the handle to
complete.

```js
import { open } from 'fs/promises';

let filehandle;
try {
  filehandle = await open('thefile.txt', 'r');
} finally {
  await filehandle?.close();
}
```

###### Returns

`Promise`\<`void`\>

Fulfills with `undefined` upon success.

##### datasync()

> **datasync**(): `Promise`\<`void`\>

Forces all currently queued I/O operations associated with the file to the
operating system's synchronized I/O completion state. Refer to the POSIX [`fdatasync(2)`](http://man7.org/linux/man-pages/man2/fdatasync.2.html) documentation for details.

Unlike `filehandle.sync` this method does not flush modified metadata.

###### Returns

`Promise`\<`void`\>

Fulfills with `undefined` upon success.

##### read()

###### Call Signature

> **read**\<`T`\>(`buffer`: `T`, `offset`?: `null` \| `number`, `length`?: `null` \| `number`, `position`?: `null` \| `number`): `Promise`\<[`FileReadResult`](promises.md#filereadresultt)\<`T`\>\>

Reads data from the file and stores that in the given buffer.

If the file is not modified concurrently, the end-of-file is reached when the
number of bytes read is zero.

###### Type Parameters

| Type Parameter |
| ------ |
| `T` *extends* [`ArrayBufferView`](../../globals/namespaces/QuickJS.md#arraybufferview) |

###### Parameters

| Parameter | Type | Description |
| ------ | ------ | ------ |
| `buffer` | `T` | A buffer that will be filled with the file data read. |
| `offset`? | `null` \| `number` | The location in the buffer at which to start filling. |
| `length`? | `null` \| `number` | The number of bytes to read. |
| `position`? | `null` \| `number` | The location where to begin reading data from the file. If `null`, data will be read from the current file position, and the position will be updated. If `position` is an integer, the current file position will remain unchanged. |

###### Returns

`Promise`\<[`FileReadResult`](promises.md#filereadresultt)\<`T`\>\>

Fulfills upon success with an object with two properties: bytesRead and buffer

###### Call Signature

> **read**\<`T`\>(`buffer`: `T`, `options`?: [`FileReadOptions`](promises.md#filereadoptionst)\<`T`\>): `Promise`\<[`FileReadResult`](promises.md#filereadresultt)\<`T`\>\>

Reads data from the file and stores that in the given buffer.

If the file is not modified concurrently, the end-of-file is reached when the
number of bytes read is zero.

###### Type Parameters

| Type Parameter | Default type |
| ------ | ------ |
| `T` *extends* [`ArrayBufferView`](../../globals/namespaces/QuickJS.md#arraybufferview) | [`Buffer`](../../buffer.md#buffer) |

###### Parameters

| Parameter | Type | Description |
| ------ | ------ | ------ |
| `buffer` | `T` | A buffer that will be filled with the file data read. |
| `options`? | [`FileReadOptions`](promises.md#filereadoptionst)\<`T`\> | - |

###### Returns

`Promise`\<[`FileReadResult`](promises.md#filereadresultt)\<`T`\>\>

Fulfills upon success with an object with two properties: bytesRead and buffer

###### Call Signature

> **read**\<`T`\>(`options`?: [`FileReadOptions`](promises.md#filereadoptionst)\<`T`\>): `Promise`\<[`FileReadResult`](promises.md#filereadresultt)\<`T`\>\>

Reads data from the file and stores that in the given buffer.

If the file is not modified concurrently, the end-of-file is reached when the
number of bytes read is zero.

###### Type Parameters

| Type Parameter | Default type |
| ------ | ------ |
| `T` *extends* [`ArrayBufferView`](../../globals/namespaces/QuickJS.md#arraybufferview) | [`Buffer`](../../buffer.md#buffer) |

###### Parameters

| Parameter | Type |
| ------ | ------ |
| `options`? | [`FileReadOptions`](promises.md#filereadoptionst)\<`T`\> |

###### Returns

`Promise`\<[`FileReadResult`](promises.md#filereadresultt)\<`T`\>\>

Fulfills upon success with an object with two properties: bytesRead and buffer

##### readFile()

###### Call Signature

> **readFile**(`options`?: `null` \| \{ `encoding`: `null`; \}): `Promise`\<[`Buffer`](../../buffer.md#buffer)\>

Asynchronously reads the entire contents of a file.

If `options` is a string, then it specifies the `encoding`.

The `FileHandle` has to support reading.

If one or more `filehandle.read()` calls are made on a file handle and then a `filehandle.readFile()` call is made, the data will be read from the current
position till the end of the file. It doesn't always read from the beginning
of the file.

###### Parameters

| Parameter | Type |
| ------ | ------ |
| `options`? | `null` \| \{ `encoding`: `null`; \} |

###### Returns

`Promise`\<[`Buffer`](../../buffer.md#buffer)\>

Fulfills upon a successful read with the contents of the file. If no encoding is specified (using `options.encoding`), the data is returned as a {Buffer} object. Otherwise, the
data will be a string.

###### Call Signature

> **readFile**(`options`: [`BufferEncoding`](../../buffer.md#bufferencoding) \| \{ `encoding`: [`BufferEncoding`](../../buffer.md#bufferencoding); \}): `Promise`\<`string`\>

Asynchronously reads the entire contents of a file.

If `options` is a string, then it specifies the `encoding`.

The `FileHandle` has to support reading.

If one or more `filehandle.read()` calls are made on a file handle and then a `filehandle.readFile()` call is made, the data will be read from the current
position till the end of the file. It doesn't always read from the beginning
of the file.

###### Parameters

| Parameter | Type |
| ------ | ------ |
| `options` | [`BufferEncoding`](../../buffer.md#bufferencoding) \| \{ `encoding`: [`BufferEncoding`](../../buffer.md#bufferencoding); \} |

###### Returns

`Promise`\<`string`\>

Fulfills upon a successful read with the contents of the file. If no encoding is specified (using `options.encoding`), the data is returned as a {Buffer} object. Otherwise, the
data will be a string.

##### stat()

> **stat**(): `Promise`\<[`Stats`](../index.md#stats)\>

Get {FileHandle} status.

###### Returns

`Promise`\<[`Stats`](../index.md#stats)\>

Fulfills with the {fs.Stats} object.

##### sync()

> **sync**(): `Promise`\<`void`\>

Request that all data for the open file descriptor is flushed to the storage
device. The specific implementation is operating system and device specific.
Refer to the POSIX [`fsync(2)`](http://man7.org/linux/man-pages/man2/fsync.2.html) documentation for more detail.

###### Returns

`Promise`\<`void`\>

Fulfills with `undefined` upon success.

##### truncate()

> **truncate**(`len`?: `number`): `Promise`\<`void`\>

Truncates the file.

If the file was larger than `len` bytes, only the first `len` bytes will be
retained in the file.

The following example retains only the first four bytes of the file:

```js
import { open } from 'fs/promises';

let filehandle = null;
try {
  filehandle = await open('temp.txt', 'r+');
  await filehandle.truncate(4);
} finally {
  await filehandle?.close();
}
```

If the file previously was shorter than `len` bytes, it is extended, and the
extended part is filled with null bytes (`'\0'`):

###### Parameters

| Parameter | Type | Description |
| ------ | ------ | ------ |
| `len`? | `number` |  |

###### Returns

`Promise`\<`void`\>

Fulfills with `undefined` upon success.

##### write()

###### Call Signature

> **write**\<`TBuffer`\>(`buffer`: `TBuffer`, `offset`?: `null` \| `number`, `length`?: `null` \| `number`, `position`?: `null` \| `number`): `Promise`\<\{ `buffer`: `TBuffer`; `bytesWritten`: `number`; \}\>

Write `buffer` to the file.

The promise is fulfilled with an object containing two properties:

It is unsafe to use `filehandle.write()` multiple times on the same file
without waiting for the promise to be fulfilled (or rejected). For this
scenario, use `filehandle.createWriteStream()`.

On Linux, positional writes do not work when the file is opened in append mode.
The kernel ignores the position argument and always appends the data to
the end of the file.

###### Type Parameters

| Type Parameter |
| ------ |
| `TBuffer` *extends* [`ArrayBufferView`](../../globals/namespaces/QuickJS.md#arraybufferview) |

###### Parameters

| Parameter | Type | Description |
| ------ | ------ | ------ |
| `buffer` | `TBuffer` | - |
| `offset`? | `null` \| `number` | The start position from within `buffer` where the data to write begins. |
| `length`? | `null` \| `number` | The number of bytes from `buffer` to write. |
| `position`? | `null` \| `number` | The offset from the beginning of the file where the data from `buffer` should be written. If `position` is not a `number`, the data will be written at the current position. See the POSIX pwrite(2) documentation for more detail. |

###### Returns

`Promise`\<\{ `buffer`: `TBuffer`; `bytesWritten`: `number`; \}\>

###### Call Signature

> **write**\<`TBuffer`\>(`buffer`: `TBuffer`, `options`?: `null` \| \{ `length`: `null` \| `number`; `offset`: `null` \| `number`; `position`: `null` \| `number`; \}): `Promise`\<\{ `buffer`: `TBuffer`; `bytesWritten`: `number`; \}\>

Write `buffer` to the file.

The promise is fulfilled with an object containing two properties:

It is unsafe to use `filehandle.write()` multiple times on the same file
without waiting for the promise to be fulfilled (or rejected). For this
scenario, use `filehandle.createWriteStream()`.

On Linux, positional writes do not work when the file is opened in append mode.
The kernel ignores the position argument and always appends the data to
the end of the file.

###### Type Parameters

| Type Parameter |
| ------ |
| `TBuffer` *extends* [`ArrayBufferView`](../../globals/namespaces/QuickJS.md#arraybufferview) |

###### Parameters

| Parameter | Type |
| ------ | ------ |
| `buffer` | `TBuffer` |
| `options`? | `null` \| \{ `length`: `null` \| `number`; `offset`: `null` \| `number`; `position`: `null` \| `number`; \} |

###### Returns

`Promise`\<\{ `buffer`: `TBuffer`; `bytesWritten`: `number`; \}\>

###### Call Signature

> **write**(`data`: `string`, `position`?: `null` \| `number`, `encoding`?: `null` \| [`BufferEncoding`](../../buffer.md#bufferencoding)): `Promise`\<\{ `buffer`: `string`; `bytesWritten`: `number`; \}\>

Write `buffer` to the file.

The promise is fulfilled with an object containing two properties:

It is unsafe to use `filehandle.write()` multiple times on the same file
without waiting for the promise to be fulfilled (or rejected). For this
scenario, use `filehandle.createWriteStream()`.

On Linux, positional writes do not work when the file is opened in append mode.
The kernel ignores the position argument and always appends the data to
the end of the file.

###### Parameters

| Parameter | Type | Description |
| ------ | ------ | ------ |
| `data` | `string` | - |
| `position`? | `null` \| `number` | The offset from the beginning of the file where the data from `buffer` should be written. If `position` is not a `number`, the data will be written at the current position. See the POSIX pwrite(2) documentation for more detail. |
| `encoding`? | `null` \| [`BufferEncoding`](../../buffer.md#bufferencoding) | - |

###### Returns

`Promise`\<\{ `buffer`: `string`; `bytesWritten`: `number`; \}\>

##### writeFile()

> **writeFile**(`data`: `string` \| [`ArrayBufferView`](../../globals/namespaces/QuickJS.md#arraybufferview), `options`?: `null` \| [`BufferEncoding`](../../buffer.md#bufferencoding) \| \{ `encoding`: BufferEncoding \| null \| undefined; \}): `Promise`\<`void`\>

Asynchronously writes data to a file, replacing the file if it already exists.

If `options` is a string, then it specifies the `encoding`.

The `FileHandle` has to support writing.

It is unsafe to use `filehandle.writeFile()` multiple times on the same file
without waiting for the promise to be fulfilled (or rejected).

If one or more `filehandle.write()` calls are made on a file handle and then a`filehandle.writeFile()` call is made, the data will be written from the
current position till the end of the file. It doesn't always write from the beginning of the file.

###### Parameters

| Parameter | Type |
| ------ | ------ |
| `data` | `string` \| [`ArrayBufferView`](../../globals/namespaces/QuickJS.md#arraybufferview) |
| `options`? | `null` \| [`BufferEncoding`](../../buffer.md#bufferencoding) \| \{ `encoding`: BufferEncoding \| null \| undefined; \} |

###### Returns

`Promise`\<`void`\>

## Interfaces

### FileReadOptions\<T\>

#### Type Parameters

| Type Parameter | Default type |
| ------ | ------ |
| `T` *extends* [`ArrayBufferView`](../../globals/namespaces/QuickJS.md#arraybufferview) | [`Buffer`](../../buffer.md#buffer) |

#### Properties

##### buffer?

> `optional` **buffer**: `T`

###### Default

`Buffer.alloc(16384)`

##### length?

> `optional` **length**: `null` \| `number`

###### Default

`buffer.byteLength - offset`

##### offset?

> `optional` **offset**: `null` \| `number`

###### Default

```ts
0
```

##### position?

> `optional` **position**: `null` \| `number`

***

### FileReadResult\<T\>

#### Type Parameters

| Type Parameter |
| ------ |
| `T` *extends* [`ArrayBufferView`](../../globals/namespaces/QuickJS.md#arraybufferview) |

#### Properties

##### buffer

> **buffer**: `T`

##### bytesRead

> **bytesRead**: `number`

## Type Aliases

### FileSystemFlags

> **FileSystemFlags**: `"a"` \| `"ax"` \| `"a+"` \| `"r"` \| `"r+"` \| `"w"` \| `"wx"` \| `"w+"` \| `"wx+"`

## Variables

### constants

> `const` **constants**: *typeof* [`constants`](../namespaces/constants.md)

## Functions

### access()

> **access**(`path`: `string`, `mode`?: `number`): `Promise`\<`void`\>

Tests a user's permissions for the file or directory specified by `path`.
The `mode` argument is an optional integer that specifies the accessibility
checks to be performed. `mode` should be either the value `fs.constants.F_OK` or a mask consisting of the bitwise OR of any of `fs.constants.R_OK`, `fs.constants.W_OK`, and `fs.constants.X_OK`
(e.g.`fs.constants.W_OK | fs.constants.R_OK`). Check `File access constants` for
possible values of `mode`.

If the accessibility check is successful, the promise is fulfilled with no
value. If any of the accessibility checks fail, the promise is rejected
with an [Error](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Error) object. The following example checks if the file`/etc/passwd` can be read and
written by the current process.

```js
import { access, constants } from 'fs/promises';

try {
  await access('/etc/passwd', constants.R_OK | constants.W_OK);
  console.log('can access');
} catch {
  console.error('cannot access');
}
```

Using `fsPromises.access()` to check for the accessibility of a file before
calling `fsPromises.open()` is not recommended. Doing so introduces a race
condition, since other processes may change the file's state between the two
calls. Instead, user code should open/read/write the file directly and handle
the error raised if the file is not accessible.

#### Parameters

| Parameter | Type | Description |
| ------ | ------ | ------ |
| `path` | `string` | - |
| `mode`? | `number` |  |

#### Returns

`Promise`\<`void`\>

Fulfills with `undefined` upon success.

***

### chmod()

> **chmod**(`path`: `string`, `mode`: `number`): `Promise`\<`void`\>

Changes the permissions of a file.

#### Parameters

| Parameter | Type |
| ------ | ------ |
| `path` | `string` |
| `mode` | `number` |

#### Returns

`Promise`\<`void`\>

Fulfills with `undefined` upon success.

***

### mkdir()

> **mkdir**(`path`: `string`, `options`?: [`MakeDirectoryOptions`](../index.md#makedirectoryoptions)): `Promise`\<`string`\>

Asynchronously creates a directory.

The optional `options` argument can be an object with a `mode` property and a `recursive` property indicating whether parent directories should be created.
Calling `fsPromises.mkdir()` when `path` is a directory that exists results in a rejection only when `recursive` is false.

```js
import { mkdir } from 'fs/promises';

try {
  const projectFolder = './test/project/123';
  const createDir = await mkdir(projectFolder, { recursive: true });

  console.log(`created ${createDir}`);
} catch (err) {
  console.error(err.message);
}
```

#### Parameters

| Parameter | Type |
| ------ | ------ |
| `path` | `string` |
| `options`? | [`MakeDirectoryOptions`](../index.md#makedirectoryoptions) |

#### Returns

`Promise`\<`string`\>

Upon success, fulfills with `undefined` if `recursive` is `false`, or the first directory path created if `recursive` is `true`.

***

### mkdtemp()

> **mkdtemp**(`prefix`: `string`): `Promise`\<`string`\>

Creates a unique temporary directory. A unique directory name is generated by
appending six random characters to the end of the provided `prefix`. Due to
platform inconsistencies, avoid trailing `X` characters in `prefix`. Some
platforms, notably the BSDs, can return more than six random characters, and
replace trailing `X` characters in `prefix` with random characters.

```js
import { mkdtemp } from 'fs/promises';
import { join } from 'path';
import { tmpdir } from 'os';

try {
  await mkdtemp(join(tmpdir(), 'foo-'));
} catch (err) {
  console.error(err);
}
```

The `fsPromises.mkdtemp()` method will append the six randomly selected
characters directly to the `prefix` string. For instance, given a directory `/tmp`, if the intention is to create a temporary directory _within_ `/tmp`, the `prefix` must end with a trailing
platform-specific path separator
(`require('path').sep`).

#### Parameters

| Parameter | Type |
| ------ | ------ |
| `prefix` | `string` |

#### Returns

`Promise`\<`string`\>

Fulfills with a string containing the file system path of the newly created temporary directory.

***

### open()

> **open**(`path`: `string`, `flags`?: [`FileSystemFlags`](promises.md#filesystemflags), `mode`?: `number`): `Promise`\<[`FileHandle`](promises.md#filehandle)\>

Opens a `FileHandle`.

Refer to the POSIX [`open(2)`](http://man7.org/linux/man-pages/man2/open.2.html) documentation for more detail.

Some characters (`< > : " / \ | ? *`) are reserved under Windows as documented
by [Naming Files, Paths, and Namespaces](https://docs.microsoft.com/en-us/windows/desktop/FileIO/naming-a-file).

#### Parameters

| Parameter | Type | Description |
| ------ | ------ | ------ |
| `path` | `string` | - |
| `flags`? | [`FileSystemFlags`](promises.md#filesystemflags) | See {FileSystemFlags}. |
| `mode`? | `number` | Sets the file mode if the file is created (UNIX). |

#### Returns

`Promise`\<[`FileHandle`](promises.md#filehandle)\>

Fulfills with a {FileHandle} object.

***

### readdir()

#### Call Signature

> **readdir**(`path`: `string`, `options`?: `object`): `Promise`\<`string`[]\>

Reads the contents of a directory.

If `options.withFileTypes` is set to `true`, the returned array will contain `fs.Dirent` objects.

```js
import { readdir } from 'fs/promises';

try {
  const files = await readdir(path);
  for (const file of files)
    console.log(file);
} catch (err) {
  console.error(err);
}
```

##### Parameters

| Parameter | Type |
| ------ | ------ |
| `path` | `string` |
| `options`? | \{ `recursive`: `boolean`; `withFileTypes`: `false`; \} |
| `options.recursive`? | `boolean` |
| `options.withFileTypes`? | `false` |

##### Returns

`Promise`\<`string`[]\>

Fulfills with an array of the names of the files in the directory excluding `'.'` and `'..'`.

#### Call Signature

> **readdir**(`path`: `string`, `options`: `object`): `Promise`\<[`Dirent`](../index.md#dirent)[]\>

Asynchronous readdir(2) - read a directory.

##### Parameters

| Parameter | Type | Description |
| ------ | ------ | ------ |
| `path` | `string` | A path to a file. If a URL is provided, it must use the `file:` protocol. |
| `options` | \{ `recursive`: `boolean`; `withFileTypes`: `true`; \} | If called with `withFileTypes: true` the result data will be an array of Dirent. |
| `options.recursive`? | `boolean` | - |
| `options.withFileTypes` | `true` | - |

##### Returns

`Promise`\<[`Dirent`](../index.md#dirent)[]\>

***

### readFile()

#### Call Signature

> **readFile**(`path`: `string`, `options`?: `null` \| \{ `encoding`: `null`; \}): `Promise`\<[`Buffer`](../../buffer.md#buffer)\>

Asynchronously reads the entire contents of a file.

If no encoding is specified (using `options.encoding`), the data is returned
as a `Buffer` object. Otherwise, the data will be a string.

If `options` is a string, then it specifies the encoding.

When the `path` is a directory, the behavior of `fsPromises.readFile()` is
platform-specific. On macOS, Linux, and Windows, the promise will be rejected
with an error. On FreeBSD, a representation of the directory's contents will be
returned.

An example of reading a `package.json` file.

```js
import { readFile } from 'fs/promises';
try {
  const filePath = './package.json';
  const contents = await readFile(filePath, { encoding: 'utf8' });
  console.log(contents);
} catch (err) {
  console.error(err.message);
}
```

##### Parameters

| Parameter | Type | Description |
| ------ | ------ | ------ |
| `path` | `string` | filename or `FileHandle` |
| `options`? | `null` \| \{ `encoding`: `null`; \} | - |

##### Returns

`Promise`\<[`Buffer`](../../buffer.md#buffer)\>

Fulfills with the contents of the file.

#### Call Signature

> **readFile**(`path`: `string`, `options`: [`BufferEncoding`](../../buffer.md#bufferencoding) \| \{ `encoding`: [`BufferEncoding`](../../buffer.md#bufferencoding); \}): `Promise`\<`string`\>

Asynchronously reads the entire contents of a file.

##### Parameters

| Parameter | Type | Description |
| ------ | ------ | ------ |
| `path` | `string` | A path to a file. If a URL is provided, it must use the `file:` protocol. If a `FileHandle` is provided, the underlying file will _not_ be closed automatically. |
| `options` | [`BufferEncoding`](../../buffer.md#bufferencoding) \| \{ `encoding`: [`BufferEncoding`](../../buffer.md#bufferencoding); \} | An object that may contain an optional flag. If a flag is not provided, it defaults to `'r'`. |

##### Returns

`Promise`\<`string`\>

***

### rename()

> **rename**(`oldPath`: `string`, `newPath`: `string`): `Promise`\<`void`\>

Asynchronously renames a file or directory from `oldPath` to `newPath`.

```js
import { rename } from 'fs/promises';

try {
  await rename('oldfile.txt', 'newfile.txt');
  console.log('Rename complete!');
} catch (err) {
  console.error(err);
}
```

#### Parameters

| Parameter | Type | Description |
| ------ | ------ | ------ |
| `oldPath` | `string` | A path to a file or directory. |
| `newPath` | `string` | The new path for the file or directory. |

#### Returns

`Promise`\<`void`\>

Fulfills with `undefined` upon success.

***

### rm()

> **rm**(`path`: `string`, `options`?: [`RmOptions`](../index.md#rmoptions)): `Promise`\<`void`\>

Removes files and directories (modeled on the standard POSIX `rm` utility).

#### Parameters

| Parameter | Type |
| ------ | ------ |
| `path` | `string` |
| `options`? | [`RmOptions`](../index.md#rmoptions) |

#### Returns

`Promise`\<`void`\>

Fulfills with `undefined` upon success.

***

### rmdir()

> **rmdir**(`path`: `string`, `options`?: [`RmDirOptions`](../index.md#rmdiroptions)): `Promise`\<`void`\>

Removes the directory identified by `path`.

Using `fsPromises.rmdir()` on a file (not a directory) results in the
promise being rejected with an `ENOENT` error on Windows and an `ENOTDIR` error on POSIX.

To get a behavior similar to the `rm -rf` Unix command, use `fsPromises.rm()` with options `{ recursive: true, force: true }`.

#### Parameters

| Parameter | Type |
| ------ | ------ |
| `path` | `string` |
| `options`? | [`RmDirOptions`](../index.md#rmdiroptions) |

#### Returns

`Promise`\<`void`\>

Fulfills with `undefined` upon success.

***

### stat()

> **stat**(`path`: `string`): `Promise`\<[`Stats`](../index.md#stats)\>

Asynchronous stat - Get file status.

#### Parameters

| Parameter | Type | Description |
| ------ | ------ | ------ |
| `path` | `string` | A path to a file. |

#### Returns

`Promise`\<[`Stats`](../index.md#stats)\>

Fulfills with the {fs.Stats} object for the given `path`.

***

### writeFile()

> **writeFile**(`file`: `string`, `data`: `string` \| `ArrayBuffer` \| `SharedArrayBuffer` \| [`ArrayBufferView`](../../globals/namespaces/QuickJS.md#arraybufferview) \| [`Buffer`](../../buffer.md#buffer)): `Promise`\<`void`\>

Asynchronously writes data to a file, replacing the file if it already exists.

The `encoding` option is ignored if `data` is a buffer.

It is unsafe to use `fsPromises.writeFile()` multiple times on the same file
without waiting for the promise to be settled.

Similarly to `fsPromises.readFile` \- `fsPromises.writeFile` is a convenience
method that performs multiple `write` calls internally to write the buffer
passed to it.

#### Parameters

| Parameter | Type | Description |
| ------ | ------ | ------ |
| `file` | `string` | filename or `FileHandle` |
| `data` | `string` \| `ArrayBuffer` \| `SharedArrayBuffer` \| [`ArrayBufferView`](../../globals/namespaces/QuickJS.md#arraybufferview) \| [`Buffer`](../../buffer.md#buffer) | - |

#### Returns

`Promise`\<`void`\>

Fulfills with `undefined` upon success.



================================================
FILE: src/reference/modules/llrt/fs/namespaces/constants.md
================================================
[@caido/quickjs-types](../../../index.md) / [llrt/fs](../index.md) / constants

# constants

## Variables

### F\_OK

> `const` **F\_OK**: `number`

Constant for fs.access(). File is visible to the calling process.

***

### R\_OK

> `const` **R\_OK**: `number`

Constant for fs.access(). File can be read by the calling process.

***

### W\_OK

> `const` **W\_OK**: `number`

Constant for fs.access(). File can be written by the calling process.

***

### X\_OK

> `const` **X\_OK**: `number`

Constant for fs.access(). File can be executed by the calling process.



================================================
FILE: src/reference/modules/llrt/globals/index.md
================================================
[@caido/quickjs-types](../../index.md) / llrt/globals

# llrt/globals

## Namespaces

| Namespace | Description |
| ------ | ------ |
| [QuickJS](namespaces/QuickJS.md) | - |

## Classes

### EventEmitter\<T\>

#### Extended by

- [`ChildProcess`](../child_process.md#childprocess)
- [`Server`](../net.md#server)
- [`ReadableStreamInner`](../stream.md#readablestreaminner)
- [`WritableStreamInner`](../stream.md#writablestreaminner)
- [`ReadableStream`](namespaces/QuickJS.md#readablestream)
- [`WritableStream`](namespaces/QuickJS.md#writablestream)

#### Type Parameters

| Type Parameter | Default type |
| ------ | ------ |
| `T` *extends* [`EventMap`](index.md#eventmapt)\<`T`\> | [`DefaultEventMap`](index.md#defaulteventmap) |

#### Constructors

##### new EventEmitter()

> **new EventEmitter**\<`T`\>(): [`EventEmitter`](index.md#eventemittert)\<`T`\>

###### Returns

[`EventEmitter`](index.md#eventemittert)\<`T`\>

#### Methods

##### addListener()

> **addListener**\<`K`\>(`eventName`: [`Key`](index.md#keyk-t)\<`K`, `T`\>, `listener`: [`Listener`](index.md#listenerk-t-f)\<`K`, `T`, (...`args`: `any`[]) => `void`\>): `this`

Alias for `emitter.on(eventName, listener)`.

###### Type Parameters

| Type Parameter |
| ------ |
| `K` |

###### Parameters

| Parameter | Type |
| ------ | ------ |
| `eventName` | [`Key`](index.md#keyk-t)\<`K`, `T`\> |
| `listener` | [`Listener`](index.md#listenerk-t-f)\<`K`, `T`, (...`args`: `any`[]) => `void`\> |

###### Returns

`this`

##### emit()

> **emit**\<`K`\>(`eventName`: [`Key`](index.md#keyk-t)\<`K`, `T`\>, ...`args`: [`Args`](index.md#argsk-t)\<`K`, `T`\>): `void`

Synchronously calls each of the listeners registered for the event named `eventName`, in the order they were registered, passing the supplied arguments
to each.

```js
import { EventEmitter } from 'events';
const myEmitter = new EventEmitter();

// First listener
myEmitter.on('event', function firstListener() {
  console.log('Helloooo! first listener');
});
// Second listener
myEmitter.on('event', function secondListener(arg1, arg2) {
  console.log(`event with parameters ${arg1}, ${arg2} in second listener`);
});
// Third listener
myEmitter.on('event', function thirdListener(...args) {
  const parameters = args.join(', ');
  console.log(`event with parameters ${parameters} in third listener`);
});

myEmitter.emit('event', 1, 2, 3, 4, 5);

// Prints:
// Helloooo! first listener
// event with parameters 1, 2 in second listener
// event with parameters 1, 2, 3, 4, 5 in third listener
```

###### Type Parameters

| Type Parameter |
| ------ |
| `K` |

###### Parameters

| Parameter | Type |
| ------ | ------ |
| `eventName` | [`Key`](index.md#keyk-t)\<`K`, `T`\> |
| ...`args` | [`Args`](index.md#argsk-t)\<`K`, `T`\> |

###### Returns

`void`

##### eventNames()

> **eventNames**(): [`EventKey`](../dom-events.md#eventkey) & [`Key2`](index.md#key2k-t)\<`unknown`, `T`\>[]

Returns an array listing the events for which the emitter has registered
listeners. The values in the array are strings or `Symbol`s.

```js
import { EventEmitter } from 'events';

const myEE = new EventEmitter();
myEE.on('foo', () => {});
myEE.on('bar', () => {});

const sym = Symbol('symbol');
myEE.on(sym, () => {});

console.log(myEE.eventNames());
// Prints: [ 'foo', 'bar', Symbol(symbol) ]
```

###### Returns

[`EventKey`](../dom-events.md#eventkey) & [`Key2`](index.md#key2k-t)\<`unknown`, `T`\>[]

##### off()

> **off**\<`K`\>(`eventName`: [`Key`](index.md#keyk-t)\<`K`, `T`\>, `listener`: [`Listener`](index.md#listenerk-t-f)\<`K`, `T`, (...`args`: `any`[]) => `void`\>): `this`

Alias for `emitter.removeListener()`.

###### Type Parameters

| Type Parameter |
| ------ |
| `K` |

###### Parameters

| Parameter | Type |
| ------ | ------ |
| `eventName` | [`Key`](index.md#keyk-t)\<`K`, `T`\> |
| `listener` | [`Listener`](index.md#listenerk-t-f)\<`K`, `T`, (...`args`: `any`[]) => `void`\> |

###### Returns

`this`

##### on()

> **on**\<`K`\>(`eventName`: [`Key`](index.md#keyk-t)\<`K`, `T`\>, `listener`: [`Listener`](index.md#listenerk-t-f)\<`K`, `T`, (...`args`: `any`[]) => `void`\>): `this`

Adds the `listener` function to the end of the listeners array for the event
named `eventName`. No checks are made to see if the `listener` has already
been added. Multiple calls passing the same combination of `eventName` and
`listener` will result in the `listener` being added, and called, multiple times.

```js
server.on('connection', (stream) => {
  console.log('someone connected!');
});
```

Returns a reference to the `EventEmitter`, so that calls can be chained.

By default, event listeners are invoked in the order they are added. The `emitter.prependListener()` method can be used as an alternative to add the
event listener to the beginning of the listeners array.

```js
import { EventEmitter } from 'events';
const myEE = new EventEmitter();
myEE.on('foo', () => console.log('a'));
myEE.prependListener('foo', () => console.log('b'));
myEE.emit('foo');
// Prints:
//   b
//   a
```

###### Type Parameters

| Type Parameter |
| ------ |
| `K` |

###### Parameters

| Parameter | Type | Description |
| ------ | ------ | ------ |
| `eventName` | [`Key`](index.md#keyk-t)\<`K`, `T`\> | The name of the event. |
| `listener` | [`Listener`](index.md#listenerk-t-f)\<`K`, `T`, (...`args`: `any`[]) => `void`\> | The callback function |

###### Returns

`this`

##### once()

> **once**\<`K`\>(`eventName`: [`Key`](index.md#keyk-t)\<`K`, `T`\>, `listener`: [`Listener`](index.md#listenerk-t-f)\<`K`, `T`, (...`args`: `any`[]) => `void`\>): `this`

Adds a **one-time** `listener` function for the event named `eventName`. The
next time `eventName` is triggered, this listener is removed and then invoked.

Returns a reference to the `EventEmitter`, so that calls can be chained.

By default, event listeners are invoked in the order they are added. The `emitter.prependOnceListener()` method can be used as an alternative to add the
event listener to the beginning of the listeners array.

```js
import { EventEmitter } from 'events';
const myEE = new EventEmitter();
myEE.once('foo', () => console.log('a'));
myEE.prependOnceListener('foo', () => console.log('b'));
myEE.emit('foo');
// Prints:
//   b
//   a
```

###### Type Parameters

| Type Parameter |
| ------ |
| `K` |

###### Parameters

| Parameter | Type | Description |
| ------ | ------ | ------ |
| `eventName` | [`Key`](index.md#keyk-t)\<`K`, `T`\> | The name of the event. |
| `listener` | [`Listener`](index.md#listenerk-t-f)\<`K`, `T`, (...`args`: `any`[]) => `void`\> | The callback function |

###### Returns

`this`

###### Since

v0.3.0

##### prependListener()

> **prependListener**\<`K`\>(`eventName`: [`Key`](index.md#keyk-t)\<`K`, `T`\>, `listener`: [`Listener`](index.md#listenerk-t-f)\<`K`, `T`, (...`args`: `any`[]) => `void`\>): `this`

Adds the `listener` function to the _beginning_ of the listeners array for the
event named `eventName`. No checks are made to see if the `listener` has
already been added. Multiple calls passing the same combination of `eventName`
and `listener` will result in the `listener` being added, and called, multiple times.

Returns a reference to the `EventEmitter`, so that calls can be chained.

###### Type Parameters

| Type Parameter |
| ------ |
| `K` |

###### Parameters

| Parameter | Type | Description |
| ------ | ------ | ------ |
| `eventName` | [`Key`](index.md#keyk-t)\<`K`, `T`\> | The name of the event. |
| `listener` | [`Listener`](index.md#listenerk-t-f)\<`K`, `T`, (...`args`: `any`[]) => `void`\> | The callback function |

###### Returns

`this`

##### prependOnceListener()

> **prependOnceListener**\<`K`\>(`eventName`: [`Key`](index.md#keyk-t)\<`K`, `T`\>, `listener`: [`Listener`](index.md#listenerk-t-f)\<`K`, `T`, (...`args`: `any`[]) => `void`\>): `this`

Adds a **one-time**`listener` function for the event named `eventName` to the _beginning_ of the listeners array.
The next time `eventName` is triggered, this listener is removed, and then invoked.

Returns a reference to the `EventEmitter`, so that calls can be chained.

###### Type Parameters

| Type Parameter |
| ------ |
| `K` |

###### Parameters

| Parameter | Type | Description |
| ------ | ------ | ------ |
| `eventName` | [`Key`](index.md#keyk-t)\<`K`, `T`\> | The name of the event. |
| `listener` | [`Listener`](index.md#listenerk-t-f)\<`K`, `T`, (...`args`: `any`[]) => `void`\> | The callback function |

###### Returns

`this`

##### removeListener()

> **removeListener**\<`K`\>(`eventName`: [`Key`](index.md#keyk-t)\<`K`, `T`\>, `listener`: [`Listener`](index.md#listenerk-t-f)\<`K`, `T`, (...`args`: `any`[]) => `void`\>): `this`

Removes the specified `listener` from the listener array for the event named `eventName`.

`removeListener()` will remove, at most, one instance of a listener from the
listener array. If any single listener has been added multiple times to the
listener array for the specified `eventName`, then `removeListener()` must be
called multiple times to remove each instance.

Once an event is emitted, all listeners attached to it at the time of emitting are called in order.
This implies that any `removeListener()` calls _after_ emitting and _before_ the last listener finishes execution
will not remove them from `emit()` in progress. Subsequent events behave as expected.

```js
import { EventEmitter } from 'events';
class MyEmitter extends EventEmitter {}
const myEmitter = new MyEmitter();

const callbackA = () => {
  console.log('A');
  myEmitter.removeListener('event', callbackB);
};

const callbackB = () => {
  console.log('B');
};

myEmitter.on('event', callbackA);

myEmitter.on('event', callbackB);

// callbackA removes listener callbackB but it will still be called.
// Internal listener array at time of emit [callbackA, callbackB]
myEmitter.emit('event');
// Prints:
//   A
//   B

// callbackB is now removed.
// Internal listener array [callbackA]
myEmitter.emit('event');
// Prints:
//   A
```

Because listeners are managed using an internal array, calling this will
change the position indices of any listener registered _after_ the listener
being removed. This will not impact the order in which listeners are called,
but it means that any copies of the listener array as returned by
the `emitter.listeners()` method will need to be recreated.

When a single function has been added as a handler multiple times for a single
event (as in the example below), `removeListener()` will remove the most
recently added instance. In the example the `once('ping')` listener is removed:

```js
import { EventEmitter } from 'events';
const ee = new EventEmitter();

function pong() {
  console.log('pong');
}

ee.on('ping', pong);
ee.once('ping', pong);
ee.removeListener('ping', pong);

ee.emit('ping');
ee.emit('ping');
```

Returns a reference to the `EventEmitter`, so that calls can be chained.

###### Type Parameters

| Type Parameter |
| ------ |
| `K` |

###### Parameters

| Parameter | Type |
| ------ | ------ |
| `eventName` | [`Key`](index.md#keyk-t)\<`K`, `T`\> |
| `listener` | [`Listener`](index.md#listenerk-t-f)\<`K`, `T`, (...`args`: `any`[]) => `void`\> |

###### Returns

`this`

## Type Aliases

### AnyRest

> **AnyRest**: \[`any`[]\]

***

### Args\<K, T\>

> **Args**\<`K`, `T`\>: `T` *extends* [`DefaultEventMap`](index.md#defaulteventmap) ? [`AnyRest`](index.md#anyrest) : `K` *extends* keyof `T` ? `T`\[`K`\] : `never`

#### Type Parameters

| Type Parameter |
| ------ |
| `K` |
| `T` |

***

### DefaultEventMap

> **DefaultEventMap**: \[`never`\]

***

### EventMap\<T\>

> **EventMap**\<`T`\>: `Record`\<keyof `T`, `any`[]\> \| [`DefaultEventMap`](index.md#defaulteventmap)

#### Type Parameters

| Type Parameter |
| ------ |
| `T` |

***

### Key\<K, T\>

> **Key**\<`K`, `T`\>: `T` *extends* [`DefaultEventMap`](index.md#defaulteventmap) ? [`EventKey`](../dom-events.md#eventkey) : `K` \| keyof `T`

#### Type Parameters

| Type Parameter |
| ------ |
| `K` |
| `T` |

***

### Key2\<K, T\>

> **Key2**\<`K`, `T`\>: `T` *extends* [`DefaultEventMap`](index.md#defaulteventmap) ? [`EventKey`](../dom-events.md#eventkey) : `K` & keyof `T`

#### Type Parameters

| Type Parameter |
| ------ |
| `K` |
| `T` |

***

### Listener\<K, T, F\>

> **Listener**\<`K`, `T`, `F`\>: `T` *extends* [`DefaultEventMap`](index.md#defaulteventmap) ? `F` : `K` *extends* keyof `T` ? `T`\[`K`\] *extends* `unknown`[] ? (...`args`: `T`\[`K`\]) => `void` : `never` : `never`

#### Type Parameters

| Type Parameter |
| ------ |
| `K` |
| `T` |
| `F` |



================================================
FILE: src/reference/modules/llrt/globals/namespaces/QuickJS.md
================================================
[@caido/quickjs-types](../../../index.md) / [llrt/globals](../index.md) / QuickJS

# QuickJS

## Interfaces

### ReadableStream

#### Extends

- [`EventEmitter`](../index.md#eventemittert)

#### Methods

##### addListener()

> **addListener**\<`K`\>(`eventName`: [`EventKey`](../../dom-events.md#eventkey), `listener`: (...`args`: `any`[]) => `void`): `this`

Alias for `emitter.on(eventName, listener)`.

###### Type Parameters

| Type Parameter |
| ------ |
| `K` |

###### Parameters

| Parameter | Type |
| ------ | ------ |
| `eventName` | [`EventKey`](../../dom-events.md#eventkey) |
| `listener` | (...`args`: `any`[]) => `void` |

###### Returns

`this`

###### Inherited from

[`EventEmitter`](../index.md#eventemittert).[`addListener`](../index.md#addlistener)

##### emit()

> **emit**\<`K`\>(`eventName`: [`EventKey`](../../dom-events.md#eventkey), ...`args`: [`AnyRest`](../index.md#anyrest)): `void`

Synchronously calls each of the listeners registered for the event named `eventName`, in the order they were registered, passing the supplied arguments
to each.

```js
import { EventEmitter } from 'events';
const myEmitter = new EventEmitter();

// First listener
myEmitter.on('event', function firstListener() {
  console.log('Helloooo! first listener');
});
// Second listener
myEmitter.on('event', function secondListener(arg1, arg2) {
  console.log(`event with parameters ${arg1}, ${arg2} in second listener`);
});
// Third listener
myEmitter.on('event', function thirdListener(...args) {
  const parameters = args.join(', ');
  console.log(`event with parameters ${parameters} in third listener`);
});

myEmitter.emit('event', 1, 2, 3, 4, 5);

// Prints:
// Helloooo! first listener
// event with parameters 1, 2 in second listener
// event with parameters 1, 2, 3, 4, 5 in third listener
```

###### Type Parameters

| Type Parameter |
| ------ |
| `K` |

###### Parameters

| Parameter | Type |
| ------ | ------ |
| `eventName` | [`EventKey`](../../dom-events.md#eventkey) |
| ...`args` | [`AnyRest`](../index.md#anyrest) |

###### Returns

`void`

###### Inherited from

[`EventEmitter`](../index.md#eventemittert).[`emit`](../index.md#emit)

##### eventNames()

> **eventNames**(): [`EventKey`](../../dom-events.md#eventkey)[]

Returns an array listing the events for which the emitter has registered
listeners. The values in the array are strings or `Symbol`s.

```js
import { EventEmitter } from 'events';

const myEE = new EventEmitter();
myEE.on('foo', () => {});
myEE.on('bar', () => {});

const sym = Symbol('symbol');
myEE.on(sym, () => {});

console.log(myEE.eventNames());
// Prints: [ 'foo', 'bar', Symbol(symbol) ]
```

###### Returns

[`EventKey`](../../dom-events.md#eventkey)[]

###### Inherited from

[`EventEmitter`](../index.md#eventemittert).[`eventNames`](../index.md#eventnames)

##### off()

> **off**\<`K`\>(`eventName`: [`EventKey`](../../dom-events.md#eventkey), `listener`: (...`args`: `any`[]) => `void`): `this`

Alias for `emitter.removeListener()`.

###### Type Parameters

| Type Parameter |
| ------ |
| `K` |

###### Parameters

| Parameter | Type |
| ------ | ------ |
| `eventName` | [`EventKey`](../../dom-events.md#eventkey) |
| `listener` | (...`args`: `any`[]) => `void` |

###### Returns

`this`

###### Inherited from

[`EventEmitter`](../index.md#eventemittert).[`off`](../index.md#off)

##### on()

> **on**\<`K`\>(`eventName`: [`EventKey`](../../dom-events.md#eventkey), `listener`: (...`args`: `any`[]) => `void`): `this`

Adds the `listener` function to the end of the listeners array for the event
named `eventName`. No checks are made to see if the `listener` has already
been added. Multiple calls passing the same combination of `eventName` and
`listener` will result in the `listener` being added, and called, multiple times.

```js
server.on('connection', (stream) => {
  console.log('someone connected!');
});
```

Returns a reference to the `EventEmitter`, so that calls can be chained.

By default, event listeners are invoked in the order they are added. The `emitter.prependListener()` method can be used as an alternative to add the
event listener to the beginning of the listeners array.

```js
import { EventEmitter } from 'events';
const myEE = new EventEmitter();
myEE.on('foo', () => console.log('a'));
myEE.prependListener('foo', () => console.log('b'));
myEE.emit('foo');
// Prints:
//   b
//   a
```

###### Type Parameters

| Type Parameter |
| ------ |
| `K` |

###### Parameters

| Parameter | Type | Description |
| ------ | ------ | ------ |
| `eventName` | [`EventKey`](../../dom-events.md#eventkey) | The name of the event. |
| `listener` | (...`args`: `any`[]) => `void` | The callback function |

###### Returns

`this`

###### Inherited from

[`EventEmitter`](../index.md#eventemittert).[`on`](../index.md#on)

##### once()

> **once**\<`K`\>(`eventName`: [`EventKey`](../../dom-events.md#eventkey), `listener`: (...`args`: `any`[]) => `void`): `this`

Adds a **one-time** `listener` function for the event named `eventName`. The
next time `eventName` is triggered, this listener is removed and then invoked.

Returns a reference to the `EventEmitter`, so that calls can be chained.

By default, event listeners are invoked in the order they are added. The `emitter.prependOnceListener()` method can be used as an alternative to add the
event listener to the beginning of the listeners array.

```js
import { EventEmitter } from 'events';
const myEE = new EventEmitter();
myEE.once('foo', () => console.log('a'));
myEE.prependOnceListener('foo', () => console.log('b'));
myEE.emit('foo');
// Prints:
//   b
//   a
```

###### Type Parameters

| Type Parameter |
| ------ |
| `K` |

###### Parameters

| Parameter | Type | Description |
| ------ | ------ | ------ |
| `eventName` | [`EventKey`](../../dom-events.md#eventkey) | The name of the event. |
| `listener` | (...`args`: `any`[]) => `void` | The callback function |

###### Returns

`this`

###### Since

v0.3.0

###### Inherited from

[`EventEmitter`](../index.md#eventemittert).[`once`](../index.md#once)

##### prependListener()

> **prependListener**\<`K`\>(`eventName`: [`EventKey`](../../dom-events.md#eventkey), `listener`: (...`args`: `any`[]) => `void`): `this`

Adds the `listener` function to the _beginning_ of the listeners array for the
event named `eventName`. No checks are made to see if the `listener` has
already been added. Multiple calls passing the same combination of `eventName`
and `listener` will result in the `listener` being added, and called, multiple times.

Returns a reference to the `EventEmitter`, so that calls can be chained.

###### Type Parameters

| Type Parameter |
| ------ |
| `K` |

###### Parameters

| Parameter | Type | Description |
| ------ | ------ | ------ |
| `eventName` | [`EventKey`](../../dom-events.md#eventkey) | The name of the event. |
| `listener` | (...`args`: `any`[]) => `void` | The callback function |

###### Returns

`this`

###### Inherited from

[`EventEmitter`](../index.md#eventemittert).[`prependListener`](../index.md#prependlistener)

##### prependOnceListener()

> **prependOnceListener**\<`K`\>(`eventName`: [`EventKey`](../../dom-events.md#eventkey), `listener`: (...`args`: `any`[]) => `void`): `this`

Adds a **one-time**`listener` function for the event named `eventName` to the _beginning_ of the listeners array.
The next time `eventName` is triggered, this listener is removed, and then invoked.

Returns a reference to the `EventEmitter`, so that calls can be chained.

###### Type Parameters

| Type Parameter |
| ------ |
| `K` |

###### Parameters

| Parameter | Type | Description |
| ------ | ------ | ------ |
| `eventName` | [`EventKey`](../../dom-events.md#eventkey) | The name of the event. |
| `listener` | (...`args`: `any`[]) => `void` | The callback function |

###### Returns

`this`

###### Inherited from

[`EventEmitter`](../index.md#eventemittert).[`prependOnceListener`](../index.md#prependoncelistener)

##### read()

> **read**(`size`?: `number`): `null` \| [`Buffer`](../../buffer.md#buffer)

###### Parameters

| Parameter | Type |
| ------ | ------ |
| `size`? | `number` |

###### Returns

`null` \| [`Buffer`](../../buffer.md#buffer)

##### removeListener()

> **removeListener**\<`K`\>(`eventName`: [`EventKey`](../../dom-events.md#eventkey), `listener`: (...`args`: `any`[]) => `void`): `this`

Removes the specified `listener` from the listener array for the event named `eventName`.

`removeListener()` will remove, at most, one instance of a listener from the
listener array. If any single listener has been added multiple times to the
listener array for the specified `eventName`, then `removeListener()` must be
called multiple times to remove each instance.

Once an event is emitted, all listeners attached to it at the time of emitting are called in order.
This implies that any `removeListener()` calls _after_ emitting and _before_ the last listener finishes execution
will not remove them from `emit()` in progress. Subsequent events behave as expected.

```js
import { EventEmitter } from 'events';
class MyEmitter extends EventEmitter {}
const myEmitter = new MyEmitter();

const callbackA = () => {
  console.log('A');
  myEmitter.removeListener('event', callbackB);
};

const callbackB = () => {
  console.log('B');
};

myEmitter.on('event', callbackA);

myEmitter.on('event', callbackB);

// callbackA removes listener callbackB but it will still be called.
// Internal listener array at time of emit [callbackA, callbackB]
myEmitter.emit('event');
// Prints:
//   A
//   B

// callbackB is now removed.
// Internal listener array [callbackA]
myEmitter.emit('event');
// Prints:
//   A
```

Because listeners are managed using an internal array, calling this will
change the position indices of any listener registered _after_ the listener
being removed. This will not impact the order in which listeners are called,
but it means that any copies of the listener array as returned by
the `emitter.listeners()` method will need to be recreated.

When a single function has been added as a handler multiple times for a single
event (as in the example below), `removeListener()` will remove the most
recently added instance. In the example the `once('ping')` listener is removed:

```js
import { EventEmitter } from 'events';
const ee = new EventEmitter();

function pong() {
  console.log('pong');
}

ee.on('ping', pong);
ee.once('ping', pong);
ee.removeListener('ping', pong);

ee.emit('ping');
ee.emit('ping');
```

Returns a reference to the `EventEmitter`, so that calls can be chained.

###### Type Parameters

| Type Parameter |
| ------ |
| `K` |

###### Parameters

| Parameter | Type |
| ------ | ------ |
| `eventName` | [`EventKey`](../../dom-events.md#eventkey) |
| `listener` | (...`args`: `any`[]) => `void` |

###### Returns

`this`

###### Inherited from

[`EventEmitter`](../index.md#eventemittert).[`removeListener`](../index.md#removelistener)

***

### WritableStream

#### Extends

- [`EventEmitter`](../index.md#eventemittert)

#### Methods

##### addListener()

> **addListener**\<`K`\>(`eventName`: [`EventKey`](../../dom-events.md#eventkey), `listener`: (...`args`: `any`[]) => `void`): `this`

Alias for `emitter.on(eventName, listener)`.

###### Type Parameters

| Type Parameter |
| ------ |
| `K` |

###### Parameters

| Parameter | Type |
| ------ | ------ |
| `eventName` | [`EventKey`](../../dom-events.md#eventkey) |
| `listener` | (...`args`: `any`[]) => `void` |

###### Returns

`this`

###### Inherited from

[`EventEmitter`](../index.md#eventemittert).[`addListener`](../index.md#addlistener)

##### emit()

> **emit**\<`K`\>(`eventName`: [`EventKey`](../../dom-events.md#eventkey), ...`args`: [`AnyRest`](../index.md#anyrest)): `void`

Synchronously calls each of the listeners registered for the event named `eventName`, in the order they were registered, passing the supplied arguments
to each.

```js
import { EventEmitter } from 'events';
const myEmitter = new EventEmitter();

// First listener
myEmitter.on('event', function firstListener() {
  console.log('Helloooo! first listener');
});
// Second listener
myEmitter.on('event', function secondListener(arg1, arg2) {
  console.log(`event with parameters ${arg1}, ${arg2} in second listener`);
});
// Third listener
myEmitter.on('event', function thirdListener(...args) {
  const parameters = args.join(', ');
  console.log(`event with parameters ${parameters} in third listener`);
});

myEmitter.emit('event', 1, 2, 3, 4, 5);

// Prints:
// Helloooo! first listener
// event with parameters 1, 2 in second listener
// event with parameters 1, 2, 3, 4, 5 in third listener
```

###### Type Parameters

| Type Parameter |
| ------ |
| `K` |

###### Parameters

| Parameter | Type |
| ------ | ------ |
| `eventName` | [`EventKey`](../../dom-events.md#eventkey) |
| ...`args` | [`AnyRest`](../index.md#anyrest) |

###### Returns

`void`

###### Inherited from

[`EventEmitter`](../index.md#eventemittert).[`emit`](../index.md#emit)

##### end()

> **end**(): `this`

###### Returns

`this`

##### eventNames()

> **eventNames**(): [`EventKey`](../../dom-events.md#eventkey)[]

Returns an array listing the events for which the emitter has registered
listeners. The values in the array are strings or `Symbol`s.

```js
import { EventEmitter } from 'events';

const myEE = new EventEmitter();
myEE.on('foo', () => {});
myEE.on('bar', () => {});

const sym = Symbol('symbol');
myEE.on(sym, () => {});

console.log(myEE.eventNames());
// Prints: [ 'foo', 'bar', Symbol(symbol) ]
```

###### Returns

[`EventKey`](../../dom-events.md#eventkey)[]

###### Inherited from

[`EventEmitter`](../index.md#eventemittert).[`eventNames`](../index.md#eventnames)

##### off()

> **off**\<`K`\>(`eventName`: [`EventKey`](../../dom-events.md#eventkey), `listener`: (...`args`: `any`[]) => `void`): `this`

Alias for `emitter.removeListener()`.

###### Type Parameters

| Type Parameter |
| ------ |
| `K` |

###### Parameters

| Parameter | Type |
| ------ | ------ |
| `eventName` | [`EventKey`](../../dom-events.md#eventkey) |
| `listener` | (...`args`: `any`[]) => `void` |

###### Returns

`this`

###### Inherited from

[`EventEmitter`](../index.md#eventemittert).[`off`](../index.md#off)

##### on()

> **on**\<`K`\>(`eventName`: [`EventKey`](../../dom-events.md#eventkey), `listener`: (...`args`: `any`[]) => `void`): `this`

Adds the `listener` function to the end of the listeners array for the event
named `eventName`. No checks are made to see if the `listener` has already
been added. Multiple calls passing the same combination of `eventName` and
`listener` will result in the `listener` being added, and called, multiple times.

```js
server.on('connection', (stream) => {
  console.log('someone connected!');
});
```

Returns a reference to the `EventEmitter`, so that calls can be chained.

By default, event listeners are invoked in the order they are added. The `emitter.prependListener()` method can be used as an alternative to add the
event listener to the beginning of the listeners array.

```js
import { EventEmitter } from 'events';
const myEE = new EventEmitter();
myEE.on('foo', () => console.log('a'));
myEE.prependListener('foo', () => console.log('b'));
myEE.emit('foo');
// Prints:
//   b
//   a
```

###### Type Parameters

| Type Parameter |
| ------ |
| `K` |

###### Parameters

| Parameter | Type | Description |
| ------ | ------ | ------ |
| `eventName` | [`EventKey`](../../dom-events.md#eventkey) | The name of the event. |
| `listener` | (...`args`: `any`[]) => `void` | The callback function |

###### Returns

`this`

###### Inherited from

[`EventEmitter`](../index.md#eventemittert).[`on`](../index.md#on)

##### once()

> **once**\<`K`\>(`eventName`: [`EventKey`](../../dom-events.md#eventkey), `listener`: (...`args`: `any`[]) => `void`): `this`

Adds a **one-time** `listener` function for the event named `eventName`. The
next time `eventName` is triggered, this listener is removed and then invoked.

Returns a reference to the `EventEmitter`, so that calls can be chained.

By default, event listeners are invoked in the order they are added. The `emitter.prependOnceListener()` method can be used as an alternative to add the
event listener to the beginning of the listeners array.

```js
import { EventEmitter } from 'events';
const myEE = new EventEmitter();
myEE.once('foo', () => console.log('a'));
myEE.prependOnceListener('foo', () => console.log('b'));
myEE.emit('foo');
// Prints:
//   b
//   a
```

###### Type Parameters

| Type Parameter |
| ------ |
| `K` |

###### Parameters

| Parameter | Type | Description |
| ------ | ------ | ------ |
| `eventName` | [`EventKey`](../../dom-events.md#eventkey) | The name of the event. |
| `listener` | (...`args`: `any`[]) => `void` | The callback function |

###### Returns

`this`

###### Since

v0.3.0

###### Inherited from

[`EventEmitter`](../index.md#eventemittert).[`once`](../index.md#once)

##### prependListener()

> **prependListener**\<`K`\>(`eventName`: [`EventKey`](../../dom-events.md#eventkey), `listener`: (...`args`: `any`[]) => `void`): `this`

Adds the `listener` function to the _beginning_ of the listeners array for the
event named `eventName`. No checks are made to see if the `listener` has
already been added. Multiple calls passing the same combination of `eventName`
and `listener` will result in the `listener` being added, and called, multiple times.

Returns a reference to the `EventEmitter`, so that calls can be chained.

###### Type Parameters

| Type Parameter |
| ------ |
| `K` |

###### Parameters

| Parameter | Type | Description |
| ------ | ------ | ------ |
| `eventName` | [`EventKey`](../../dom-events.md#eventkey) | The name of the event. |
| `listener` | (...`args`: `any`[]) => `void` | The callback function |

###### Returns

`this`

###### Inherited from

[`EventEmitter`](../index.md#eventemittert).[`prependListener`](../index.md#prependlistener)

##### prependOnceListener()

> **prependOnceListener**\<`K`\>(`eventName`: [`EventKey`](../../dom-events.md#eventkey), `listener`: (...`args`: `any`[]) => `void`): `this`

Adds a **one-time**`listener` function for the event named `eventName` to the _beginning_ of the listeners array.
The next time `eventName` is triggered, this listener is removed, and then invoked.

Returns a reference to the `EventEmitter`, so that calls can be chained.

###### Type Parameters

| Type Parameter |
| ------ |
| `K` |

###### Parameters

| Parameter | Type | Description |
| ------ | ------ | ------ |
| `eventName` | [`EventKey`](../../dom-events.md#eventkey) | The name of the event. |
| `listener` | (...`args`: `any`[]) => `void` | The callback function |

###### Returns

`this`

###### Inherited from

[`EventEmitter`](../index.md#eventemittert).[`prependOnceListener`](../index.md#prependoncelistener)

##### removeListener()

> **removeListener**\<`K`\>(`eventName`: [`EventKey`](../../dom-events.md#eventkey), `listener`: (...`args`: `any`[]) => `void`): `this`

Removes the specified `listener` from the listener array for the event named `eventName`.

`removeListener()` will remove, at most, one instance of a listener from the
listener array. If any single listener has been added multiple times to the
listener array for the specified `eventName`, then `removeListener()` must be
called multiple times to remove each instance.

Once an event is emitted, all listeners attached to it at the time of emitting are called in order.
This implies that any `removeListener()` calls _after_ emitting and _before_ the last listener finishes execution
will not remove them from `emit()` in progress. Subsequent events behave as expected.

```js
import { EventEmitter } from 'events';
class MyEmitter extends EventEmitter {}
const myEmitter = new MyEmitter();

const callbackA = () => {
  console.log('A');
  myEmitter.removeListener('event', callbackB);
};

const callbackB = () => {
  console.log('B');
};

myEmitter.on('event', callbackA);

myEmitter.on('event', callbackB);

// callbackA removes listener callbackB but it will still be called.
// Internal listener array at time of emit [callbackA, callbackB]
myEmitter.emit('event');
// Prints:
//   A
//   B

// callbackB is now removed.
// Internal listener array [callbackA]
myEmitter.emit('event');
// Prints:
//   A
```

Because listeners are managed using an internal array, calling this will
change the position indices of any listener registered _after_ the listener
being removed. This will not impact the order in which listeners are called,
but it means that any copies of the listener array as returned by
the `emitter.listeners()` method will need to be recreated.

When a single function has been added as a handler multiple times for a single
event (as in the example below), `removeListener()` will remove the most
recently added instance. In the example the `once('ping')` listener is removed:

```js
import { EventEmitter } from 'events';
const ee = new EventEmitter();

function pong() {
  console.log('pong');
}

ee.on('ping', pong);
ee.once('ping', pong);
ee.removeListener('ping', pong);

ee.emit('ping');
ee.emit('ping');
```

Returns a reference to the `EventEmitter`, so that calls can be chained.

###### Type Parameters

| Type Parameter |
| ------ |
| `K` |

###### Parameters

| Parameter | Type |
| ------ | ------ |
| `eventName` | [`EventKey`](../../dom-events.md#eventkey) |
| `listener` | (...`args`: `any`[]) => `void` |

###### Returns

`this`

###### Inherited from

[`EventEmitter`](../index.md#eventemittert).[`removeListener`](../index.md#removelistener)

##### write()

> **write**(`chunk`: `string` \| `ArrayBuffer` \| `SharedArrayBuffer` \| [`ArrayBufferView`](QuickJS.md#arraybufferview) \| [`Buffer`](../../buffer.md#buffer), `callback`?: (`err`?: `null` \| `Error`) => `void`): `void`

###### Parameters

| Parameter | Type |
| ------ | ------ |
| `chunk` | `string` \| `ArrayBuffer` \| `SharedArrayBuffer` \| [`ArrayBufferView`](QuickJS.md#arraybufferview) \| [`Buffer`](../../buffer.md#buffer) |
| `callback`? | (`err`?: `null` \| `Error`) => `void` |

###### Returns

`void`

## Type Aliases

### ArrayBufferView

> **ArrayBufferView**: [`TypedArray`](QuickJS.md#typedarray) \| `DataView`

***

### Platform

> **Platform**: `"darwin"` \| `"linux"` \| `"win32"`

***

### Signals

> **Signals**: `"SIGABRT"` \| `"SIGALRM"` \| `"SIGFPE"` \| `"SIGHUP"` \| `"SIGILL"` \| `"SIGINT"` \| `"SIGKILL"` \| `"SIGPIPE"` \| `"SIGQUIT"` \| `"SIGSEGV"` \| `"SIGTERM"`

***

### TypedArray

> **TypedArray**: `Uint8Array` \| `Uint8ClampedArray` \| `Uint16Array` \| `Uint32Array` \| `Int8Array` \| `Int16Array` \| `Int32Array` \| `BigUint64Array` \| `BigInt64Array` \| `Float32Array` \| `Float64Array`



================================================
FILE: src/reference/modules/llrt/path/index.md
================================================
[@caido/quickjs-types](../../index.md) / llrt/path

# llrt/path

## Namespaces

| Namespace | Description |
| ------ | ------ |
| [export=](namespaces/export=.md) | - |

## Variables

### export=

> **export=**: [`PlatformPath`](namespaces/export=.md#platformpath)

## References

### FormatInputPathObject

Re-exports [FormatInputPathObject](namespaces/export=.md#formatinputpathobject)

### ParsedPath

Re-exports [ParsedPath](namespaces/export=.md#parsedpath)

### PlatformPath

Re-exports [PlatformPath](namespaces/export=.md#platformpath)



================================================
FILE: src/reference/modules/llrt/path/namespaces/export=.md
================================================
[@caido/quickjs-types](../../../index.md) / [llrt/path](../index.md) / export=

# export=

## Interfaces

### FormatInputPathObject

#### Properties

##### base?

> `optional` **base**: `string`

The file name including extension (if any) such as 'index.html'

##### dir?

> `optional` **dir**: `string`

The full directory path such as '/home/user/dir' or 'c:\path\dir'

##### ext?

> `optional` **ext**: `string`

The file extension (if any) such as '.html'

##### name?

> `optional` **name**: `string`

The file name without extension (if any) such as 'index'

##### root?

> `optional` **root**: `string`

The root of the path such as '/' or 'c:\'

***

### ParsedPath

A parsed path object generated by path.parse() or consumed by path.format().

#### Properties

##### base

> **base**: `string`

The file name including extension (if any) such as 'index.html'

##### dir

> **dir**: `string`

The full directory path such as '/home/user/dir' or 'c:\path\dir'

##### ext

> **ext**: `string`

The file extension (if any) such as '.html'

##### name

> **name**: `string`

The file name without extension (if any) such as 'index'

##### root

> **root**: `string`

The root of the path such as '/' or 'c:\'

***

### PlatformPath

#### Properties

##### delimiter

> `readonly` **delimiter**: `";"` \| `":"`

The platform-specific file delimiter. ';' or ':'.

##### sep

> `readonly` **sep**: "\\" \| `"/"`

The platform-specific file separator. '\\' or '/'.

#### Methods

##### basename()

> **basename**(`path`: `string`, `suffix`?: `string`): `string`

Return the last portion of a path. Similar to the Unix basename command.
Often used to extract the file name from a fully qualified path.

###### Parameters

| Parameter | Type | Description |
| ------ | ------ | ------ |
| `path` | `string` | the path to evaluate. |
| `suffix`? | `string` | optionally, an extension to remove from the result. |

###### Returns

`string`

##### dirname()

> **dirname**(`path`: `string`): `string`

Return the directory name of a path. Similar to the Unix dirname command.

###### Parameters

| Parameter | Type | Description |
| ------ | ------ | ------ |
| `path` | `string` | the path to evaluate. |

###### Returns

`string`

##### extname()

> **extname**(`path`: `string`): `string`

Return the extension of the path, from the last '.' to end of string in the last portion of the path.
If there is no '.' in the last portion of the path or the first character of it is '.', then it returns an empty string.

###### Parameters

| Parameter | Type | Description |
| ------ | ------ | ------ |
| `path` | `string` | the path to evaluate. |

###### Returns

`string`

##### format()

> **format**(`pathObject`: [`FormatInputPathObject`](export=.md#formatinputpathobject)): `string`

Returns a path string from an object - the opposite of parse().

###### Parameters

| Parameter | Type | Description |
| ------ | ------ | ------ |
| `pathObject` | [`FormatInputPathObject`](export=.md#formatinputpathobject) | path to evaluate. |

###### Returns

`string`

##### isAbsolute()

> **isAbsolute**(`path`: `string`): `boolean`

Determines whether {path} is an absolute path. An absolute path will always resolve to the same location, regardless of the working directory.

If the given {path} is a zero-length string, `false` will be returned.

###### Parameters

| Parameter | Type | Description |
| ------ | ------ | ------ |
| `path` | `string` | path to test. |

###### Returns

`boolean`

##### join()

> **join**(...`paths`: `string`[]): `string`

Join all arguments together and normalize the resulting path.

###### Parameters

| Parameter | Type | Description |
| ------ | ------ | ------ |
| ...`paths` | `string`[] | paths to join. |

###### Returns

`string`

###### Throws

if any of the path segments is not a string.

##### normalize()

> **normalize**(`path`: `string`): `string`

Normalize a string path, reducing '..' and '.' parts.
When multiple slashes are found, they're replaced by a single one; when the path contains a trailing slash, it is preserved. On Windows backslashes are used.

###### Parameters

| Parameter | Type | Description |
| ------ | ------ | ------ |
| `path` | `string` | string path to normalize. |

###### Returns

`string`

###### Throws

if `path` is not a string.

##### parse()

> **parse**(`path`: `string`): [`ParsedPath`](export=.md#parsedpath)

Returns an object from a path string - the opposite of format().

###### Parameters

| Parameter | Type | Description |
| ------ | ------ | ------ |
| `path` | `string` | path to evaluate. |

###### Returns

[`ParsedPath`](export=.md#parsedpath)

###### Throws

if `path` is not a string.

##### resolve()

> **resolve**(...`paths`: `string`[]): `string`

The right-most parameter is considered {to}. Other parameters are considered an array of {from}.

Starting from leftmost {from} parameter, resolves {to} to an absolute path.

If {to} isn't already absolute, {from} arguments are prepended in right to left order,
until an absolute path is found. If after using all {from} paths still no absolute path is found,
the current working directory is used as well. The resulting path is normalized,
and trailing slashes are removed unless the path gets resolved to the root directory.

###### Parameters

| Parameter | Type | Description |
| ------ | ------ | ------ |
| ...`paths` | `string`[] | A sequence of paths or path segments. |

###### Returns

`string`

###### Throws

if any of the arguments is not a string.



================================================
FILE: src/reference/sdks/backend/index.md
================================================
# @caido/sdk-backend

This is the reference for the backend SDK used by backend plugins.
[SDK](#events) is the main interface that provides access to various services and functionalities.

## SDK

### SDK\<API, Events\>

The SDK object available to all scripts.

#### Type Parameters

| Type Parameter | Default type |
| ------ | ------ |
| `API` | `object` |
| `Events` | `object` |

#### Properties

##### api

> **api**: [`APISDK`](index.md#apisdkapi-events)\<`API`, `Events`\>

The SDK for the API RPC service.

##### console

> **console**: [`Console`](index.md#console-1)

The console.

This is currently the same as the global `console`.

##### env

> **env**: [`EnvironmentSDK`](index.md#environmentsdk)

The SDK for the Environment service.

##### events

> **events**: [`EventsSDK`](index.md#eventssdkapi-events)\<`API`, `Events`\>

The SDK for the Events service.

##### findings

> **findings**: [`FindingsSDK`](index.md#findingssdk)

The SDK for the Findings service.

##### graphql

> **graphql**: [`GraphQLSDK`](index.md#graphqlsdk)

The SDK for the GraphQL service.

##### meta

> **meta**: [`MetaSDK`](index.md#metasdk)

The SDK for metadata information about the plugin.

##### projects

> **projects**: [`ProjectsSDK`](index.md#projectssdk)

The SDK for the Projects service.

##### replay

> **replay**: [`ReplaySDK`](index.md#replaysdk)

The SDK for the Replay service.

##### requests

> **requests**: [`RequestsSDK`](index.md#requestssdk)

The SDK for the Requests service.

##### runtime

> **runtime**: [`RuntimeSDK`](index.md#runtimesdk)

The SDK for the runtime information.

##### scope

> **scope**: [`ScopeSDK`](index.md#scopesdk)

The SDK for the Scope service.

## Meta

### MetaSDK

> **MetaSDK**: `object`

The SDK for metadata information about the plugin.

#### Type declaration

##### assetsPath()

The directory of the plugin's assets in Caido Data.
You can read static data from your plugin in this directory.
You shouldn't write anything there, as the contents can be reset at any time.

###### Returns

`string`

##### db()

Get a sqlite database for the plugin stored in Caido Data.
You can use this to store data related to your plugin.

###### Returns

`Promise`\<[`Database`](index.md#database)\>

##### path()

The directory of the plugin in Caido Data.
You can store data related to your plugin in this directory.

###### Returns

`string`

##### updateAvailable()

Check if an update is available for the plugin.

###### Returns

`Promise`\<`boolean`\>

###### Throws

If Caido Cloud is offline.

##### version()

Get the version of the plugin.
This uses the semver format.

###### Returns

`string`

## API

### APISDK\<API, Events\>

> **APISDK**\<`API`, `Events`\>: `object`

The SDK for the API RPC service.

#### Type Parameters

| Type Parameter | Default type |
| ------ | ------ |
| `API` | `object` |
| `Events` | `object` |

#### Type declaration

##### register()

Registers a new backend function for the RPC.

###### Parameters

| Parameter | Type |
| ------ | ------ |
| `name` | keyof `API` |
| `callback` | (`sdk`: [`SDK`](index.md#sdkapi-events), ...`args`: `any`[]) => `any` |

###### Returns

`void`

###### Example

```ts
sdk.api.register("multiply", (sdk: SDK, a: number, b: number) => {
   return a * b;
});
```

##### send()

Sends an event to the frontend plugin.

###### Parameters

| Parameter | Type |
| ------ | ------ |
| `event` | keyof `Events` |
| ...`args` | `any`[] |

###### Returns

`void`

###### Example

```ts
sdk.api.send("myEvent", 5, "hello");
```

## Events

### EventsSDK\<API, Events\>

> **EventsSDK**\<`API`, `Events`\>: `object`

The SDK for the API RPC service.

#### Type Parameters

| Type Parameter | Default type |
| ------ | ------ |
| `API` | `object` |
| `Events` | `object` |

#### Type declaration

##### onInterceptRequest()

Registers an callback on new intercepted requests.

This callback is called asynchronously and cannot modify requests.

###### Parameters

| Parameter | Type |
| ------ | ------ |
| `callback` | (`sdk`: [`SDK`](index.md#sdkapi-events)\<`API`, `Events`\>, `request`: [`Request`](index.md#request-1)) => [`MaybePromise`](index.md#maybepromiset-1)\<`void`\> |

###### Returns

`void`

###### Example

```ts
sdk.events.onInterceptRequest((sdk, request) => {
   // Do something with the request
});
```

##### onInterceptResponse()

Registers an callback on new intercepted responses.

This callback is called asynchronously and cannot modify responses.

###### Parameters

| Parameter | Type |
| ------ | ------ |
| `callback` | (`sdk`: [`SDK`](index.md#sdkapi-events)\<`API`, `Events`\>, `request`: [`Request`](index.md#request-1), `response`: [`Response`](index.md#response-4)) => [`MaybePromise`](index.md#maybepromiset-1)\<`void`\> |

###### Returns

`void`

###### Example

```ts
sdk.events.onInterceptResponse((sdk, request, response) => {
   // Do something with the request/response
});
```

##### onProjectChange()

Registers an callback on project change.

This callback is called asynchronously and cannot modify the project.

It can happen that the project is null if the user deleted the currently selected one.

###### Parameters

| Parameter | Type |
| ------ | ------ |
| `callback` | (`sdk`: [`SDK`](index.md#sdkapi-events)\<`API`, `Events`\>, `project`: `null` \| [`Project`](index.md#project)) => [`MaybePromise`](index.md#maybepromiset-1)\<`void`\> |

###### Returns

`void`

###### Example

```ts
sdk.events.onProjectChange((sdk, project) => {
  if (project !== null) {
    // Do something with the project
  }
});
```

## Requests

### Body

The body of a [Request](index.md#request-1) or [Response](index.md#response-4).

Calling `to<FORMAT>` will try to convert the body to the desired format.

#### Constructors

##### new Body()

> **new Body**(`data`: `string` \| `number`[] \| `Uint8Array`): [`Body`](index.md#body)

###### Parameters

| Parameter | Type |
| ------ | ------ |
| `data` | `string` \| `number`[] \| `Uint8Array` |

###### Returns

[`Body`](index.md#body)

#### Properties

##### length

> `readonly` **length**: `number`

The length of the body in bytes.

#### Methods

##### toJson()

> **toJson**(): `unknown`

Try to parse the body as JSON.

###### Returns

`unknown`

###### Throws

If the body is not valid JSON.

##### toRaw()

> **toRaw**(): `Uint8Array`

Get the raw body as an array of bytes.

###### Returns

`Uint8Array`

##### toText()

> **toText**(): `string`

Parse the body as a string.

Unprintable characters will be replaced with `�`.

###### Returns

`string`

***

### RequestSpec

A mutable Request that has not yet been sent.

#### Constructors

##### new RequestSpec()

> **new RequestSpec**(`url`: `string`): [`RequestSpec`](index.md#requestspec)

Build a new [RequestSpec](index.md#requestspec) from a URL string.
We try to infer as much information as possible from the URL, including the scheme, host, path and query.

You can convert a saved immutable [Request](index.md#request-1) object into a [RequestSpec](index.md#requestspec) object by using the `toSpec()` method.

By default:

- Method is `GET`.
- Path is `/`.

###### Parameters

| Parameter | Type |
| ------ | ------ |
| `url` | `string` |

###### Returns

[`RequestSpec`](index.md#requestspec)

###### Throws

If the URL is invalid.

###### Example

```js
const spec = new RequestSpec("https://example.com");
```

#### Methods

##### getBody()

> **getBody**(): `undefined` \| [`Body`](index.md#body)

The body of the request.

###### Returns

`undefined` \| [`Body`](index.md#body)

##### getHeader()

> **getHeader**(`name`: `string`): `undefined` \| `string`[]

Get a header value.

Header name is case-insensitive.
The header might have multiple values.

###### Parameters

| Parameter | Type |
| ------ | ------ |
| `name` | `string` |

###### Returns

`undefined` \| `string`[]

##### getHeaders()

> **getHeaders**(): `Record`\<`string`, `string`[]\>

The headers of the request.

Header names are case-insensitive.
Each header might have multiple values.

###### Returns

`Record`\<`string`, `string`[]\>

###### Example

```json
{
  "Host": ["caido.io"],
  "Connection": ["keep-alive"],
  "Content-Length": ["95"]
}
```

##### getHost()

> **getHost**(): `string`

Get the host of the request.

###### Returns

`string`

##### getMethod()

###### Call Signature

> **getMethod**(): `string`

Get the HTTP method of the request.

Get the raw version by passing `{ raw: true }` in the options.

###### Returns

`string`

###### Call Signature

> **getMethod**(`options`: [`RawOption`](index.md#rawoption)): `Uint8Array`

Get the HTTP method of the request.

Get the raw version by passing `{ raw: true }` in the options.

###### Parameters

| Parameter | Type |
| ------ | ------ |
| `options` | [`RawOption`](index.md#rawoption) |

###### Returns

`Uint8Array`

##### getPath()

###### Call Signature

> **getPath**(): `string`

Get the path of the request.

Get the raw version by passing `{ raw: true }` in the options.

###### Returns

`string`

###### Call Signature

> **getPath**(`options`: [`RawOption`](index.md#rawoption)): `Uint8Array`

Get the path of the request.

Get the raw version by passing `{ raw: true }` in the options.

###### Parameters

| Parameter | Type |
| ------ | ------ |
| `options` | [`RawOption`](index.md#rawoption) |

###### Returns

`Uint8Array`

##### getPort()

> **getPort**(): `number`

Get the port of the request.

###### Returns

`number`

##### getQuery()

###### Call Signature

> **getQuery**(): `string`

Get the unparsed query of the request.

Get the raw version by passing `{ raw: true }` in the options.

Excludes the leading `?`.

###### Returns

`string`

###### Call Signature

> **getQuery**(`options`: [`RawOption`](index.md#rawoption)): `Uint8Array`

Get the unparsed query of the request.

Get the raw version by passing `{ raw: true }` in the options.

Excludes the leading `?`.

###### Parameters

| Parameter | Type |
| ------ | ------ |
| `options` | [`RawOption`](index.md#rawoption) |

###### Returns

`Uint8Array`

##### getRaw()

> **getRaw**(): [`RequestSpecRaw`](index.md#requestspecraw)

This methods converts the [RequestSpec](index.md#requestspec) to a [RequestSpecRaw](index.md#requestspecraw).

This is useful to retrieve the raw bytes of the request.

###### Returns

[`RequestSpecRaw`](index.md#requestspecraw)

###### Example

```js
const spec = new RequestSpec("https://example.com");
const specRaw = spec.getRaw();
const bytes = specRaw.getRaw(); // GET / HTTP/1.1\r\nHost: example.com\r\n\r\n
```

##### getTls()

> **getTls**(): `boolean`

Get if the request uses TLS (HTTPS).

###### Returns

`boolean`

##### removeHeader()

> **removeHeader**(`name`: `string`): `void`

Removes a header.

###### Parameters

| Parameter | Type |
| ------ | ------ |
| `name` | `string` |

###### Returns

`void`

##### setBody()

> **setBody**(`body`: [`Body`](index.md#body) \| [`Bytes`](index.md#bytes), `options`?: [`SetBodyOptions`](index.md#setbodyoptions)): `void`

Set the body of the request.

The body can either be a [Body](index.md#body) or any type that can be converted to [Bytes](index.md#bytes).

###### Parameters

| Parameter | Type |
| ------ | ------ |
| `body` | [`Body`](index.md#body) \| [`Bytes`](index.md#bytes) |
| `options`? | [`SetBodyOptions`](index.md#setbodyoptions) |

###### Returns

`void`

###### Example

```js
const body = new Body("Hello world.");
const options = { updateContentLength: true };
request.setBody(body, options);
```

##### setHeader()

> **setHeader**(`name`: `string`, `value`: `string`): `void`

Set a header value.

This will overwrite any existing values.

###### Parameters

| Parameter | Type |
| ------ | ------ |
| `name` | `string` |
| `value` | `string` |

###### Returns

`void`

##### setHost()

> **setHost**(`host`: `string`): `void`

Set the host of the request.

It will also update the `Host` header.

###### Parameters

| Parameter | Type |
| ------ | ------ |
| `host` | `string` |

###### Returns

`void`

##### setMethod()

> **setMethod**(`method`: [`Bytes`](index.md#bytes)): `void`

Set the HTTP method of the request.

All strings are accepted.

###### Parameters

| Parameter | Type |
| ------ | ------ |
| `method` | [`Bytes`](index.md#bytes) |

###### Returns

`void`

##### setPath()

> **setPath**(`path`: [`Bytes`](index.md#bytes)): `void`

Set the path of the request.

###### Parameters

| Parameter | Type |
| ------ | ------ |
| `path` | [`Bytes`](index.md#bytes) |

###### Returns

`void`

##### setPort()

> **setPort**(`port`: `number`): `void`

Set the port of the request.

The port number must be between 1 and 65535.

###### Parameters

| Parameter | Type |
| ------ | ------ |
| `port` | `number` |

###### Returns

`void`

##### setQuery()

> **setQuery**(`query`: [`Bytes`](index.md#bytes)): `void`

Set the unparsed query of the request.

The query string should not include the leading `?`.

###### Parameters

| Parameter | Type |
| ------ | ------ |
| `query` | [`Bytes`](index.md#bytes) |

###### Returns

`void`

###### Example

```js
spec.setQuery("q=hello");
```

##### setRaw()

> **setRaw**(`raw`: [`Bytes`](index.md#bytes)): [`RequestSpecRaw`](index.md#requestspecraw)

This method sets the raw [Bytes](index.md#bytes) of the request and converts it to a [RequestSpecRaw](index.md#requestspecraw).

This is useful when you have a prepared [RequestSpec](index.md#requestspec) and you just want to modify the raw data.

###### Parameters

| Parameter | Type |
| ------ | ------ |
| `raw` | [`Bytes`](index.md#bytes) |

###### Returns

[`RequestSpecRaw`](index.md#requestspecraw)

###### Example

```js
const rawBytes = []; // RAW BYTES HERE
const request = new RequestSpec("https://example.com");
const rawRequest = request.setRaw(rawBytes);
```

##### setTls()

> **setTls**(`tls`: `boolean`): `void`

Set if the request uses TLS (HTTPS).

###### Parameters

| Parameter | Type |
| ------ | ------ |
| `tls` | `boolean` |

###### Returns

`void`

##### parse()

###### Call Signature

> `static` **parse**(`bytes`: [`Bytes`](index.md#bytes)): [`RequestSpec`](index.md#requestspec)

Parses raw bytes into a [RequestSpec](index.md#requestspec).

###### Parameters

| Parameter | Type |
| ------ | ------ |
| `bytes` | [`Bytes`](index.md#bytes) |

###### Returns

[`RequestSpec`](index.md#requestspec)

###### Throws

If the bytes are not a valid HTTP request.

###### Example

```js
const rawInput = 'GET / HTTP/1.1\r\nHost: example.com\r\n\r\n';
const spec = RequestSpec.parse(rawInput);
spec.setHeader('x-caido', 'test');
const specRaw = spec.getRaw();
const rawOutput = specRaw.getRaw(); // Will contain the new header
```

###### Call Signature

> `static` **parse**(`raw`: [`RequestSpecRaw`](index.md#requestspecraw)): [`RequestSpec`](index.md#requestspec)

Parses the raw bytes of a [RequestSpecRaw](index.md#requestspecraw) into a [RequestSpec](index.md#requestspec).

###### Parameters

| Parameter | Type |
| ------ | ------ |
| `raw` | [`RequestSpecRaw`](index.md#requestspecraw) |

###### Returns

[`RequestSpec`](index.md#requestspec)

###### Throws

If the bytes are not a valid HTTP request.

***

### RequestSpecRaw

A mutable raw Request that has not yet been sent.

#### Constructors

##### new RequestSpecRaw()

> **new RequestSpecRaw**(`url`: `string`): [`RequestSpecRaw`](index.md#requestspecraw)

Build a new [RequestSpecRaw](index.md#requestspecraw) from a URL string. Only the host, port and scheme will be parsed.

You can convert a saved immutable [Request](index.md#request-1) object into a [RequestSpecRaw](index.md#requestspecraw) object by using the `toSpecRaw()` method.

You MUST use `setRaw` to set the raw bytes of the request.

###### Parameters

| Parameter | Type |
| ------ | ------ |
| `url` | `string` |

###### Returns

[`RequestSpecRaw`](index.md#requestspecraw)

###### Example

```js
const spec = new RequestSpecRaw("https://example.com");
```

#### Methods

##### getHost()

> **getHost**(): `string`

Get the host of the request.

###### Returns

`string`

##### getPort()

> **getPort**(): `number`

Get the port of the request.

###### Returns

`number`

##### getRaw()

> **getRaw**(): `Uint8Array`

Get the raw bytes of the request.

###### Returns

`Uint8Array`

##### getSpec()

> **getSpec**(): [`RequestSpec`](index.md#requestspec)

This methods converts the [RequestSpecRaw](index.md#requestspecraw) to a [RequestSpec](index.md#requestspec).

###### Returns

[`RequestSpec`](index.md#requestspec)

###### Throws

If the bytes are not a valid HTTP request.

###### See

[RequestSpec.parse](index.md#parse)

##### getTls()

> **getTls**(): `boolean`

Get if the request uses TLS (HTTPS).

###### Returns

`boolean`

##### setHost()

> **setHost**(`host`: `string`): `void`

Set the host of the request.

It will NOT update the `Host` header.

###### Parameters

| Parameter | Type |
| ------ | ------ |
| `host` | `string` |

###### Returns

`void`

##### setPort()

> **setPort**(`port`: `number`): `void`

Set the port of the request.

The port number must be between 1 and 65535.

###### Parameters

| Parameter | Type |
| ------ | ------ |
| `port` | `number` |

###### Returns

`void`

##### setRaw()

> **setRaw**(`raw`: [`Bytes`](index.md#bytes)): `void`

Set the raw [Bytes](index.md#bytes) of the request.

###### Parameters

| Parameter | Type |
| ------ | ------ |
| `raw` | [`Bytes`](index.md#bytes) |

###### Returns

`void`

##### setTls()

> **setTls**(`tls`: `boolean`): `void`

Set if the request uses TLS (HTTPS).

###### Parameters

| Parameter | Type |
| ------ | ------ |
| `tls` | `boolean` |

###### Returns

`void`

***

### Request

> **Request**: `object`

An immutable saved Request.

To modify, use `toSpec` to get a `RequestSpec` object.

#### Type declaration

##### getBody()

The body of the request.

###### Returns

`undefined` \| [`Body`](index.md#body)

##### getCreatedAt()

The datetime the request was recorded by the proxy.

###### Returns

`Date`

##### getHeader()

Get a header value.

Header name is case-insensitive.
The header might have multiple values.

###### Parameters

| Parameter | Type |
| ------ | ------ |
| `name` | `string` |

###### Returns

`undefined` \| `string`[]

##### getHeaders()

The headers of the request.

Header names are case-insensitive.
Each header might have multiple values.

###### Returns

`Record`\<`string`, `string`[]\>

###### Example

```json
{
  "Host": ["caido.io"],
  "Connection": ["keep-alive"],
  "Content-Length": ["95"]
}
```

##### getHost()

The target host of the request.

###### Returns

`string`

##### getId()

The unique Caido [ID](index.md#id) of the request.

###### Returns

[`ID`](index.md#id)

##### getMethod()

The HTTP method of the request.

###### Returns

`string`

##### getPath()

The path of the request.

###### Returns

`string`

##### getPort()

The target port of the request.

###### Returns

`number`

##### getQuery()

The unparsed query of the request.

Excludes the leading `?`.

###### Returns

`string`

##### getRaw()

The raw version of the request.

Used to access the bytes directly.

###### Returns

[`RequestRaw`](index.md#requestraw)

##### getTls()

If the request uses TLS (HTTPS).

###### Returns

`boolean`

##### getUrl()

The full URL of the request.

###### Returns

`string`

##### toSpec()

Copied the request to a mutable un-saved [RequestSpec](index.md#requestspec).
This enables you to make modify a request before re-sending it.

###### Returns

[`RequestSpec`](index.md#requestspec)

##### toSpecRaw()

Copied the request to a mutable un-saved [RequestSpecRaw](index.md#requestspecraw).
The raw requests are not parsed and can be used to send invalid HTTP Requests.

###### Returns

[`RequestSpecRaw`](index.md#requestspecraw)

***

### RequestOrderField

> **RequestOrderField**: `"ext"` \| `"host"` \| `"id"` \| `"method"` \| `"path"` \| `"query"` \| `"created_at"` \| `"source"`

Field to order requests by.

***

### RequestRaw

> **RequestRaw**: `object`

An immutable saved raw Request.

#### Type declaration

##### toBytes()

Get the raw request as an array of bytes.

###### Returns

`Uint8Array`

##### toText()

Parse the raw request as a string.

Unprintable characters will be replaced with `�`.

###### Returns

`string`

***

### RequestResponse

> **RequestResponse**: `object`

An immutable saved Request and Response pair.

#### Type declaration

##### request

> **request**: [`Request`](index.md#request-1)

##### response

> **response**: [`Response`](index.md#response-4)

***

### RequestResponseOpt

> **RequestResponseOpt**: `object`

An immutable saved Request and optional Response pair.

#### Type declaration

##### request

> **request**: [`Request`](index.md#request-1)

##### response?

> `optional` **response**: [`Response`](index.md#response-4)

***

### RequestsConnection

> **RequestsConnection**: `object`

A connection of requests.

#### Type declaration

##### items

> **items**: [`RequestsConnectionItem`](index.md#requestsconnectionitem)[]

##### pageInfo

> **pageInfo**: [`PageInfo`](index.md#pageinfo)

***

### RequestsConnectionItem

> **RequestsConnectionItem**: `object`

An item in a connection of requests.

#### Type declaration

##### cursor

> **cursor**: [`Cursor`](index.md#cursor)

##### request

> **request**: [`Request`](index.md#request-1)

##### response?

> `optional` **response**: [`Response`](index.md#response-4)

***

### RequestSendTimeouts

> **RequestSendTimeouts**: `object`

Timeouts for sending a request and receiving a response.

#### Type declaration

##### connect?

> `optional` **connect**: `number`

The timeout to open the TCP connection to the target host
and perform the TLS handshake.

Defaults to 30s.

##### extra?

> `optional` **extra**: `number`

The timeout to read data after we have a read the full response.

This is useful if you believe the server will send more data
than implied by the Content-Length header.

Defaults to 0s (no timeout).

##### global?

> `optional` **global**: `number`

The global timeout for sending a request and receiving a response.

No default value.

##### partial?

> `optional` **partial**: `number`

The timeout between each read attempt for the response.
On a slow connection, this is important to increase.

Defaults to 5s.

##### response?

> `optional` **response**: `number`

The timeout to receive the first byte of the response.

After the first byte is received, the partial timeout will be used.

Defaults to 30s.

***

### RequestsQuery

> **RequestsQuery**: `object`

Query builder to fetch requests.

#### Type declaration

##### after()

Requests after a given cursor.

###### Parameters

| Parameter | Type | Description |
| ------ | ------ | ------ |
| `cursor` | [`Cursor`](index.md#cursor) | [Cursor](index.md#cursor) of the request |

###### Returns

[`RequestsQuery`](index.md#requestsquery)

##### ascending()

###### Call Signature

Ascending ordering.

###### Parameters

| Parameter | Type | Description |
| ------ | ------ | ------ |
| `target` | `"req"` | Target of the ordering: req or resp. |
| `field` | [`RequestOrderField`](index.md#requestorderfield) | Field to order by. |

###### Returns

[`RequestsQuery`](index.md#requestsquery)

###### Call Signature

###### Parameters

| Parameter | Type |
| ------ | ------ |
| `target` | `"resp"` |
| `field` | [`ResponseOrderField`](index.md#responseorderfield) |

###### Returns

[`RequestsQuery`](index.md#requestsquery)

##### before()

Requests before a given cursor.

###### Parameters

| Parameter | Type | Description |
| ------ | ------ | ------ |
| `cursor` | [`Cursor`](index.md#cursor) | [Cursor](index.md#cursor) of the request |

###### Returns

[`RequestsQuery`](index.md#requestsquery)

##### descending()

###### Call Signature

Descending ordering.

###### Parameters

| Parameter | Type | Description |
| ------ | ------ | ------ |
| `target` | `"req"` | Target of the ordering: req or resp. |
| `field` | [`RequestOrderField`](index.md#requestorderfield) | Field to order by. |

###### Returns

[`RequestsQuery`](index.md#requestsquery)

###### Call Signature

###### Parameters

| Parameter | Type |
| ------ | ------ |
| `target` | `"resp"` |
| `field` | [`ResponseOrderField`](index.md#responseorderfield) |

###### Returns

[`RequestsQuery`](index.md#requestsquery)

##### execute()

Execute the query.

###### Returns

`Promise`\<[`RequestsConnection`](index.md#requestsconnection)\>

###### Throws

If a query parameter is invalid or the query cannot be executed.

##### filter()

Filter requests.

###### Parameters

| Parameter | Type | Description |
| ------ | ------ | ------ |
| `filter` | `string` | HTTPQL filter |

###### Returns

[`RequestsQuery`](index.md#requestsquery)

##### first()

First n requests.

###### Parameters

| Parameter | Type | Description |
| ------ | ------ | ------ |
| `n` | `number` | Number of requests to return |

###### Returns

[`RequestsQuery`](index.md#requestsquery)

##### last()

Last n requests.

###### Parameters

| Parameter | Type | Description |
| ------ | ------ | ------ |
| `n` | `number` | Number of requests to return |

###### Returns

[`RequestsQuery`](index.md#requestsquery)

***

### RequestsSDK

> **RequestsSDK**: `object`

The SDK for the Requests service.

#### Type declaration

##### get()

Get a request by its unique [ID](index.md#id).

###### Parameters

| Parameter | Type |
| ------ | ------ |
| `id` | [`ID`](index.md#id) |

###### Returns

`Promise`\<`undefined` \| [`RequestResponseOpt`](index.md#requestresponseopt)\>

###### Example

```js
await sdk.requests.get("1");
```

##### inScope()

Checks if a request is in scope.

###### Parameters

| Parameter | Type |
| ------ | ------ |
| `request` | [`Request`](index.md#request-1) \| [`RequestSpec`](index.md#requestspec) |

###### Returns

`boolean`

###### Example

```js
if (sdk.requests.inScope(request)) {
 sdk.console.log("In scope");
}
```

##### matches()

Checks if a request/response matches an HTTPQL filter.

###### Parameters

| Parameter | Type | Description |
| ------ | ------ | ------ |
| `filter` | `string` | HTTPQL filter |
| `request` | [`Request`](index.md#request-1) | The [Request](index.md#request-1) to match against |
| `response`? | [`Response`](index.md#response-4) | The [Response](index.md#response-4) to match against |

###### Returns

`boolean`

##### query()

Query requests of the current project.

###### Returns

[`RequestsQuery`](index.md#requestsquery)

###### Example

```js
const page = await sqk.requests.query().first(2).execute();
sdk.console.log(`ID: ${page.items[1].request.getId()}`);
```

##### send()

Sends an HTTP request, either a [RequestSpec](index.md#requestspec) or [RequestSpecRaw](index.md#requestspecraw).

This respects the upstream proxy settings.

###### Parameters

| Parameter | Type |
| ------ | ------ |
| `request` | [`RequestSpec`](index.md#requestspec) \| [`RequestSpecRaw`](index.md#requestspecraw) |
| `options`? | [`RequestSendOptions`](index.md#requestsendoptions) |

###### Returns

`Promise`\<[`RequestResponse`](index.md#requestresponse)\>

###### Throws

If the request cannot be sent.
If the request times out, the error message will contain the word "Timeout".

###### Example

```js
const spec = new RequestSpec("https://example.com");
try {
  const res = await sdk.requests.send(request)
  sdk.console.log(res.request.getId());
  sdk.console.log(res.response.getCode());
} catch (err) {
  sdk.console.error(err);
}
```

***

### Response

> **Response**: `object`

An immutable saved Response.

#### Type declaration

##### getBody()

The body of the response

###### Returns

`undefined` \| [`Body`](index.md#body)

##### getCode()

The status code of the response.

###### Returns

`number`

##### getCreatedAt()

The datetime the response was recorded by the proxy.

###### Returns

`Date`

##### getHeader()

Get a header value.

Header name is case-insensitive.
The header might have multiple values.

###### Parameters

| Parameter | Type |
| ------ | ------ |
| `name` | `string` |

###### Returns

`undefined` \| `string`[]

##### getHeaders()

The headers of the response.

Header names are case-insensitive.
Each header might have multiple values.

###### Returns

`Record`\<`string`, `string`[]\>

###### Example

```json
{
  "Date": ["Sun, 26 May 2024 10:59:21 GMT"],
  "Content-Type": ["text/html"]
}
```

##### getId()

The unique Caido [ID](index.md#id) of the response.

###### Returns

[`ID`](index.md#id)

##### getRaw()

The raw version of the response.

Used to access the bytes directly.

###### Returns

[`ResponseRaw`](index.md#responseraw)

##### getRoundtripTime()

The time it took to send the request and receive the response in milliseconds.

###### Returns

`number`

***

### ResponseOrderField

> **ResponseOrderField**: `"length"` \| `"roundtrip"` \| `"code"`

Field to order responses by.

***

### ResponseRaw

> **ResponseRaw**: `object`

An immutable saved raw Response.

#### Type declaration

##### toBytes()

Get the raw response as an array of bytes.

###### Returns

`Uint8Array`

##### toText()

Parse the raw response as a string.

Unprintable characters will be replaced with `�`.

###### Returns

`string`

***

### SetBodyOptions

> **SetBodyOptions**: `object`

Options when setting the body of a Request.

#### Type declaration

##### updateContentLength

> **updateContentLength**: `boolean`

Should update the Content-export type header.

###### Default

```ts
true
```

## Findings

### DedupeKey

> **DedupeKey**: `string` & `object`

A deduplication key.

#### Type declaration

##### \_\_dedupeKey?

> `optional` **\_\_dedupeKey**: `never`

***

### Finding

> **Finding**: `object`

A saved immutable Finding.

#### Type declaration

##### getDedupeKey()

The deduplication key of the finding.

###### Returns

`undefined` \| [`DedupeKey`](index.md#dedupekey)

##### getDescription()

The description of the finding.

###### Returns

`undefined` \| `string`

##### getId()

The unique Caido [ID](index.md#id) of the finding.

###### Returns

[`ID`](index.md#id)

##### getReporter()

The name of the reporter.

###### Returns

`string`

##### getRequestId()

The ID of the associated [Request](index.md#request-1).

###### Returns

`string`

##### getTitle()

The title of the finding.

###### Returns

`string`

***

### FindingSpec

> **FindingSpec**: `object`

A mutable Finding not yet created.

#### Type declaration

##### dedupeKey?

> `optional` **dedupeKey**: [`DedupeKey`](index.md#dedupekey)

Deduplication key for findings.
If a finding with the same dedupe key already exists, it will not be created.

##### description?

> `optional` **description**: `string`

The description of the finding.

##### reporter

> **reporter**: `string`

The name of the reporter.
It will be used to group findings.

##### request

> **request**: [`Request`](index.md#request-1)

The associated [Request](index.md#request-1).

##### title

> **title**: `string`

The title of the finding.

***

### FindingsSDK

> **FindingsSDK**: `object`

The SDK for the Findings service.

#### Type declaration

##### create()

Creates a new Finding.

###### Parameters

| Parameter | Type |
| ------ | ------ |
| `spec` | [`FindingSpec`](index.md#findingspec) |

###### Returns

`Promise`\<[`Finding`](index.md#finding)\>

###### Throws

If the request cannot be saved.

###### Example

```js
await sdk.findings.create({
  title: "Title",
  description: "Description",
  reporter: "Reporter",
  dedupeKey: `${request.getHost()}-${request.getPath()}`,
  request,
});
```

##### exists()

Check if a [Finding](index.md#finding) exists.
Similar to `get`, but returns a boolean.

###### Parameters

| Parameter | Type |
| ------ | ------ |
| `input` | [`GetFindingInput`](index.md#getfindinginput) |

###### Returns

`Promise`\<`boolean`\>

###### Example

```js
await sdk.findings.exists("my-dedupe-key");
```

##### get()

Try to get a [Finding](index.md#finding) for a request.

Since a request can have multiple findings, this will return the first one found.
You can also filter by reporter to get a specific finding.

Finally, you can use a deduplication key to get a specific finding.

###### Parameters

| Parameter | Type |
| ------ | ------ |
| `input` | [`GetFindingInput`](index.md#getfindinginput) |

###### Returns

`Promise`\<`undefined` \| [`Finding`](index.md#finding)\>

###### Example

```js
await sdk.findings.get({
 reporter: "Reporter",
 request,
});
```

***

### GetFindingInput

> **GetFindingInput**: [`DedupeKey`](index.md#dedupekey) \| \{ `reporter`: `string`; `request`: [`Request`](index.md#request-1); \}

Input to get a [Finding](index.md#finding).

#### Type declaration

[`DedupeKey`](index.md#dedupekey)

\{ `reporter`: `string`; `request`: [`Request`](index.md#request-1); \}

##### reporter?

> `optional` **reporter**: `string`

The name of the reporter.

##### request

> **request**: [`Request`](index.md#request-1)

The associated [Request](index.md#request-1).

## Replay

### ReplayCollection

> **ReplayCollection**: `object`

A collection of replay sessions.

#### Type declaration

##### getId()

The unique Caido [ID](index.md#id) of the replay collection.

###### Returns

[`ID`](index.md#id)

##### getName()

The name of the replay collection.

###### Returns

`string`

***

### ReplaySDK

> **ReplaySDK**: `object`

The SDK for the Replay service.

#### Type declaration

##### createSession()

###### Parameters

| Parameter | Type |
| ------ | ------ |
| `source`? | [`RequestSource`](index.md#requestsource) |
| `collection`? | [`ID`](index.md#id) \| [`ReplayCollection`](index.md#replaycollection) |

###### Returns

`Promise`\<[`ReplaySession`](index.md#replaysession)\>

##### getCollections()

###### Returns

`Promise`\<[`ReplayCollection`](index.md#replaycollection)[]\>

***

### ReplaySession

> **ReplaySession**: `object`

A replay session.

#### Type declaration

##### getId()

The unique Caido [ID](index.md#id) of the replay session.

###### Returns

[`ID`](index.md#id)

##### getName()

The name of the replay session.

###### Returns

`string`

## Projects

### Project

> **Project**: `object`

A saved immutable Project.

#### Type declaration

##### getId()

The unique Caido [ID](index.md#id) of the project.

###### Returns

[`ID`](index.md#id)

##### getName()

The name of the project.

###### Returns

`string`

##### getPath()

The directory where the project is located.

###### Returns

`string`

##### getStatus()

The status of the project.

###### Returns

[`ProjectStatus`](index.md#projectstatus)

##### getVersion()

The version of the project.
The format is `MAJOR.MINOR.PATCH`.

###### Returns

`string`

***

### ProjectsSDK

> **ProjectsSDK**: `object`

The SDK for the Projects service.

#### Type declaration

##### getCurrent()

Get the currently selected [Project](index.md#project) if any.

###### Returns

`Promise`\<`undefined` \| [`Project`](index.md#project)\>

###### Example

```js
await sdk.projects.getCurrent();
```

***

### ProjectStatus

> **ProjectStatus**: `"ready"` \| `"restoring"` \| `"error"`

A [Project](index.md#project) status.

## Shared

### Bytes

> **Bytes**: `string` \| `number`[] \| `Uint8Array`

Types that can be converted to bytes in inputs.

***

### Cursor

> **Cursor**: `string` & `object`

A cursor for pagination.

#### Type declaration

##### \_\_cursor?

> `optional` **\_\_cursor**: `never`

***

### DefineAPI\<API\>

> **DefineAPI**\<`API`\>: `{ [K in keyof API]: DefineAPICallback<API[K]> }`

Define a Plugin backend functions that are callable from the frontend.

#### Type Parameters

| Type Parameter |
| ------ |
| `API` *extends* `Record`\<`string`, (...`args`: `any`[]) => [`MaybePromise`](index.md#maybepromiset)\<`any`\>\> |

#### Example

```typescript
function generateNumber(sdk: SDK, min: number, max: number): number {
  return Math.floor(Math.random() * (max - min + 1) + min);
}

export type API = DefineAPI<{
  generateNumber: typeof generateNumber;
}>;

export function init(sdk: SDK<API>) {
  sdk.api.register("generateNumber", generateNumber);
}
```

***

### DefineAPICallback\<F\>

> **DefineAPICallback**\<`F`\>: `F` *extends* (`sdk`: [`SDK`](index.md#sdkapi-events), ...`args`: infer A) => infer R ? (...`args`: `A`) => `R` : `"Your callback must respect the format (sdk: SDK, ...args: unknown[]) => MaybePromise<unknown>"`

Parser for Plugin backend callable functions

#### Type Parameters

| Type Parameter |
| ------ |
| `F` |

***

### DefineEventCallback\<F\>

> **DefineEventCallback**\<`F`\>: `F` *extends* (...`args`: infer A) => [`MaybePromise`](index.md#maybepromiset)\<`void`\> ? (...`args`: `A`) => [`MaybePromise`](index.md#maybepromiset)\<`void`\> : `"Your callback must respect the format (...args: unknown[]) => MaybePromise<void>"`

Parser for Plugin backend events callbacks.

#### Type Parameters

| Type Parameter |
| ------ |
| `F` |

***

### DefineEvents\<Events\>

> **DefineEvents**\<`Events`\>: `{ [K in keyof Events]: DefineEventCallback<Events[K]> }`

Define a Plugin backend events that the frontend can receive.

#### Type Parameters

| Type Parameter |
| ------ |
| `Events` *extends* `Record`\<`string`, (...`args`: `any`[]) => [`MaybePromise`](index.md#maybepromiset)\<`void`\>\> |

#### Example

```typescript
type MyEventData = { id: string; name: string };

export type BackendEvents = DefineEvents<{
  "myevent": (data: MyEventData) => void;
}>;

export function init(sdk: SDK<{}, BackendEvents>) {
  sdk.api.send("myevent", { id: "1", name: "hello" });
}
```

***

### ID

> **ID**: `string` & `object`

A unique identifier.

#### Type declaration

##### \_\_id?

> `optional` **\_\_id**: `never`

***

### MaybePromise\<T\>

> **MaybePromise**\<`T`\>: `T` \| `Promise`\<`T`\>

Promise or value.

#### Type Parameters

| Type Parameter |
| ------ |
| `T` |

***

### MaybePromise\<T\>

> **MaybePromise**\<`T`\>: `T` \| `Promise`\<`T`\>

Promise or value.

#### Type Parameters

| Type Parameter |
| ------ |
| `T` |

***

### RawOption

> **RawOption**: `object`

Option to return raw value

#### Type declaration

##### raw

> **raw**: `true`

***

### RequestSource

> **RequestSource**: [`ID`](index.md#id) \| [`Request`](index.md#request-1) \| [`RequestSpec`](index.md#requestspec) \| [`RequestSpecRaw`](index.md#requestspecraw)

The source of a request.

## Environment

### EnvironmentSDK

> **EnvironmentSDK**: `object`

The SDK for the Environment service.

#### Type declaration

##### getVar()

Get the value of an environment variable.

###### Parameters

| Parameter | Type | Description |
| ------ | ------ | ------ |
| `name` | `string` | The name of the environment variable. |

###### Returns

`undefined` \| `string`

The value of the environment variable.

##### getVars()

Get all the environment variables.
It includes the global environment and the selected environment.
Those variables can change over time so avoid caching them.

###### Returns

[`EnvironmentVariable`](index.md#environmentvariable)[]

An array of [EnvironmentVariable](index.md#environmentvariable)

##### setVar()

Sets an environment variable to a given value.
This will override any existing value.
The environment variable can be set either on the currently
selected environment or the global environment.

###### Parameters

| Parameter | Type |
| ------ | ------ |
| `input` | [`SetVarInput`](index.md#setvarinput) |

###### Returns

`Promise`\<`void`\>

###### Throws

If trying to set when a project is not selected.

###### Throws

If trying to set when an environment is not selected (with `global: false`).

###### Example

```js
await sdk.env.setVar({
  name: "USER_SECRET",
  value: "my secret value",
  secret: true,
  global: false
});
```

***

### EnvironmentVariable

> **EnvironmentVariable**: `object`

A saved immutable Finding.

#### Type declaration

##### isSecret

> `readonly` **isSecret**: `boolean`

If the environment variable is a secret

##### name

> `readonly` **name**: `string`

The name of the environment variable

##### value

> `readonly` **value**: `string`

The value of the environment variable

***

### SetVarInput

> **SetVarInput**: `object`

Input for the `setVar` of [EnvironmentSDK](index.md#environmentsdk).

#### Type declaration

##### env?

> `optional` **env**: `string`

The `name` of the Environment to set the variable on.
This will take precedence over the `global` flag if provided.

##### global

> **global**: `boolean`

If the environment variable should be set on the global
environment or the currently selected environment.
By default, it will be set globally.

###### Default

```ts
true
```

##### name

> **name**: `string`

Name of the environment variable

##### secret

> **secret**: `boolean`

If the environment variable should be treated as secret.
Secrets are encrypted on the disk.

###### Default

```ts
false
```

##### value

> **value**: `string`

Value of the environment variable

## GraphQL

### GraphQLSDK

> **GraphQLSDK**: `object`

The SDK for the GraphQL service.

#### Type declaration

##### execute()

Executes a GraphQL query.

###### Type Parameters

| Type Parameter |
| ------ |
| `T` |

###### Parameters

| Parameter | Type |
| ------ | ------ |
| `query` | `string` |
| `variables`? | `Record`\<`string`, `any`\> |

###### Returns

`Promise`\<[`GraphQLResponse`](index.md#graphqlresponset)\<`T`\>\>

###### Example

```js
await sdk.graphql.execute(`
  query {
    viewer
  }
`);
```

## Other

### Database

A SQLite database.

The implementation uses a connection pool and is fully asynchronous.
Each connection will be spawned in a worker thread.

#### Example

```ts
const db = await open({ filename: "path/to/database.sqlite" });
await db.exec("CREATE TABLE test (id INTEGER PRIMARY KEY, name TEXT);");
await db.exec("INSERT INTO test (name) VALUES ('foo');");
```

#### Constructors

##### new Database()

> **new Database**(): [`Database`](index.md#database)

###### Returns

[`Database`](index.md#database)

#### Methods

##### exec()

> **exec**(`sql`: `string`): `Promise`\<`void`\>

This method allows one or more SQL statements to be executed without returning any results.

###### Parameters

| Parameter | Type |
| ------ | ------ |
| `sql` | `string` |

###### Returns

`Promise`\<`void`\>

##### prepare()

> **prepare**(`sql`: `string`): `Promise`\<[`Statement`](index.md#statement)\>

Compiles a SQL statement into a [prepared statement](https://www.sqlite.org/c3ref/stmt.html).

###### Parameters

| Parameter | Type |
| ------ | ------ |
| `sql` | `string` |

###### Returns

`Promise`\<[`Statement`](index.md#statement)\>

***

### Statement

This class represents a single prepared statement. This class cannot be instantiated via its constructor.
Instead, instances are created via the database.prepare() method.

#### Constructors

##### new Statement()

> **new Statement**(): [`Statement`](index.md#statement)

###### Returns

[`Statement`](index.md#statement)

#### Methods

##### all()

> **all**\<`T`\>(...`params`: [`Parameter`](index.md#parameter)[]): `Promise`\<`T`[]\>

This method executes a prepared statement and returns all results as an array of objects.
If the prepared statement does not return any results, this method returns an empty array.
The prepared statement [parameters are bound](https://www.sqlite.org/c3ref/bind_blob.html) using the values in `params`.

###### Type Parameters

| Type Parameter | Default type |
| ------ | ------ |
| `T` *extends* `object` | `object` |

###### Parameters

| Parameter | Type | Description |
| ------ | ------ | ------ |
| ...`params` | [`Parameter`](index.md#parameter)[] | The values to bind to the prepared statement. Named parameters are not supported. |

###### Returns

`Promise`\<`T`[]\>

##### get()

> **get**\<`T`\>(...`params`: [`Parameter`](index.md#parameter)[]): `Promise`\<`undefined` \| `T`\>

This method executes a prepared statement and returns the first result as an object.
If the prepared statement does not return any results, this method returns undefined.
The prepared statement [parameters are bound](https://www.sqlite.org/c3ref/bind_blob.html) using the values in params.

###### Type Parameters

| Type Parameter | Default type |
| ------ | ------ |
| `T` *extends* `object` | `object` |

###### Parameters

| Parameter | Type | Description |
| ------ | ------ | ------ |
| ...`params` | [`Parameter`](index.md#parameter)[] | The values to bind to the prepared statement. Named parameters are not supported. |

###### Returns

`Promise`\<`undefined` \| `T`\>

##### run()

> **run**(...`params`: [`Parameter`](index.md#parameter)[]): `Promise`\<[`Result`](index.md#result)\>

This method executes a prepared statement and returns an object summarizing the resulting changes.
The prepared statement [parameters are bound](https://www.sqlite.org/c3ref/bind_blob.html) using the values in params.

###### Parameters

| Parameter | Type | Description |
| ------ | ------ | ------ |
| ...`params` | [`Parameter`](index.md#parameter)[] | The values to bind to the prepared statement. Named parameters are not supported. |

###### Returns

`Promise`\<[`Result`](index.md#result)\>

***

### Console

> **Console**: `object`

Console interface for logging.

Currently logs are only available in the backend logs.
See the [documentation](https://docs.caido.io/report_bug.html#1-backend-logs) on how to retrieve them.

#### Type declaration

##### debug()

Log a message with the debug level.

Usually used for troubleshooting purposes.

###### Parameters

| Parameter | Type |
| ------ | ------ |
| `message` | `any` |

###### Returns

`void`

##### error()

Log a message with the error level.

Usually used for critical errors.

###### Parameters

| Parameter | Type |
| ------ | ------ |
| `message` | `any` |

###### Returns

`void`

##### log()

Log a message with the info level.

Usually used for general information.

###### Parameters

| Parameter | Type |
| ------ | ------ |
| `message` | `any` |

###### Returns

`void`

##### warn()

Log a message with the warn level.

Usually used for unexpected behaviors.

###### Parameters

| Parameter | Type |
| ------ | ------ |
| `message` | `any` |

###### Returns

`void`

***

### GraphQLError

> **GraphQLError**: `object`

#### Type declaration

##### extensions

> **extensions**: `Record`\<`string`, `any`\>

##### locations

> **locations**: [`GraphQLLocation`](index.md#graphqllocation)[]

##### message

> **message**: `string`

##### path

> **path**: [`GraphQLPathSegment`](index.md#graphqlpathsegment)[]

***

### GraphQLLocation

> **GraphQLLocation**: `object`

#### Type declaration

##### column

> **column**: `number`

##### line

> **line**: `number`

***

### GraphQLPathSegment

> **GraphQLPathSegment**: `string` \| `number`

***

### GraphQLResponse\<T\>

> **GraphQLResponse**\<`T`\>: `object`

#### Type Parameters

| Type Parameter |
| ------ |
| `T` |

#### Type declaration

##### data?

> `optional` **data**: `T`

##### errors?

> `optional` **errors**: [`GraphQLError`](index.md#graphqlerror)[]

***

### PageInfo

> **PageInfo**: `object`

Information on the current page of paginated data.

#### Type declaration

##### endCursor

> **endCursor**: [`Cursor`](index.md#cursor)

##### hasNextPage

> **hasNextPage**: `boolean`

##### hasPreviousPage

> **hasPreviousPage**: `boolean`

##### startCursor

> **startCursor**: [`Cursor`](index.md#cursor)

***

### Parameter

> **Parameter**: `null` \| `number` \| `bigint` \| `string` \| `Uint8Array`

***

### RequestSendOptions

> **RequestSendOptions**: `object`

#### Type declaration

##### save?

> `optional` **save**: `boolean`

If true, the request and response will be saved to the database
and the user will see them in the Search tab.

If you do not save, the request and response IDs will be set to 0.

###### Default

```ts
true
```

##### timeouts?

> `optional` **timeouts**: [`RequestSendTimeouts`](index.md#requestsendtimeouts) \| `number`

The timeouts to use for sending a request and receiving a response.

If a number is provided, it will be used as the global timeout and
the other timeouts will be set to infinity.

See the [RequestSendTimeouts](index.md#requestsendtimeouts) for the default values.

***

### Result

> **Result**: `object`

#### Type declaration

##### changes

> **changes**: `number`

##### lastInsertRowid

> **lastInsertRowid**: `number`

## Runtime

### RuntimeSDK

> **RuntimeSDK**: `object`

The SDK for the runtime information.

#### Type declaration

##### version

###### Get Signature

> **get** **version**(): `string`

Get the current version of Caido.

###### Returns

`string`

## Scope

### Scope

> **Scope**: `object`

A saved immutable Scope.

#### Type declaration

##### allowlist

> `readonly` **allowlist**: `string`[]

The allowlist of the scope.

##### denylist

> `readonly` **denylist**: `string`[]

The denylist of the scope.

##### id

> `readonly` **id**: [`ID`](index.md#id)

The unique Caido [ID](index.md#id) of the scope.

##### name

> `readonly` **name**: `string`

The name of the scope.

***

### ScopeSDK

> **ScopeSDK**: `object`

The SDK for the Scope service.

#### Type declaration

##### getAll()

Get all the scopes.

###### Returns

`Promise`\<[`Scope`](index.md#scope-1)[]\>

An array of [Scope](index.md#scope-1)



================================================
FILE: src/reference/sdks/frontend/index.md
================================================
# @caido/sdk-frontend

This is the reference for the frontend SDK used by frontend plugins.
[Caido](#caido-t-e) is the main interface that provides access to various services and functionalities.

## SDK

### Caido\<T, E\>

> **Caido**\<`T`, `E`\>: `object`

Utilities for frontend plugins.

#### Type Parameters

| Type Parameter | Default type |
| ------ | ------ |
| `T` *extends* [`BackendEndpoints`](index.md#backendendpoints) | `Record`\<`string`, `never`\> |
| `E` *extends* [`BackendEvents`](index.md#backendevents) | `Record`\<`string`, `never`\> |

#### Type declaration

##### ai

> **ai**: [`AiSDK`](index.md#aisdk)

Utilities to interact with AI.

##### assets

> **assets**: [`AssetsSDK`](index.md#assetssdk)

Utilities to interact with the plugin's static assets.

##### automate

> **automate**: [`AutomateSDK`](index.md#automatesdk)

Utilities to interact with the Automate page.

##### backend

> **backend**: [`BackendSDK`](index.md#backendsdkt-e)\<`T`, `E`\>

Utilities to interact with the backend plugin.

##### commandPalette

> **commandPalette**: [`CommandPaletteSDK`](index.md#commandpalettesdk)

Utilities to interact with the command palette.

##### commands

> **commands**: [`CommandsSDK`](index.md#commandssdk)

Utilities to interact with commands

##### env

> **env**: [`EnvironmentSDK`](index.md#environmentsdk)

Utilities to interact with the environment.

##### files

> **files**: [`FilesSDK`](index.md#filessdk)

Utilities to interact with the Files page.

##### filters

> **filters**: [`FiltersSDK`](index.md#filterssdk)

Utilities to interact with Filters page.

##### findings

> **findings**: [`FindingsSDK`](index.md#findingssdk)

Utilities to interact with findings

##### footer

> **footer**: [`FooterSDK`](index.md#footersdk)

Utilities to interact with the footer.

##### graphql

> **graphql**: `GraphqlSDK`

Utilities to interact with the GraphQL API.

##### httpHistory

> **httpHistory**: [`HTTPHistorySDK`](index.md#httphistorysdk)

Utilities to interact with the HTTP History page.

##### intercept

> **intercept**: [`InterceptSDK`](index.md#interceptsdk)

Utilities to interact with the Intercept page.

##### log

> **log**: [`LogSDK`](index.md#logsdk)

Utilities for logging messages to the console.

##### matchReplace

> **matchReplace**: [`MatchReplaceSDK`](index.md#matchreplacesdk)

Utilities to interact with Match and Replace page.

##### menu

> **menu**: [`MenuSDK`](index.md#menusdk)

Utilities to insert menu items and context-menus throughout the UI.

##### navigation

> **navigation**: [`NavigationSDK`](index.md#navigationsdk)

Utilities to interact with navigation.

##### projects

> **projects**: [`ProjectsSDK`](index.md#projectssdk)

Utilities to interact with projects.

##### replay

> **replay**: [`ReplaySDK`](index.md#replaysdk)

Utilities to interact with the Replay page.

##### runtime

> **runtime**: [`RuntimeSDK`](index.md#runtimesdk)

Utilities to interact with the runtime.

##### scopes

> **scopes**: [`ScopesSDK`](index.md#scopessdk)

Utilities to interact with scopes

##### search

> **search**: [`SearchSDK`](index.md#searchsdk)

Utilities to interact with the Search page.

##### shortcuts

> **shortcuts**: [`ShortcutsSDK`](index.md#shortcutssdk)

Utilities to interact with shortcuts.

##### sidebar

> **sidebar**: [`SidebarSDK`](index.md#sidebarsdk)

Utilities to interact with the sidebar.

##### sitemap

> **sitemap**: [`SitemapSDK`](index.md#sitemapsdk)

Utilities to interact with the Sitemap page.

##### storage

> **storage**: [`StorageSDK`](index.md#storagesdk)

Utilities to interact with frontend-plugin storage.

##### ui

> **ui**: [`UISDK`](index.md#uisdk)

Utilities to create UI components.

##### window

> **window**: [`WindowSDK`](index.md#windowsdk)

Utilities to interact with the active page.

##### workflows

> **workflows**: [`WorkflowSDK`](index.md#workflowsdk)

Utilities to interact with workflows.

## Backend

### BackendEndpoints

> **BackendEndpoints**: `object`

Endpoints provided by the backend plugin.

#### Index Signature

\[`key`: `string`\]: (...`args`: `any`[]) => `any`

***

### BackendEvents

> **BackendEvents**: `object`

Events emitted by the backend plugin.

#### Index Signature

\[`key`: `string`\]: (...`args`: `any`[]) => `void`

***

### BackendSDK\<T, E\>

> **BackendSDK**\<`T`, `E`\>: `{ [K in keyof T]: (args: Parameters<T[K]>) => PromisifiedReturnType<T[K]> }` & `object`

Utilities to interact with the backend plugin.

#### Type declaration

##### onEvent()

> **onEvent**: \<`K`\>(`event`: `K`, `callback`: `E`\[`K`\]) => `object`

Subscribe to a backend event.

###### Type Parameters

| Type Parameter |
| ------ |
| `K` *extends* keyof `E` |

###### Parameters

| Parameter | Type | Description |
| ------ | ------ | ------ |
| `event` | `K` | The event to subscribe to. |
| `callback` | `E`\[`K`\] | The callback to call when the event is emitted. |

###### Returns

`object`

An object with a `stop` method that can be called to stop listening to the event.

###### stop()

> **stop**: () => `void`

###### Returns

`void`

#### Type Parameters

| Type Parameter |
| ------ |
| `T` *extends* [`BackendEndpoints`](index.md#backendendpoints) |
| `E` *extends* [`BackendEvents`](index.md#backendevents) |

## UI

### UISDK

> **UISDK**: `object`

Utilities to create UI components.

#### Type declaration

##### button()

> **button**: (`options`?: `object`) => `HTMLElement`

Create a button.

###### Parameters

| Parameter | Type | Description |
| ------ | ------ | ------ |
| `options`? | \{ `label`: `string`; `leadingIcon`: [`Icon`](index.md#icon); `size`: `"small"` \| `"medium"` \| `"large"`; `trailingIcon`: [`Icon`](index.md#icon); `variant`: `"primary"` \| `"secondary"` \| `"tertiary"`; \} | Options for the button. |
| `options.label`? | `string` | The label of the button. |
| `options.leadingIcon`? | [`Icon`](index.md#icon) | The leading icon of the button. |
| `options.size`? | `"small"` \| `"medium"` \| `"large"` | The size of the button. |
| `options.trailingIcon`? | [`Icon`](index.md#icon) | The trailing icon of the button. |
| `options.variant`? | `"primary"` \| `"secondary"` \| `"tertiary"` | The variant of the button. |

###### Returns

`HTMLElement`

The button element.

###### Example

```ts
const deleteButton = sdk.ui.button({
  variant: "primary",
  label: "Delete",
  trailingIcon: "fas fa-trash-can",
  size: "small",
});
```

##### card()

> **card**: (`options`?: `object`) => `HTMLElement`

Create a card.

###### Parameters

| Parameter | Type | Description |
| ------ | ------ | ------ |
| `options`? | \{ `body`: `HTMLElement`; `footer`: `HTMLElement`; `header`: `HTMLElement`; \} | Options for the card. |
| `options.body`? | `HTMLElement` | The body of the card. |
| `options.footer`? | `HTMLElement` | The footer of the card. |
| `options.header`? | `HTMLElement` | The header of the card. |

###### Returns

`HTMLElement`

The card element.

##### httpRequestEditor()

> **httpRequestEditor**: () => [`HTTPRequestEditor`](index.md#httprequesteditor)

Create an HTTP request editor

###### Returns

[`HTTPRequestEditor`](index.md#httprequesteditor)

The HTTP request editor.

##### httpResponseEditor()

> **httpResponseEditor**: () => [`HTTPResponseEditor`](index.md#httpresponseeditor)

Create an HTTP response editor

###### Returns

[`HTTPResponseEditor`](index.md#httpresponseeditor)

The HTTP response editor.

##### well()

> **well**: (`options`?: `object`) => `HTMLElement`

Create a well.

###### Parameters

| Parameter | Type | Description |
| ------ | ------ | ------ |
| `options`? | \{ `body`: `HTMLElement`; `footer`: `HTMLElement`; `header`: `HTMLElement`; \} | Options for the well. |
| `options.body`? | `HTMLElement` | The body of the well. |
| `options.footer`? | `HTMLElement` | The footer of the well. |
| `options.header`? | `HTMLElement` | The header of the well. |

###### Returns

`HTMLElement`

The well element.

## Scopes

### Scope

> **Scope**: `object`

Represents a scope.

#### Type declaration

##### allowlist

> **allowlist**: `string`[]

The list of included items.

##### denylist

> **denylist**: `string`[]

The list of excluded items.

##### id

> **id**: [`ID`](index.md#id-3)

The unique ID of the scope.

##### name

> **name**: `string`

The name of the scope.

***

### ScopesSDK

> **ScopesSDK**: `object`

Utilities to interact with scopes

#### Type declaration

##### createScope()

> **createScope**: (`options`: `object`) => `Promise`\<[`Scope`](index.md#scope) \| `undefined`\>

Create a scope.

###### Parameters

| Parameter | Type | Description |
| ------ | ------ | ------ |
| `options` | \{ `allowlist`: `string`[]; `denylist`: `string`[]; `name`: `string`; \} | Options for the scope. |
| `options.allowlist` | `string`[] | The list of included items in the scope. |
| `options.denylist` | `string`[] | The list of excluded items in the scope. |
| `options.name` | `string` | The name of the scope. |

###### Returns

`Promise`\<[`Scope`](index.md#scope) \| `undefined`\>

The created scope.

###### Example

```ts
const newScope = await sdk.scopes.createScope({
  name: "Example",
  allowlist: ["*example.com", "*github.com"],
  denylist: ["*caido.io"],
});
```

##### deleteScope()

> **deleteScope**: (`id`: [`ID`](index.md#id-3)) => `Promise`\<`boolean`\>

Delete a scope.

###### Parameters

| Parameter | Type | Description |
| ------ | ------ | ------ |
| `id` | [`ID`](index.md#id-3) | The id of the scope to delete. |

###### Returns

`Promise`\<`boolean`\>

Whether the scope was deleted.

##### getScopes()

> **getScopes**: () => [`Scope`](index.md#scope)[]

Get all scopes.

###### Returns

[`Scope`](index.md#scope)[]

A list of scopes.

##### updateScope()

> **updateScope**: (`id`: [`ID`](index.md#id-3), `options`: `object`) => `Promise`\<[`Scope`](index.md#scope) \| `undefined`\>

Update a scope.

###### Parameters

| Parameter | Type | Description |
| ------ | ------ | ------ |
| `id` | [`ID`](index.md#id-3) | The id of the scope to update. |
| `options` | \{ `allowlist`: `string`[]; `denylist`: `string`[]; `name`: `string`; \} | Options for the scope. |
| `options.allowlist`? | `string`[] | The list of included items in the scope. |
| `options.denylist`? | `string`[] | The list of excluded items in the scope. |
| `options.name`? | `string` | The name of the scope. |

###### Returns

`Promise`\<[`Scope`](index.md#scope) \| `undefined`\>

The updated scope.

## Findings

### Finding

> **Finding**: `object`

Represents a [https://docs.caido.io/reference/features/logging/findings\|Finding](https://docs.caido.io/reference/features/logging/findings|Finding).

#### Type declaration

##### description?

> `optional` **description**: `string`

The description of the finding.

##### host

> **host**: `string`

The host of the request attached to this finding

##### id

> **id**: [`ID`](index.md#id-3)

The ID of the finding.

##### path

> **path**: `string`

The path of the request attached to this finding

##### reporter

> **reporter**: `string`

The reporter of the finding.

##### title

> **title**: `string`

The title of the finding.

***

### FindingsSDK

> **FindingsSDK**: `object`

Utilities to interact with findings

#### Type declaration

##### addRequestEditorExtension()

> **addRequestEditorExtension**: (`extension`: `Extension`) => `void`

Add an extension to the request editor.

###### Parameters

| Parameter | Type | Description |
| ------ | ------ | ------ |
| `extension` | `Extension` | The extension to add. |

###### Returns

`void`

##### addRequestViewMode()

> **addRequestViewMode**: (`options`: [`RequestViewModeOptions`](index.md#requestviewmodeoptions)) => `void`

Add a custom request view mode.

###### Parameters

| Parameter | Type | Description |
| ------ | ------ | ------ |
| `options` | [`RequestViewModeOptions`](index.md#requestviewmodeoptions) | The view mode options. |

###### Returns

`void`

##### createFinding()

> **createFinding**: (`requestId`: [`ID`](index.md#id-3), `options`: `object`) => `Promise`\<[`Finding`](index.md#finding) \| `undefined`\>

Create a [Finding](index.md#finding).

###### Parameters

| Parameter | Type | Description |
| ------ | ------ | ------ |
| `requestId` | [`ID`](index.md#id-3) | The id of the request the finding is associated with. |
| `options` | \{ `dedupeKey`: `string`; `description`: `string`; `reporter`: `string`; `title`: `string`; \} | Options for the finding. |
| `options.dedupeKey`? | `string` | If a finding with the same deduplication key already exists, it will not create a new finding. |
| `options.description`? | `string` | The description of the finding. |
| `options.reporter` | `string` | The reporter of the finding. |
| `options.title` | `string` | The title of the finding. |

###### Returns

`Promise`\<[`Finding`](index.md#finding) \| `undefined`\>

The created finding.

## Commands

### CommandContext

> **CommandContext**: [`CommandContextBase`](index.md#commandcontextbase) \| [`CommandContextRequestRow`](index.md#commandcontextrequestrow) \| [`CommandContextRequest`](index.md#commandcontextrequest) \| [`CommandContextResponse`](index.md#commandcontextresponse)

Represents the context in which a command is executed.

***

### CommandContextBase

> **CommandContextBase**: `object`

The base context for a command.
This context is used for commands that are not executed in a specific context, such as via shortcuts and the command palette.

#### Type declaration

##### type

> **type**: `"BaseContext"`

***

### CommandContextRequest

> **CommandContextRequest**: `object`

The context for a command that is executed on a request pane.

#### Type declaration

##### request

> **request**: [`RequestDraft`](index.md#requestdraft) \| [`RequestFull`](index.md#requestfull)

The request that is currently open in the request pane.
If the request has not yet been saved in the database, the id will be undefined.

##### selection

> **selection**: `string`

The currently selected text in the request pane.

##### type

> **type**: `"RequestContext"`

***

### CommandContextRequestRow

> **CommandContextRequestRow**: `object`

The context for a command that is executed on a row in the request table.

#### Type declaration

##### requests

> **requests**: [`RequestMeta`](index.md#requestmeta)[]

The requests that are selected in the request table.

##### type

> **type**: `"RequestRowContext"`

***

### CommandContextResponse

> **CommandContextResponse**: `object`

The context for a command that is executed on a response pane.

#### Type declaration

##### request

> **request**: [`RequestMeta`](index.md#requestmeta)

The request that is associated with the response.

##### response

> **response**: `object`

The response that is currently open in the response pane.

###### response.id

> **id**: [`ID`](index.md#id-3)

###### response.raw

> **raw**: `string`

###### response.roundtripTime

> **roundtripTime**: `number`

###### response.statusCode

> **statusCode**: `number`

##### selection

> **selection**: `string`

The currently selected text in the response pane.

##### type

> **type**: `"ResponseContext"`

***

### CommandsSDK

> **CommandsSDK**: `object`

Utilities to interact with commands

#### Type declaration

##### register()

> **register**: (`id`: [`CommandID`](index.md#commandid), `options`: `object`) => `void`

Register a command.

###### Parameters

| Parameter | Type | Description |
| ------ | ------ | ------ |
| `id` | [`CommandID`](index.md#commandid) | The id of the command. |
| `options` | \{ `group`: `string`; `name`: `string`; `run`: (`context`: [`CommandContext`](index.md#commandcontext)) => `Promise`\<`void`\> \| `void`; `when`: (`context`: [`CommandContext`](index.md#commandcontext)) => `Promise`\<`boolean`\> \| `boolean`; \} | Options for the command. |
| `options.group`? | `string` | The group this command belongs to. |
| `options.name` | `string` | The name of the command. |
| `options.run` | (`context`: [`CommandContext`](index.md#commandcontext)) => `Promise`\<`void`\> \| `void` | The function to run when the command is executed. |
| `options.when`? | (`context`: [`CommandContext`](index.md#commandcontext)) => `Promise`\<`boolean`\> \| `boolean` | A function to determine if the command is available. |

###### Returns

`void`

###### Example

```ts
sdk.commands.register("hello", {
  name: "Print to console.",
  run: () => console.log("Hello world!"),
  group: "Custom Commands",
});
```

## Menu

### MenuItem

> **MenuItem**: [`RequestRowMenuItem`](index.md#requestrowmenuitem) \| [`SettingsMenuItem`](index.md#settingsmenuitem) \| [`RequestMenuItem`](index.md#requestmenuitem) \| [`ResponseMenuItem`](index.md#responsemenuitem)

A content-menu item.

***

### MenuSDK

> **MenuSDK**: `object`

Utilities to insert menu items and context-menus throughout the UI.

#### Type declaration

##### registerItem()

> **registerItem**: (`item`: [`MenuItem`](index.md#menuitem)) => `void`

Register a menu item.

###### Parameters

| Parameter | Type | Description |
| ------ | ------ | ------ |
| `item` | [`MenuItem`](index.md#menuitem) | The menu item to register. |

###### Returns

`void`

###### Example

```ts
sdk.menu.registerItem({
  type: "Request",
  commandId: "hello",
  leadingIcon: "fas fa-hand",
});
```

***

### RequestMenuItem

> **RequestMenuItem**: `object`

A context-menu item that appears when right-clicking a request pane.

#### Type declaration

##### commandId

> **commandId**: [`CommandID`](index.md#commandid)

The command ID to execute when the menu item is clicked.

##### leadingIcon?

> `optional` **leadingIcon**: `string`

The icon to display to the left of the menu item.

##### type

> **type**: `"Request"`

***

### RequestRowMenuItem

> **RequestRowMenuItem**: `object`

A context-menu item that appears when right-clicking a request row.

#### Type declaration

##### commandId

> **commandId**: [`CommandID`](index.md#commandid)

The command ID to execute when the menu item is clicked.

##### leadingIcon?

> `optional` **leadingIcon**: `string`

The icon to display to the left of the menu item.

##### type

> **type**: `"RequestRow"`

***

### ResponseMenuItem

> **ResponseMenuItem**: `object`

A context-menu item that appears when right-clicking a response pane.

#### Type declaration

##### commandId

> **commandId**: [`CommandID`](index.md#commandid)

The command ID to execute when the menu item is

##### leadingIcon?

> `optional` **leadingIcon**: `string`

The icon to display to the left of the menu item.

##### type

> **type**: `"Response"`

***

### SettingsMenuItem

> **SettingsMenuItem**: `object`

A menu item that appears in the settings menu.

#### Type declaration

##### label

> **label**: `string`

The label of the menu item.

##### leadingIcon?

> `optional` **leadingIcon**: [`Icon`](index.md#icon)

The [Icon](index.md#icon) to display to the left of the menu item.

##### path

> **path**: `string`

The path that the user will be navigated to when the menu item is clicked
The path must start with "/settings/".

##### type

> **type**: `"Settings"`

## Navigation

### NavigationSDK

> **NavigationSDK**: `object`

Utilities to interact with navigation.

#### Type declaration

##### addPage()

> **addPage**: (`path`: `string`, `options`: `object`) => `void`

Add a page to the navigation.

###### Parameters

| Parameter | Type | Description |
| ------ | ------ | ------ |
| `path` | `string` | The path of the page. |
| `options` | \{ `body`: `HTMLElement`; `onEnter`: () => `void`; `topbar`: `HTMLElement`; \} | Options for the page. |
| `options.body` | `HTMLElement` | The body of the page. |
| `options.onEnter`? | () => `void` | The callback to execute when the page is entered. |
| `options.topbar`? | `HTMLElement` | The topbar of the page. |

###### Returns

`void`

##### goTo()

> **goTo**: (`route`: `string` \| \{ `id`: [`Routes`](index.md#routes); \}) => `void`

Navigate to a route or path.

###### Parameters

| Parameter | Type | Description |
| ------ | ------ | ------ |
| `route` | `string` \| \{ `id`: [`Routes`](index.md#routes); \} | The route to navigate to. Can be a route ID object or a custom path string. |

###### Returns

`void`

###### Example

```ts
sdk.navigation.goTo({ id: Routes.Replay });
sdk.navigation.goTo({ id: Routes.Projects });
sdk.navigation.goTo("/my-plugin-page");
```

##### onPageChange()

> **onPageChange**: (`callback`: (`route`: [`PageChangeEvent`](index.md#pagechangeevent)) => `void`) => [`ListenerHandle`](index.md#listenerhandle)

Subscribe to page changes.

###### Parameters

| Parameter | Type | Description |
| ------ | ------ | ------ |
| `callback` | (`route`: [`PageChangeEvent`](index.md#pagechangeevent)) => `void` | The callback to call when the page changes. |

###### Returns

[`ListenerHandle`](index.md#listenerhandle)

An object with a `stop` method that can be called to stop listening to page changes.

###### Example

```ts
const handler = sdk.navigation.onPageChange((event) => {
  console.log('Page changed to:', event.routeId);
  console.log('- path:', event.path);
});

// Later, stop listening
handler.stop();
```

## Window

### WindowSDK

> **WindowSDK**: `object`

Utilities to interact with the active page.

#### Type declaration

##### getActiveEditor()

> **getActiveEditor**: () => [`Editor`](index.md#editor) \| `undefined`

Get the active editor.

###### Returns

[`Editor`](index.md#editor) \| `undefined`

The active editor.

##### showDialog()

> **showDialog**: (`component`: [`ComponentDefinition`](index.md#componentdefinition), `options`?: [`DialogOptions`](index.md#dialogoptions)) => [`Dialog`](index.md#dialog)

Show a dialog component.

###### Parameters

| Parameter | Type | Description |
| ------ | ------ | ------ |
| `component` | [`ComponentDefinition`](index.md#componentdefinition) | The custom slot content to display in the dialog. |
| `options`? | [`DialogOptions`](index.md#dialogoptions) | Options for the dialog. |

###### Returns

[`Dialog`](index.md#dialog)

A dialog object that can be used to close the dialog.

##### showToast()

> **showToast**: (`message`: `string`, `options`?: `object`) => `void`

Show a toast message.

###### Parameters

| Parameter | Type | Description |
| ------ | ------ | ------ |
| `message` | `string` | The message to show. |
| `options`? | \{ `duration`: `number`; `variant`: `"success"` \| `"error"` \| `"warning"` \| `"info"`; \} | Options for the toast message. |
| `options.duration`? | `number` | The duration of the toast message in milliseconds. |
| `options.variant`? | `"success"` \| `"error"` \| `"warning"` \| `"info"` | The variant of the toast message. |

###### Returns

`void`

## Storage

### StorageSDK

> **StorageSDK**: `object`

Utilities to interact with frontend-plugin storage.

#### Type declaration

##### get()

> **get**: () => [`JSONValue`](index.md#jsonvalue)

Get the storage.

###### Returns

[`JSONValue`](index.md#jsonvalue)

The storage.

##### onChange()

> **onChange**: (`callback`: (`value`: [`JSONValue`](index.md#jsonvalue)) => `void`) => `void`

Subscribe to storage changes.

###### Parameters

| Parameter | Type | Description |
| ------ | ------ | ------ |
| `callback` | (`value`: [`JSONValue`](index.md#jsonvalue)) => `void` | The callback to call when the storage changes. |

###### Returns

`void`

##### set()

> **set**: \<`T`\>(`value`: [`JSONCompatible`](index.md#jsoncompatiblet)\<`T`\>) => `Promise`\<`void`\>

Set the storage.

###### Type Parameters

| Type Parameter |
| ------ |
| `T` |

###### Parameters

| Parameter | Type | Description |
| ------ | ------ | ------ |
| `value` | [`JSONCompatible`](index.md#jsoncompatiblet)\<`T`\> | The value to set the storage to |

###### Returns

`Promise`\<`void`\>

A promise that resolves when the storage has been set.

## Shortcuts

### ShortcutsSDK

> **ShortcutsSDK**: `object`

Utilities to interact with shortcuts.

#### Type declaration

##### register()

> **register**: (`commandId`: [`CommandID`](index.md#commandid), `keys`: `string`[]) => `void`

Register a shortcut.

###### Parameters

| Parameter | Type | Description |
| ------ | ------ | ------ |
| `commandId` | [`CommandID`](index.md#commandid) | The id of the command to run when the shortcut is triggered. |
| `keys` | `string`[] | The keys of the shortcut. Check out [KeyboardEvent.key](https://developer.mozilla.org/en-US/docs/Web/API/UI_Events/Keyboard_event_key_values) for the list of supported keys. |

###### Returns

`void`

## Command Palette

### CommandPaletteSDK

> **CommandPaletteSDK**: `object`

Utilities to interact with the command palette.

#### Type declaration

##### pushView()

> **pushView**: (`view`: [`CommandPaletteView`](index.md#commandpaletteview)) => `void`

Push a new view onto the command palette view stack.

###### Parameters

| Parameter | Type | Description |
| ------ | ------ | ------ |
| `view` | [`CommandPaletteView`](index.md#commandpaletteview) | The view to push onto the stack. |

###### Returns

`void`

##### register()

> **register**: (`commandId`: [`CommandID`](index.md#commandid)) => `void`

Register a command.

###### Parameters

| Parameter | Type | Description |
| ------ | ------ | ------ |
| `commandId` | [`CommandID`](index.md#commandid) | The id of the command to register. |

###### Returns

`void`

***

### CommandPaletteView

> **CommandPaletteView**: `object`

Command palette view definition for custom UI content.

#### Type declaration

##### definition

> **definition**: [`ComponentDefinition`](index.md#componentdefinition)

##### type

> **type**: `"Custom"`

## Sidebar

### SidebarItem

> **SidebarItem**: `object`

Represents a sidebar item.

#### Type declaration

##### setCount()

> **setCount**: (`count`: `number`) => `void`

Set the value of a notification badge next to the sidebar item.

###### Parameters

| Parameter | Type | Description |
| ------ | ------ | ------ |
| `count` | `number` | The number to display in the badge. A value of 0 will hide the badge. |

###### Returns

`void`

***

### SidebarSDK

> **SidebarSDK**: `object`

Utilities to interact with the sidebar.

#### Type declaration

##### registerItem()

> **registerItem**: (`name`: `string`, `path`: `string`, `options`?: `object`) => [`SidebarItem`](index.md#sidebaritem)

Register a sidebar item.

###### Parameters

| Parameter | Type | Description |
| ------ | ------ | ------ |
| `name` | `string` | The name of the sidebar item. |
| `path` | `string` | The path that the user will be navigated to when the sidebar item is clicked. |
| `options`? | \{ `group`: `string`; `icon`: [`Icon`](index.md#icon); `isExternal`: `boolean`; \} | Options for the sidebar item. |
| `options.group`? | `string` | The group the sidebar item belongs to. |
| `options.icon`? | [`Icon`](index.md#icon) | The [Icon](index.md#icon) of the sidebar item. |
| `options.isExternal`? | `boolean` | Whether the path points to an external URL. |

###### Returns

[`SidebarItem`](index.md#sidebaritem)

The created sidebar item.

###### Example

```ts
sdk.sidebar.registerItem("My Plugin", "/my-plugin-page", {
  icon: "fas fa-rocket",
});
```

## Replay

### CurrentReplaySessionChangeEvent

> **CurrentReplaySessionChangeEvent**: `object`

Event fired when the current replay session changes.

#### Type declaration

##### sessionId

> **sessionId**: [`ID`](index.md#id-3) \| `undefined`

The ID of the newly selected session, or undefined if no session is selected.

***

### OpenTabOptions

> **OpenTabOptions**: `object`

Options for opening a tab.

#### Type declaration

##### select?

> `optional` **select**: `boolean`

Whether to select the tab after opening it.
Defaults to true.

***

### ReplayCollection

> **ReplayCollection**: `object`

A collection in Replay.

#### Type declaration

##### id

> **id**: [`ID`](index.md#id-3)

The ID of the collection.

##### name

> **name**: `string`

The name of the collection.

##### sessionIds

> **sessionIds**: [`ID`](index.md#id-3)[]

The sessions in the collection.

***

### ReplaySDK

> **ReplaySDK**: `object`

Utilities to interact with Replay.

#### Type declaration

##### addRequestEditorExtension()

> **addRequestEditorExtension**: (`extension`: `Extension`) => `void`

Add an extension to the request editor.

###### Parameters

| Parameter | Type | Description |
| ------ | ------ | ------ |
| `extension` | `Extension` | The extension to add. |

###### Returns

`void`

##### addRequestViewMode()

> **addRequestViewMode**: (`options`: [`RequestViewModeOptions`](index.md#requestviewmodeoptions)) => `void`

Add a custom view mode for requests.

###### Parameters

| Parameter | Type | Description |
| ------ | ------ | ------ |
| `options` | [`RequestViewModeOptions`](index.md#requestviewmodeoptions) | The view mode options. |

###### Returns

`void`

##### addToSlot

> **addToSlot**: [`DefineAddToSlotFn`](index.md#defineaddtoslotfntmap)\<[`ReplaySlotContent`](index.md#replayslotcontent)\>

Add a component to a slot.

###### Param

The slot to add the component to.

###### Param

The content to add to the slot.

###### Example

```ts
addToSlot(ReplaySlot.SessionToolbarPrimary, {
  kind: "Command",
  commandId: "my-command",
  icon: "my-icon",
});

addToSlot(ReplaySlot.SessionToolbarSecondary, {
  kind: "Custom",
  component: MyComponent,
});

addToSlot(ReplaySlot.Topbar, {
  kind: "Button",
  label: "My Button",
  icon: "my-icon",
  onClick: () => {
    console.log("Button clicked");
  },
});
```

##### closeTab()

> **closeTab**: (`sessionId`: [`ID`](index.md#id-3)) => `void`

Close a replay tab for the given session.

###### Parameters

| Parameter | Type | Description |
| ------ | ------ | ------ |
| `sessionId` | [`ID`](index.md#id-3) | The ID of the session to close. |

###### Returns

`void`

##### createCollection()

> **createCollection**: (`name`: `string`) => `Promise`\<[`ReplayCollection`](index.md#replaycollection)\>

Create a new collection.

###### Parameters

| Parameter | Type | Description |
| ------ | ------ | ------ |
| `name` | `string` | The name of the collection to create. |

###### Returns

`Promise`\<[`ReplayCollection`](index.md#replaycollection)\>

##### createSession()

> **createSession**: (`source`: [`RequestSource`](index.md#requestsource), `collectionId`?: [`ID`](index.md#id-3)) => `Promise`\<`void`\>

Create a session.

###### Parameters

| Parameter | Type | Description |
| ------ | ------ | ------ |
| `source` | [`RequestSource`](index.md#requestsource) | - |
| `collectionId`? | [`ID`](index.md#id-3) | The ID of the collection to add the request. |

###### Returns

`Promise`\<`void`\>

##### deleteCollection()

> **deleteCollection**: (`id`: [`ID`](index.md#id-3)) => `Promise`\<`boolean`\>

Delete a collection.

###### Parameters

| Parameter | Type | Description |
| ------ | ------ | ------ |
| `id` | [`ID`](index.md#id-3) | The ID of the collection to delete. |

###### Returns

`Promise`\<`boolean`\>

Whether the collection was deleted.

##### deleteSessions()

> **deleteSessions**: (`sessionIds`: [`ID`](index.md#id-3)[]) => `Promise`\<[`ID`](index.md#id-3)[]\>

Delete a session.

###### Parameters

| Parameter | Type | Description |
| ------ | ------ | ------ |
| `sessionIds` | [`ID`](index.md#id-3)[] | The IDs of the sessions to delete. |

###### Returns

`Promise`\<[`ID`](index.md#id-3)[]\>

##### getCollections()

> **getCollections**: () => [`ReplayCollection`](index.md#replaycollection)[]

Get the list of all replay collections.

###### Returns

[`ReplayCollection`](index.md#replaycollection)[]

The list of all replay collections.

##### getSessions()

> **getSessions**: () => [`ReplaySession`](index.md#replaysession)[]

Get the list of all replay sessions.

###### Returns

[`ReplaySession`](index.md#replaysession)[]

The list of all replay sessions.

##### getTabs()

> **getTabs**: () => [`ReplayTab`](index.md#replaytab)[]

Get the list of all open replay tabs.

###### Returns

[`ReplayTab`](index.md#replaytab)[]

The list of all open replay tabs.

##### moveSession()

> **moveSession**: (`sessionId`: [`ID`](index.md#id-3), `collectionId`: [`ID`](index.md#id-3)) => `Promise`\<[`ReplaySession`](index.md#replaysession)\>

Move a session to a different collection.

###### Parameters

| Parameter | Type | Description |
| ------ | ------ | ------ |
| `sessionId` | [`ID`](index.md#id-3) | The ID of the session to move. |
| `collectionId` | [`ID`](index.md#id-3) | The ID of the collection to move the session to. |

###### Returns

`Promise`\<[`ReplaySession`](index.md#replaysession)\>

The updated session.

##### onCurrentSessionChange()

> **onCurrentSessionChange**: (`callback`: (`event`: [`CurrentReplaySessionChangeEvent`](index.md#currentreplaysessionchangeevent)) => `void`) => [`ListenerHandle`](index.md#listenerhandle)

Subscribe to current replay session changes.

###### Parameters

| Parameter | Type | Description |
| ------ | ------ | ------ |
| `callback` | (`event`: [`CurrentReplaySessionChangeEvent`](index.md#currentreplaysessionchangeevent)) => `void` | The callback to call when the selected session changes. |

###### Returns

[`ListenerHandle`](index.md#listenerhandle)

An object with a `stop` method that can be called to stop listening to session changes.

###### Example

```ts
const handler = sdk.replay.onCurrentSessionChange((event) => {
  console.log(`Session ${event.sessionId} got selected!`);
});

// Later, stop listening
handler.stop();
```

##### openTab()

> **openTab**: (`sessionId`: [`ID`](index.md#id-3), `options`?: [`OpenTabOptions`](index.md#opentaboptions)) => `void`

Open a replay tab for the given session.

###### Parameters

| Parameter | Type | Description |
| ------ | ------ | ------ |
| `sessionId` | [`ID`](index.md#id-3) | The ID of the session to open. |
| `options`? | [`OpenTabOptions`](index.md#opentaboptions) | The options for opening the tab. |

###### Returns

`void`

##### renameCollection()

> **renameCollection**: (`id`: [`ID`](index.md#id-3), `name`: `string`) => `Promise`\<[`ReplayCollection`](index.md#replaycollection)\>

Rename a collection.

###### Parameters

| Parameter | Type | Description |
| ------ | ------ | ------ |
| `id` | [`ID`](index.md#id-3) | The ID of the collection to rename. |
| `name` | `string` | The new name of the collection. |

###### Returns

`Promise`\<[`ReplayCollection`](index.md#replaycollection)\>

The updated collection.

##### renameSession()

> **renameSession**: (`id`: [`ID`](index.md#id-3), `name`: `string`) => `Promise`\<[`ReplaySession`](index.md#replaysession)\>

Rename a session.

###### Parameters

| Parameter | Type | Description |
| ------ | ------ | ------ |
| `id` | [`ID`](index.md#id-3) | The ID of the session to rename. |
| `name` | `string` | The new name of the session. |

###### Returns

`Promise`\<[`ReplaySession`](index.md#replaysession)\>

The updated session.

##### sendRequest()

> **sendRequest**: (`sessionId`: [`ID`](index.md#id-3), `options`: [`SendRequestOptions`](index.md#sendrequestoptions)) => `Promise`\<`void`\>

Send a request to the Replay backend.

###### Parameters

| Parameter | Type | Description |
| ------ | ------ | ------ |
| `sessionId` | [`ID`](index.md#id-3) | - |
| `options` | [`SendRequestOptions`](index.md#sendrequestoptions) | The options for sending the request. |

###### Returns

`Promise`\<`void`\>

###### Example

```ts
sendRequest(sessionId, {
  connectionInfo: {
    SNI: "example.com",
    host: "example.com",
    isTLS: true,
    port: 443,
  },
  raw: "GET / HTTP/1.1\r\nHost: example.com\r\n\r\n",
  updateContentLength: false,
});
```

***

### ReplaySession

> **ReplaySession**: `object`

A session in Replay.

#### Type declaration

##### collectionId

> **collectionId**: [`ID`](index.md#id-3)

The ID of the collection the session belongs to.

##### id

> **id**: [`ID`](index.md#id-3)

The ID of the session.

##### name

> **name**: `string`

The name of the session.

***

### ReplayTab

> **ReplayTab**: `object`

A replay tab.

#### Type declaration

##### sessionId

> **sessionId**: [`ID`](index.md#id-3)

The ID of the session associated with this tab.

***

### RequestSource

> **RequestSource**: \{ `connectionInfo`: [`SendRequestOptions`](index.md#sendrequestoptions)\[`"connectionInfo"`\]; `raw`: `string`; `type`: `"Raw"`; \} \| \{ `id`: `string`; `type`: `"ID"`; \}

#### Remarks

This type is a discriminated union with two possible shapes:
- A raw request, containing the raw HTTP request string and connection information.
- A reference to an existing request ID.

#### Example

```ts
// Using a raw request
const source: RequestSource = {
  type: "Raw",
  raw: "GET /api/data HTTP/1.1",
  connectionInfo: { ... }
};
// Using an ID
const source: RequestSource = {
  type: "ID",
  id: "request-123"
};
```

***

### SendRequestOptions

> **SendRequestOptions**: `object`

Options for sending a request.

#### Type declaration

##### background?

> `optional` **background**: `boolean`

Whether to send the request in the background without updating the UI.
If true, the request will not update the UI.
If false, the UI will be updated to display the session and the new request.
Defaults to false.

##### connectionClose?

> `optional` **connectionClose**: `boolean`

Whether to force close the connection by setting Connection: close header.
Defaults to true.

##### connectionInfo

> **connectionInfo**: `object`

The connection information to use for the request.

###### connectionInfo.host

> **host**: `string`

The host to use for the request.

###### connectionInfo.isTLS

> **isTLS**: `boolean`

Whether the request is TLS.

###### connectionInfo.port

> **port**: `number`

The port to use for the request.

###### connectionInfo.SNI?

> `optional` **SNI**: `string`

The SNI to use for the request.
If not provided, the SNI will be inferred from the host.

##### overwriteDraft?

> `optional` **overwriteDraft**: `boolean`

Whether to overwrite the editor's draft content.
If true, draft content will be overwritten with the new request.
If false, the draft will be kept.
Defaults to true.

##### raw

> **raw**: `string`

The raw request to send.

##### updateContentLength?

> `optional` **updateContentLength**: `boolean`

Whether to update the content length automatically to match the body.
Defaults to true.

***

### ReplaySlot

> `const` **ReplaySlot**: `object`

The slots in the Replay UI.

#### Type declaration

##### SessionToolbarPrimary

> `readonly` **SessionToolbarPrimary**: `"session-toolbar-primary"`

The left side of the session toolbar.

##### SessionToolbarSecondary

> `readonly` **SessionToolbarSecondary**: `"session-toolbar-secondary"`

The right side of the session toolbar.

##### Topbar

> `readonly` **Topbar**: `"topbar"`

The left side of the topbar.

## HTTP History

### HTTPHistorySDK

> **HTTPHistorySDK**: `object`

Utilities to interact with the HTTP History page.

#### Type declaration

##### addRequestEditorExtension()

> **addRequestEditorExtension**: (`extension`: `Extension`) => `void`

Add an extension to the request editor.

###### Parameters

| Parameter | Type | Description |
| ------ | ------ | ------ |
| `extension` | `Extension` | The extension to add. |

###### Returns

`void`

##### addRequestViewMode()

> **addRequestViewMode**: (`options`: [`RequestViewModeOptions`](index.md#requestviewmodeoptions)) => `void`

Add a custom request view mode.

###### Parameters

| Parameter | Type | Description |
| ------ | ------ | ------ |
| `options` | [`RequestViewModeOptions`](index.md#requestviewmodeoptions) | The view mode options. |

###### Returns

`void`

##### addResponseEditorExtension()

> **addResponseEditorExtension**: (`extension`: `Extension`) => `void`

Add an extension to the response editor.

###### Parameters

| Parameter | Type | Description |
| ------ | ------ | ------ |
| `extension` | `Extension` | The extension to add. |

###### Returns

`void`

##### getQuery()

> **getQuery**: () => [`HTTPQL`](index.md#httpql)

Get the current HTTPQL query.

###### Returns

[`HTTPQL`](index.md#httpql)

The current HTTPQL query.

##### getScopeId()

> **getScopeId**: () => [`ID`](index.md#id-3) \| `undefined`

Get the current scope ID.

###### Returns

[`ID`](index.md#id-3) \| `undefined`

The current scope ID.

##### scrollTo()

> **scrollTo**: (`id`: [`ID`](index.md#id-3)) => `void`

Scrolls the HTTP History table to a specific entry.

###### Parameters

| Parameter | Type | Description |
| ------ | ------ | ------ |
| `id` | [`ID`](index.md#id-3) | The ID of the entry to scroll to. |

###### Returns

`void`

##### setQuery()

> **setQuery**: (`query`: [`HTTPQL`](index.md#httpql)) => `void`

Set the HTTPQL query that will be applied on the HTTP History table results.

###### Parameters

| Parameter | Type | Description |
| ------ | ------ | ------ |
| `query` | [`HTTPQL`](index.md#httpql) | The HTTPQL query. |

###### Returns

`void`

##### setScope()

> **setScope**: (`id`: [`ID`](index.md#id-3) \| `undefined`) => `Promise`\<`void`\>

Set the current scope.

###### Parameters

| Parameter | Type | Description |
| ------ | ------ | ------ |
| `id` | [`ID`](index.md#id-3) \| `undefined` | The ID of the scope to set. |

###### Returns

`Promise`\<`void`\>

## Search

### SearchSDK

> **SearchSDK**: `object`

Utilities to interact with the Search page.

#### Type declaration

##### addRequestEditorExtension()

> **addRequestEditorExtension**: (`extension`: `Extension`) => `void`

Add an extension to the request editor.

###### Parameters

| Parameter | Type | Description |
| ------ | ------ | ------ |
| `extension` | `Extension` | The extension to add. |

###### Returns

`void`

##### addRequestViewMode()

> **addRequestViewMode**: (`options`: [`RequestViewModeOptions`](index.md#requestviewmodeoptions)) => `void`

Add a custom request view mode.

###### Parameters

| Parameter | Type | Description |
| ------ | ------ | ------ |
| `options` | [`RequestViewModeOptions`](index.md#requestviewmodeoptions) | The view mode options. |

###### Returns

`void`

##### getQuery()

> **getQuery**: () => [`HTTPQL`](index.md#httpql)

Get the current HTTPQL query.

###### Returns

[`HTTPQL`](index.md#httpql)

The current HTTPQL query.

##### getScopeId()

> **getScopeId**: () => [`ID`](index.md#id-3) \| `undefined`

Get the current scope ID.

###### Returns

[`ID`](index.md#id-3) \| `undefined`

The current scope ID.

##### scrollTo()

> **scrollTo**: (`id`: [`ID`](index.md#id-3)) => `void`

Scrolls the Search table to a specific request.

###### Parameters

| Parameter | Type | Description |
| ------ | ------ | ------ |
| `id` | [`ID`](index.md#id-3) | The ID of the request to scroll to. |

###### Returns

`void`

##### setQuery()

> **setQuery**: (`query`: [`HTTPQL`](index.md#httpql)) => `void`

Set the HTTPQL query that will be applied on the search table results.

###### Parameters

| Parameter | Type | Description |
| ------ | ------ | ------ |
| `query` | [`HTTPQL`](index.md#httpql) | The HTTPQL query. |

###### Returns

`void`

##### setScope()

> **setScope**: (`id`: [`ID`](index.md#id-3) \| `undefined`) => `Promise`\<`void`\>

Set the current scope.

###### Parameters

| Parameter | Type | Description |
| ------ | ------ | ------ |
| `id` | [`ID`](index.md#id-3) \| `undefined` | The ID of the scope to set. |

###### Returns

`Promise`\<`void`\>

## Files

### Asset

> **Asset**: `object`

A static asset.

#### Type declaration

##### asArrayBuffer()

> **asArrayBuffer**: () => `Promise`\<`ArrayBuffer`\>

###### Returns

`Promise`\<`ArrayBuffer`\>

##### asJson()

> **asJson**: \<`T`\>() => `Promise`\<`T`\>

###### Type Parameters

| Type Parameter | Default type |
| ------ | ------ |
| `T` | `unknown` |

###### Returns

`Promise`\<`T`\>

##### asReadableStream()

> **asReadableStream**: () => `ReadableStream`

###### Returns

`ReadableStream`

##### asString()

> **asString**: () => `Promise`\<`string`\>

###### Returns

`Promise`\<`string`\>

***

### AssetsSDK

> **AssetsSDK**: `object`

Utilities to interact with the plugin's static assets.

#### Type declaration

##### get()

> **get**: (`path`: `string`) => `Promise`\<[`Asset`](index.md#asset)\>

Get a file from the assets folder.

###### Parameters

| Parameter | Type |
| ------ | ------ |
| `path` | `string` |

###### Returns

`Promise`\<[`Asset`](index.md#asset)\>

The asset file.

***

### FilesSDK

> **FilesSDK**: `object`

SDK for interacting with the Files page.

#### Type declaration

##### create()

> **create**: (`file`: `File`) => `Promise`\<[`HostedFile`](index.md#hostedfile)\>

Uploads a file to the host.

###### Parameters

| Parameter | Type | Description |
| ------ | ------ | ------ |
| `file` | `File` | The file to upload. |

###### Returns

`Promise`\<[`HostedFile`](index.md#hostedfile)\>

The uploaded file.

##### delete()

> **delete**: (`id`: `string`) => `Promise`\<`void`\>

Deletes a file from the host.

###### Parameters

| Parameter | Type | Description |
| ------ | ------ | ------ |
| `id` | `string` | The ID of the file to delete. |

###### Returns

`Promise`\<`void`\>

The deleted file.

##### getAll()

> **getAll**: () => [`HostedFile`](index.md#hostedfile)[]

Gets all hosted files.

###### Returns

[`HostedFile`](index.md#hostedfile)[]

The files.

##### rename()

> **rename**: (`id`: `string`, `name`: `string`) => `Promise`\<[`HostedFile`](index.md#hostedfile)\>

Renames a file on the host.

###### Parameters

| Parameter | Type | Description |
| ------ | ------ | ------ |
| `id` | `string` | The ID of the file to rename. |
| `name` | `string` | The new name of the file. |

###### Returns

`Promise`\<[`HostedFile`](index.md#hostedfile)\>

The renamed file.

***

### HostedFile

> **HostedFile**: `object`

A hosted file.

#### Type declaration

##### createdAt

> **createdAt**: `Date`

The date the file was created.

##### id

> **id**: `string`

The ID of the file.

##### name

> **name**: `string`

The name of the file.

##### path

> **path**: `string`

The path of the file.

##### size

> **size**: `number`

The size of the file in bytes.

##### status

> **status**: `"ready"` \| `"error"`

The status of the file.

##### updatedAt

> **updatedAt**: `Date`

The date the file was updated.

## AI

### AIProvider

> **AIProvider**: `ProviderV2` & (`modelId`: `string`) => `LanguageModelV2`

Official AI Provider to be used by the [ai](https://ai-sdk.dev/) library.

***

### AiSDK

> **AiSDK**: `object`

Utilities to interact with AI.

#### Type declaration

##### createProvider()

> **createProvider**: () => [`AIProvider`](index.md#aiprovider)

Creates a new AI provider instance that can be used with the [ai](https://ai-sdk.dev/) library.

###### Returns

[`AIProvider`](index.md#aiprovider)

A provider instance compatible with the [ai](https://ai-sdk.dev/) library.

## Automate

### AutomateSDK

> **AutomateSDK**: `object`

Utilities to interact with the Automate page.

#### Type declaration

##### addRequestEditorExtension()

> **addRequestEditorExtension**: (`extension`: `Extension`) => `void`

Add an extension to the request editor.

###### Parameters

| Parameter | Type | Description |
| ------ | ------ | ------ |
| `extension` | `Extension` | The extension to add. |

###### Returns

`void`

##### addRequestViewMode()

> **addRequestViewMode**: (`options`: [`RequestViewModeOptions`](index.md#requestviewmodeoptions)) => `void`

Add a custom request view mode.

###### Parameters

| Parameter | Type | Description |
| ------ | ------ | ------ |
| `options` | [`RequestViewModeOptions`](index.md#requestviewmodeoptions) | The view mode options. |

###### Returns

`void`

## Environment

### EnvironmentSDK

> **EnvironmentSDK**: `object`

Utilities to interact with the environment.

#### Type declaration

##### getVar()

> **getVar**: (`name`: `string`) => `string` \| `undefined`

Get the value of an environment variable.

###### Parameters

| Parameter | Type | Description |
| ------ | ------ | ------ |
| `name` | `string` | The name of the environment variable. |

###### Returns

`string` \| `undefined`

The value of the environment variable.

##### getVars()

> **getVars**: () => [`EnvironmentVariable`](index.md#environmentvariable)[]

Get all environment variables available in the global environment and the selected environment.

###### Returns

[`EnvironmentVariable`](index.md#environmentvariable)[]

All environment variables.

## Filters

### Filter

> **Filter**: `object`

Represents a filter.

#### Type declaration

##### alias

> **alias**: `string`

The alias of the filter.
This alias is used when referencing the filter in an HTTPQL query (e.g. `preset:my-alias`).

##### id

> **id**: [`ID`](index.md#id-3)

The ID of the filter.

##### name

> **name**: `string`

The name of the filter.

##### query

> **query**: [`HTTPQL`](index.md#httpql)

The HTTPQL expression of the filter.

***

### FiltersSDK

> **FiltersSDK**: `object`

SDK for interacting with the Filters page.

#### Type declaration

##### create()

> **create**: (`options`: `object`) => `Promise`\<[`Filter`](index.md#filter)\>

Creates a filter.

###### Parameters

| Parameter | Type | Description |
| ------ | ------ | ------ |
| `options` | \{ `alias`: `string`; `name`: `string`; `query`: [`HTTPQL`](index.md#httpql); \} | Options for the filter. |
| `options.alias` | `string` | The alias of the filter. Used when referencing the filter in an HTTPQL query (e.g. `preset:my-alias`). Should be unique and follow the format `[a-zA-Z0-9_-]+`. |
| `options.name` | `string` | The name of the filter. Should be unique. |
| `options.query` | [`HTTPQL`](index.md#httpql) | The HTTPQL query of the filter. |

###### Returns

`Promise`\<[`Filter`](index.md#filter)\>

The created filter.

##### delete()

> **delete**: (`id`: [`ID`](index.md#id-3)) => `Promise`\<`void`\>

Deletes a filter.

###### Parameters

| Parameter | Type | Description |
| ------ | ------ | ------ |
| `id` | [`ID`](index.md#id-3) | The ID of the filter to delete. |

###### Returns

`Promise`\<`void`\>

##### getAll()

> **getAll**: () => [`Filter`](index.md#filter)[]

Gets all filters.

###### Returns

[`Filter`](index.md#filter)[]

The filters.

##### update()

> **update**: (`id`: [`ID`](index.md#id-3), `options`: `object`) => `Promise`\<[`Filter`](index.md#filter)\>

Updates a filter.

###### Parameters

| Parameter | Type | Description |
| ------ | ------ | ------ |
| `id` | [`ID`](index.md#id-3) | The ID of the filter to update. |
| `options` | \{ `alias`: `string`; `name`: `string`; `query`: [`HTTPQL`](index.md#httpql); \} | Options for the filter. |
| `options.alias` | `string` | The alias of the filter. |
| `options.name` | `string` | The name of the filter. |
| `options.query` | [`HTTPQL`](index.md#httpql) | The HTTPQL query of the filter. |

###### Returns

`Promise`\<[`Filter`](index.md#filter)\>

The updated filter.

## Footer

### FooterSDK

> **FooterSDK**: `object`

Utilities to interact with the footer.

#### Type declaration

##### addToSlot

> **addToSlot**: [`DefineAddToSlotFn`](index.md#defineaddtoslotfntmap)\<[`FooterSlotContent`](index.md#footerslotcontent)\>

Add a component to a slot.

###### Param

The slot to add the component to.

###### Param

The content to add to the slot.

###### Example

```ts
addToSlot(FooterSlot.FooterSlotPrimary, {
  kind: "Command",
  commandId: "my-command",
  icon: "my-icon",
});

addToSlot(FooterSlot.FooterSlotPrimary, {
  kind: "Button",
  label: "My button",
  icon: "fas fa-rocket",
  onClick: () => {
    console.log("Button clicked");
  },
});

addToSlot(FooterSlot.FooterSlotSecondary, {
  kind: "Custom",
  component: MyComponent,
});
```

## Intercept

### InterceptSDK

> **InterceptSDK**: `object`

Utilities to interact with the Intercept page.

#### Type declaration

##### addRequestViewMode()

> **addRequestViewMode**: (`options`: [`RequestViewModeOptions`](index.md#requestviewmodeoptions)) => `void`

Add a custom request view mode.

###### Parameters

| Parameter | Type | Description |
| ------ | ------ | ------ |
| `options` | [`RequestViewModeOptions`](index.md#requestviewmodeoptions) | The view mode options. |

###### Returns

`void`

##### getScopeId()

> **getScopeId**: () => [`ID`](index.md#id-3) \| `undefined`

Get the current scope ID.

###### Returns

[`ID`](index.md#id-3) \| `undefined`

The current scope ID.

##### setScope()

> **setScope**: (`id`: [`ID`](index.md#id-3) \| `undefined`) => `void`

Set the current scope.

###### Parameters

| Parameter | Type |
| ------ | ------ |
| `id` | [`ID`](index.md#id-3) \| `undefined` |

###### Returns

`void`

## Log

### LogSDK

> **LogSDK**: `object`

Utilities to log messages to the console.

#### Type declaration

##### debug()

> **debug**: (...`data`: `unknown`[]) => `void`

Log debug message with variable arguments

###### Parameters

| Parameter | Type |
| ------ | ------ |
| ...`data` | `unknown`[] |

###### Returns

`void`

##### error()

> **error**: (...`data`: `unknown`[]) => `void`

Log error message with variable arguments

###### Parameters

| Parameter | Type |
| ------ | ------ |
| ...`data` | `unknown`[] |

###### Returns

`void`

##### info()

> **info**: (...`data`: `unknown`[]) => `void`

Log info message with variable arguments

###### Parameters

| Parameter | Type |
| ------ | ------ |
| ...`data` | `unknown`[] |

###### Returns

`void`

##### warn()

> **warn**: (...`data`: `unknown`[]) => `void`

Log warning message with variable arguments

###### Parameters

| Parameter | Type |
| ------ | ------ |
| ...`data` | `unknown`[] |

###### Returns

`void`

## Match and Replace

### MatchReplaceCollection

> **MatchReplaceCollection**: `object`

A collection in Match and Replace.

#### Type declaration

##### id

> **id**: [`ID`](index.md#id-3)

##### name

> **name**: `string`

##### ruleIds

> **ruleIds**: [`ID`](index.md#id-3)[]

***

### MatchReplaceMatcherRaw

> **MatchReplaceMatcherRaw**: [`MatchReplaceMatcherRawRegex`](index.md#matchreplacematcherrawregex) \| [`MatchReplaceMatcherRawValue`](index.md#matchreplacematcherrawvalue) \| [`MatchReplaceMatcherRawFull`](index.md#matchreplacematcherrawfull)

A matcher for raw operations in Match and Replace.

***

### MatchReplaceMatcherRawFull

> **MatchReplaceMatcherRawFull**: `object`

This matcher will match the entire section.

#### Type declaration

##### kind

> **kind**: `"MatcherRawFull"`

***

### MatchReplaceMatcherRawRegex

> **MatchReplaceMatcherRawRegex**: `object`

This matcher will match using a regex over the section.

#### Type declaration

##### kind

> **kind**: `"MatcherRawRegex"`

##### regex

> **regex**: `string`

***

### MatchReplaceMatcherRawValue

> **MatchReplaceMatcherRawValue**: `object`

This matcher will match the value if present in the section.

#### Type declaration

##### kind

> **kind**: `"MatcherRawValue"`

##### value

> **value**: `string`

***

### MatchReplaceOperationBody

> **MatchReplaceOperationBody**: [`KeepOperation`](index.md#keepoperationt)\<[`MatchReplaceOperationBodyRaw`](index.md#matchreplaceoperationbodyraw)\>

An operation for the body section.

***

### MatchReplaceOperationBodyRaw

> **MatchReplaceOperationBodyRaw**: `object`

A raw operation for the body section.

#### Type declaration

##### kind

> **kind**: `"OperationBodyRaw"`

##### matcher

> **matcher**: [`MatchReplaceMatcherRaw`](index.md#matchreplacematcherraw)

##### replacer

> **replacer**: [`MatchReplaceReplacer`](index.md#matchreplacereplacer)

***

### MatchReplaceOperationFirstLineRaw

> **MatchReplaceOperationFirstLineRaw**: `object`

A raw operation for the request first line.

#### Type declaration

##### kind

> **kind**: `"OperationFirstLineRaw"`

##### matcher

> **matcher**: [`MatchReplaceMatcherRaw`](index.md#matchreplacematcherraw)

##### replacer

> **replacer**: [`MatchReplaceReplacer`](index.md#matchreplacereplacer)

***

### MatchReplaceOperationHeader

> **MatchReplaceOperationHeader**: [`MatchReplaceOperationHeaderRaw`](index.md#matchreplaceoperationheaderraw) \| [`MatchReplaceOperationHeaderAdd`](index.md#matchreplaceoperationheaderadd) \| [`MatchReplaceOperationHeaderRemove`](index.md#matchreplaceoperationheaderremove) \| [`MatchReplaceOperationHeaderUpdate`](index.md#matchreplaceoperationheaderupdate)

An operation for the header section.

***

### MatchReplaceReplacer

> **MatchReplaceReplacer**: [`MatchReplaceReplacerTerm`](index.md#matchreplacereplacerterm) \| [`MatchReplaceReplacerWorkflow`](index.md#matchreplacereplacerworkflow)

A replacer in Match and Replace.

***

### MatchReplaceReplacerTerm

> **MatchReplaceReplacerTerm**: `object`

A replacer that replaces with a term.
If the matcher is a regex, groups will be interpolated.

#### Type declaration

##### kind

> **kind**: `"ReplacerTerm"`

##### term

> **term**: `string`

***

### MatchReplaceReplacerWorkflow

> **MatchReplaceReplacerWorkflow**: `object`

A replacer that replaces with the result of a workflow.
The input of the workflow depends on the operation and matcher.

#### Type declaration

##### kind

> **kind**: `"ReplacerWorkflow"`

##### workflowId

> **workflowId**: [`ID`](index.md#id-3)

***

### MatchReplaceRule

> **MatchReplaceRule**: `object`

A rule in Match and Replace.

#### Type declaration

##### collectionId

> **collectionId**: [`ID`](index.md#id-3)

The ID of the collection the rule belongs to.

##### id

> **id**: [`ID`](index.md#id-3)

The ID of the rule.

##### isEnabled

> **isEnabled**: `boolean`

Whether the rule is enabled.

##### name

> **name**: `string`

The name of the rule.

##### query

> **query**: [`HTTPQL`](index.md#httpql)

The HTTPQL query to match the rule against.
Only requests that match the query will be affected by the rule.

##### section

> **section**: [`MatchReplaceSection`](index.md#matchreplacesection)

The section of the rule.

***

### MatchReplaceSDK

> **MatchReplaceSDK**: `object`

Utilities to interact with the Match and Replace page.

#### Type declaration

##### createCollection()

> **createCollection**: (`options`: `object`) => `Promise`\<[`MatchReplaceCollection`](index.md#matchreplacecollection)\>

Create a collection.

###### Parameters

| Parameter | Type | Description |
| ------ | ------ | ------ |
| `options` | \{ `name`: `string`; \} | The options for the collection. |
| `options.name` | `string` | The name of the collection. |

###### Returns

`Promise`\<[`MatchReplaceCollection`](index.md#matchreplacecollection)\>

##### createRule()

> **createRule**: (`options`: `object`) => `Promise`\<[`MatchReplaceRule`](index.md#matchreplacerule)\>

Create a rule.

###### Parameters

| Parameter | Type | Description |
| ------ | ------ | ------ |
| `options` | \{ `collectionId`: [`ID`](index.md#id-3); `name`: `string`; `query`: [`HTTPQL`](index.md#httpql); `section`: [`MatchReplaceSection`](index.md#matchreplacesection); \} | The options for the rule. |
| `options.collectionId` | [`ID`](index.md#id-3) | The ID of the collection the rule belongs to. |
| `options.name` | `string` | The name of the rule. |
| `options.query` | [`HTTPQL`](index.md#httpql) | The HTTPQL query to match the rule against. |
| `options.section` | [`MatchReplaceSection`](index.md#matchreplacesection) | - |

###### Returns

`Promise`\<[`MatchReplaceRule`](index.md#matchreplacerule)\>

##### deleteCollection()

> **deleteCollection**: (`id`: [`ID`](index.md#id-3)) => `Promise`\<`void`\>

Delete a collection.

###### Parameters

| Parameter | Type | Description |
| ------ | ------ | ------ |
| `id` | [`ID`](index.md#id-3) | The ID of the collection. |

###### Returns

`Promise`\<`void`\>

##### deleteRule()

> **deleteRule**: (`id`: [`ID`](index.md#id-3)) => `Promise`\<`void`\>

Delete a rule.

###### Parameters

| Parameter | Type | Description |
| ------ | ------ | ------ |
| `id` | [`ID`](index.md#id-3) | The ID of the rule. |

###### Returns

`Promise`\<`void`\>

##### getActiveRules()

> **getActiveRules**: () => [`MatchReplaceRule`](index.md#matchreplacerule)[]

Get all active rules.
Rules are ordered in priority from highest to lowest.

###### Returns

[`MatchReplaceRule`](index.md#matchreplacerule)[]

All active rules.

##### getCollections()

> **getCollections**: () => [`MatchReplaceCollection`](index.md#matchreplacecollection)[]

Get all collections.

###### Returns

[`MatchReplaceCollection`](index.md#matchreplacecollection)[]

##### getRules()

> **getRules**: () => [`MatchReplaceRule`](index.md#matchreplacerule)[]

Get all rules.

###### Returns

[`MatchReplaceRule`](index.md#matchreplacerule)[]

All rules.

##### selectRule()

> **selectRule**: (`id`: [`ID`](index.md#id-3) \| `undefined`) => `void`

Select a rule to be displayed in the UI.

###### Parameters

| Parameter | Type | Description |
| ------ | ------ | ------ |
| `id` | [`ID`](index.md#id-3) \| `undefined` | The ID of the rule, or undefined to clear the selection. |

###### Returns

`void`

##### toggleRule()

> **toggleRule**: (`id`: [`ID`](index.md#id-3), `enabled`: `boolean`) => `Promise`\<`void`\>

Toggle a rule.

###### Parameters

| Parameter | Type | Description |
| ------ | ------ | ------ |
| `id` | [`ID`](index.md#id-3) | The ID of the rule. |
| `enabled` | `boolean` | Whether the rule should be enabled. |

###### Returns

`Promise`\<`void`\>

##### updateCollection()

> **updateCollection**: (`id`: [`ID`](index.md#id-3), `options`: `object`) => `Promise`\<[`MatchReplaceCollection`](index.md#matchreplacecollection)\>

Update a collection.

###### Parameters

| Parameter | Type | Description |
| ------ | ------ | ------ |
| `id` | [`ID`](index.md#id-3) | The ID of the collection. |
| `options` | \{ `name`: `string`; \} | The new values for the collection. |
| `options.name` | `string` | The new name of the collection. |

###### Returns

`Promise`\<[`MatchReplaceCollection`](index.md#matchreplacecollection)\>

##### updateRule()

> **updateRule**: (`id`: [`ID`](index.md#id-3), `options`: `object`) => `Promise`\<[`MatchReplaceRule`](index.md#matchreplacerule)\>

Update a rule.

###### Parameters

| Parameter | Type | Description |
| ------ | ------ | ------ |
| `id` | [`ID`](index.md#id-3) | The ID of the rule. |
| `options` | \{ `name`: `string`; `query`: [`HTTPQL`](index.md#httpql); `section`: [`MatchReplaceSection`](index.md#matchreplacesection); \} | The new values for the rule. |
| `options.name` | `string` | The new name of the rule. |
| `options.query`? | [`HTTPQL`](index.md#httpql) | The new HTTPQL query of the rule. |
| `options.section` | [`MatchReplaceSection`](index.md#matchreplacesection) | The new section of the rule. |

###### Returns

`Promise`\<[`MatchReplaceRule`](index.md#matchreplacerule)\>

***

### MatchReplaceSectionRequestFirstLine

> **MatchReplaceSectionRequestFirstLine**: `object`

A section for the request first line.

#### Type declaration

##### kind

> **kind**: `"SectionRequestFirstLine"`

##### operation

> **operation**: [`MatchReplaceOperationFirstLine`](index.md#matchreplaceoperationfirstline)

***

### MatchReplaceSectionResponseFirstLine

> **MatchReplaceSectionResponseFirstLine**: `object`

A section for the response first line.

#### Type declaration

##### kind

> **kind**: `"SectionResponseFirstLine"`

##### operation

> **operation**: [`MatchReplaceOperationFirstLine`](index.md#matchreplaceoperationfirstline)

## Other

### As\<TType\>

> **As**\<`TType`\>: `object`

#### Type Parameters

| Type Parameter |
| ------ |
| `TType` *extends* `string` |

#### Type declaration

##### type

> **type**: `TType`

***

### ButtonSlotContent

> **ButtonSlotContent**: [`DefineSlotContent`](index.md#defineslotcontentttype-p)\<`"Button"`, \{ `icon`: `string`; `label`: `string`; `onClick`: () => `void`; \}\>

***

### CommandID

> **CommandID**: `string` & `object`

A unique command identifier.

#### Type declaration

##### \_\_commandId?

> `optional` **\_\_commandId**: `never`

#### Example

```ts
"my-super-command"
```

***

### CommandSlotContent

> **CommandSlotContent**: [`DefineSlotContent`](index.md#defineslotcontentttype-p)\<`"Command"`, \{ `commandId`: [`CommandID`](index.md#commandid); `icon`: `string`; \}\>

***

### ComponentDefinition

> **ComponentDefinition**: `object`

A custom component that will be rendered in the UI.

#### Type declaration

##### component

> **component**: `VueComponent`

##### events?

> `optional` **events**: `Record`\<`string`, (...`args`: `unknown`[]) => `void`\>

##### props?

> `optional` **props**: `Record`\<`string`, `unknown`\>

***

### CustomSlotContent

> **CustomSlotContent**: [`DefineSlotContent`](index.md#defineslotcontentttype-p)\<`"Custom"`, \{ `definition`: [`ComponentDefinition`](index.md#componentdefinition); \}\>

***

### DefineAddToSlotFn()\<TMap\>

> **DefineAddToSlotFn**\<`TMap`\>: \<`K`\>(`slot`: `K`, `spec`: `TMap`\[`K`\]) => `void`

#### Type Parameters

| Type Parameter |
| ------ |
| `TMap` *extends* `Record`\<`string`, [`DefineSlotContent`](index.md#defineslotcontentttype-p)\<`string`, `Record`\<`string`, `unknown`\>\>\> |

#### Type Parameters

| Type Parameter |
| ------ |
| `K` *extends* `string` \| `number` \| `symbol` |

#### Parameters

| Parameter | Type |
| ------ | ------ |
| `slot` | `K` |
| `spec` | `TMap`\[`K`\] |

#### Returns

`void`

***

### DefineSlotContent\<TType, P\>

> **DefineSlotContent**\<`TType`, `P`\>: [`Prettify`](index.md#prettifyt)\<`object` & `P`\>

#### Type Parameters

| Type Parameter |
| ------ |
| `TType` *extends* `string` |
| `P` *extends* `Record`\<`string`, `unknown`\> |

***

### Dialog

> **Dialog**: `object`

#### Type declaration

##### close()

> **close**: () => `void`

###### Returns

`void`

***

### DialogOptions

> **DialogOptions**: `object`

#### Type declaration

##### closable?

> `optional` **closable**: `boolean`

##### closeOnEscape?

> `optional` **closeOnEscape**: `boolean`

##### draggable?

> `optional` **draggable**: `boolean`

##### modal?

> `optional` **modal**: `boolean`

##### position?

> `optional` **position**: `"left"` \| `"right"` \| `"top"` \| `"bottom"` \| `"center"` \| `"topleft"` \| `"topright"` \| `"bottomleft"` \| `"bottomright"`

##### title?

> `optional` **title**: `string`

***

### Editor

> **Editor**: `object`

Generic editor interface.

#### Type declaration

##### focus()

> **focus**: () => `void`

Focus the editor.

###### Returns

`void`

##### getEditorView()

> **getEditorView**: () => `EditorView`

Get the editor view.

###### Returns

`EditorView`

The CodeMirror [EditorView](https://codemirror.net/docs/ref/#view.EditorView).

##### getSelectedText()

> **getSelectedText**: () => `string`

Get the currently selected text of the editor.

###### Returns

`string`

##### isReadOnly()

> **isReadOnly**: () => `boolean`

Check whether the editor is read-only.

###### Returns

`boolean`

Whether the editor is read-only.

##### replaceSelectedText()

> **replaceSelectedText**: (`text`: `string`) => `void`

Replace the currently selected text of the editor.

###### Parameters

| Parameter | Type | Description |
| ------ | ------ | ------ |
| `text` | `string` | The text to replace the selection with. |

###### Returns

`void`

***

### EnvironmentVariable

> **EnvironmentVariable**: `object`

#### Type declaration

##### isSecret

> **isSecret**: `boolean`

Whether the environment variable is a secret.

##### name

> **name**: `string`

The name of the environment variable.

##### value

> **value**: `string`

The value of the environment variable.

***

### FooterSlot

> **FooterSlot**: *typeof* [`FooterSlot`](index.md#footerslot-1)\[keyof *typeof* [`FooterSlot`](index.md#footerslot-1)\]

***

### FooterSlotContent

> **FooterSlotContent**: `object`

#### Type declaration

##### footer-primary

> **footer-primary**: [`ButtonSlotContent`](index.md#buttonslotcontent) \| [`CustomSlotContent`](index.md#customslotcontent) \| [`CommandSlotContent`](index.md#commandslotcontent)

##### footer-secondary

> **footer-secondary**: [`ButtonSlotContent`](index.md#buttonslotcontent) \| [`CustomSlotContent`](index.md#customslotcontent) \| [`CommandSlotContent`](index.md#commandslotcontent)

***

### HTTPQL

> **HTTPQL**: `string` & `object`

An HTTPQL expression.

#### Type declaration

##### \_\_httpql?

> `optional` **\_\_httpql**: `never`

#### Example

```ts
`req.method.eq:"POST"`
```

***

### HTTPRequestEditor

> **HTTPRequestEditor**: `object`

#### Type declaration

##### getEditorView()

> **getEditorView**: () => `EditorView`

Get the editor view.

###### Returns

`EditorView`

The CodeMirror [EditorView](https://codemirror.net/docs/ref/#view.EditorView).

##### getElement()

> **getElement**: () => `HTMLElement`

Get the editor element.
Append this to your DOM to display the editor.

###### Returns

`HTMLElement`

The editor element.

***

### HTTPResponseEditor

> **HTTPResponseEditor**: `object`

#### Type declaration

##### getEditorView()

> **getEditorView**: () => `EditorView`

Get the editor view.

###### Returns

`EditorView`

The CodeMirror [EditorView](https://codemirror.net/docs/ref/#view.EditorView).

##### getElement()

> **getElement**: () => `HTMLElement`

Get the editor element.
Append this to your DOM to display the editor.

###### Returns

`HTMLElement`

The editor element.

***

### Icon

> **Icon**: `string` & `object`

A [https://fontawesome.com/icons\|FontAwesome](https://fontawesome.com/icons|FontAwesome) icon class.

#### Type declaration

##### \_\_icon?

> `optional` **\_\_icon**: `never`

#### Example

```ts
"fas fa-rocket"
```

***

### ID

> **ID**: `string` & `object`

A unique Caido identifier per type.

#### Type declaration

##### \_\_id?

> `optional` **\_\_id**: `never`

***

### JSONCompatible\<T\>

> **JSONCompatible**\<`T`\>: `unknown` *extends* `T` ? `never` : `{ [P in keyof T]: T[P] extends JSONValue ? T[P] : T[P] extends NotAssignableToJson ? never : JSONCompatible<T[P]> }`

#### Type Parameters

| Type Parameter |
| ------ |
| `T` |

***

### JSONPrimitive

> **JSONPrimitive**: `string` \| `number` \| `boolean` \| `null` \| `undefined`

***

### JSONValue

> **JSONValue**: [`JSONPrimitive`](index.md#jsonprimitive) \| [`JSONValue`](index.md#jsonvalue)[] \| \{\}

***

### KeepOperation\<T\>

> **KeepOperation**\<`T`\>: `T` & `object`

#### Type declaration

##### \_\_operation?

> `optional` **\_\_operation**: `never`

#### Type Parameters

| Type Parameter |
| ------ |
| `T` |

***

### ListenerHandle

> **ListenerHandle**: `object`

A handle for a listener.

#### Type declaration

##### stop()

> **stop**: () => `void`

Stop the listener.

###### Returns

`void`

***

### MatchReplaceMatcherName

> **MatchReplaceMatcherName**: `object`

#### Type declaration

##### kind

> **kind**: `"MatcherName"`

##### name

> **name**: `string`

***

### MatchReplaceOperationAll

> **MatchReplaceOperationAll**: [`KeepOperation`](index.md#keepoperationt)\<[`MatchReplaceOperationAllRaw`](index.md#matchreplaceoperationallraw)\>

***

### MatchReplaceOperationAllRaw

> **MatchReplaceOperationAllRaw**: `object`

#### Type declaration

##### kind

> **kind**: `"OperationAllRaw"`

##### matcher

> **matcher**: [`MatchReplaceMatcherRaw`](index.md#matchreplacematcherraw)

##### replacer

> **replacer**: [`MatchReplaceReplacer`](index.md#matchreplacereplacer)

***

### MatchReplaceOperationFirstLine

> **MatchReplaceOperationFirstLine**: [`KeepOperation`](index.md#keepoperationt)\<[`MatchReplaceOperationFirstLineRaw`](index.md#matchreplaceoperationfirstlineraw)\>

***

### MatchReplaceOperationHeaderAdd

> **MatchReplaceOperationHeaderAdd**: `object`

#### Type declaration

##### kind

> **kind**: `"OperationHeaderAdd"`

##### matcher

> **matcher**: [`MatchReplaceMatcherName`](index.md#matchreplacematchername)

##### replacer

> **replacer**: [`MatchReplaceReplacer`](index.md#matchreplacereplacer)

***

### MatchReplaceOperationHeaderRaw

> **MatchReplaceOperationHeaderRaw**: `object`

#### Type declaration

##### kind

> **kind**: `"OperationHeaderRaw"`

##### matcher

> **matcher**: [`MatchReplaceMatcherRaw`](index.md#matchreplacematcherraw)

##### replacer

> **replacer**: [`MatchReplaceReplacer`](index.md#matchreplacereplacer)

***

### MatchReplaceOperationHeaderRemove

> **MatchReplaceOperationHeaderRemove**: `object`

#### Type declaration

##### kind

> **kind**: `"OperationHeaderRemove"`

##### matcher

> **matcher**: [`MatchReplaceMatcherName`](index.md#matchreplacematchername)

***

### MatchReplaceOperationHeaderUpdate

> **MatchReplaceOperationHeaderUpdate**: `object`

#### Type declaration

##### kind

> **kind**: `"OperationHeaderUpdate"`

##### matcher

> **matcher**: [`MatchReplaceMatcherName`](index.md#matchreplacematchername)

##### replacer

> **replacer**: [`MatchReplaceReplacer`](index.md#matchreplacereplacer)

***

### MatchReplaceOperationMethod

> **MatchReplaceOperationMethod**: [`KeepOperation`](index.md#keepoperationt)\<[`MatchReplaceOperationMethodUpdate`](index.md#matchreplaceoperationmethodupdate)\>

***

### MatchReplaceOperationMethodUpdate

> **MatchReplaceOperationMethodUpdate**: `object`

#### Type declaration

##### kind

> **kind**: `"OperationMethodUpdate"`

##### replacer

> **replacer**: [`MatchReplaceReplacer`](index.md#matchreplacereplacer)

***

### MatchReplaceOperationPath

> **MatchReplaceOperationPath**: [`KeepOperation`](index.md#keepoperationt)\<[`MatchReplaceOperationPathRaw`](index.md#matchreplaceoperationpathraw)\>

***

### MatchReplaceOperationPathRaw

> **MatchReplaceOperationPathRaw**: `object`

#### Type declaration

##### kind

> **kind**: `"OperationPathRaw"`

##### matcher

> **matcher**: [`MatchReplaceMatcherRaw`](index.md#matchreplacematcherraw)

##### replacer

> **replacer**: [`MatchReplaceReplacer`](index.md#matchreplacereplacer)

***

### MatchReplaceOperationQuery

> **MatchReplaceOperationQuery**: [`MatchReplaceOperationQueryRaw`](index.md#matchreplaceoperationqueryraw) \| [`MatchReplaceOperationQueryAdd`](index.md#matchreplaceoperationqueryadd) \| [`MatchReplaceOperationQueryRemove`](index.md#matchreplaceoperationqueryremove) \| [`MatchReplaceOperationQueryUpdate`](index.md#matchreplaceoperationqueryupdate)

***

### MatchReplaceOperationQueryAdd

> **MatchReplaceOperationQueryAdd**: `object`

#### Type declaration

##### kind

> **kind**: `"OperationQueryAdd"`

##### matcher

> **matcher**: [`MatchReplaceMatcherName`](index.md#matchreplacematchername)

##### replacer

> **replacer**: [`MatchReplaceReplacer`](index.md#matchreplacereplacer)

***

### MatchReplaceOperationQueryRaw

> **MatchReplaceOperationQueryRaw**: `object`

#### Type declaration

##### kind

> **kind**: `"OperationQueryRaw"`

##### matcher

> **matcher**: [`MatchReplaceMatcherRaw`](index.md#matchreplacematcherraw)

##### replacer

> **replacer**: [`MatchReplaceReplacer`](index.md#matchreplacereplacer)

***

### MatchReplaceOperationQueryRemove

> **MatchReplaceOperationQueryRemove**: `object`

#### Type declaration

##### kind

> **kind**: `"OperationQueryRemove"`

##### matcher

> **matcher**: [`MatchReplaceMatcherName`](index.md#matchreplacematchername)

***

### MatchReplaceOperationQueryUpdate

> **MatchReplaceOperationQueryUpdate**: `object`

#### Type declaration

##### kind

> **kind**: `"OperationQueryUpdate"`

##### matcher

> **matcher**: [`MatchReplaceMatcherName`](index.md#matchreplacematchername)

##### replacer

> **replacer**: [`MatchReplaceReplacer`](index.md#matchreplacereplacer)

***

### MatchReplaceOperationStatusCode

> **MatchReplaceOperationStatusCode**: [`KeepOperation`](index.md#keepoperationt)\<[`MatchReplaceOperationStatusCodeUpdate`](index.md#matchreplaceoperationstatuscodeupdate)\>

***

### MatchReplaceOperationStatusCodeUpdate

> **MatchReplaceOperationStatusCodeUpdate**: `object`

#### Type declaration

##### kind

> **kind**: `"OperationStatusCodeUpdate"`

##### replacer

> **replacer**: [`MatchReplaceReplacer`](index.md#matchreplacereplacer)

***

### MatchReplaceSection

> **MatchReplaceSection**: [`MatchReplaceSectionRequestAll`](index.md#matchreplacesectionrequestall) \| [`MatchReplaceSectionRequestBody`](index.md#matchreplacesectionrequestbody) \| [`MatchReplaceSectionRequestFirstLine`](index.md#matchreplacesectionrequestfirstline) \| [`MatchReplaceSectionRequestHeader`](index.md#matchreplacesectionrequestheader) \| [`MatchReplaceSectionRequestMethod`](index.md#matchreplacesectionrequestmethod) \| [`MatchReplaceSectionRequestPath`](index.md#matchreplacesectionrequestpath) \| [`MatchReplaceSectionRequestQuery`](index.md#matchreplacesectionrequestquery) \| [`MatchReplaceSectionResponseAll`](index.md#matchreplacesectionresponseall) \| [`MatchReplaceSectionResponseBody`](index.md#matchreplacesectionresponsebody) \| [`MatchReplaceSectionResponseFirstLine`](index.md#matchreplacesectionresponsefirstline) \| [`MatchReplaceSectionResponseHeader`](index.md#matchreplacesectionresponseheader) \| [`MatchReplaceSectionResponseStatusCode`](index.md#matchreplacesectionresponsestatuscode)

***

### MatchReplaceSectionRequestAll

> **MatchReplaceSectionRequestAll**: `object`

#### Type declaration

##### kind

> **kind**: `"SectionRequestAll"`

##### operation

> **operation**: [`MatchReplaceOperationAll`](index.md#matchreplaceoperationall)

***

### MatchReplaceSectionRequestBody

> **MatchReplaceSectionRequestBody**: `object`

#### Type declaration

##### kind

> **kind**: `"SectionRequestBody"`

##### operation

> **operation**: [`MatchReplaceOperationBody`](index.md#matchreplaceoperationbody)

***

### MatchReplaceSectionRequestHeader

> **MatchReplaceSectionRequestHeader**: `object`

#### Type declaration

##### kind

> **kind**: `"SectionRequestHeader"`

##### operation

> **operation**: [`MatchReplaceOperationHeader`](index.md#matchreplaceoperationheader)

***

### MatchReplaceSectionRequestMethod

> **MatchReplaceSectionRequestMethod**: `object`

#### Type declaration

##### kind

> **kind**: `"SectionRequestMethod"`

##### operation

> **operation**: [`MatchReplaceOperationMethod`](index.md#matchreplaceoperationmethod)

***

### MatchReplaceSectionRequestPath

> **MatchReplaceSectionRequestPath**: `object`

#### Type declaration

##### kind

> **kind**: `"SectionRequestPath"`

##### operation

> **operation**: [`MatchReplaceOperationPath`](index.md#matchreplaceoperationpath)

***

### MatchReplaceSectionRequestQuery

> **MatchReplaceSectionRequestQuery**: `object`

#### Type declaration

##### kind

> **kind**: `"SectionRequestQuery"`

##### operation

> **operation**: [`MatchReplaceOperationQuery`](index.md#matchreplaceoperationquery)

***

### MatchReplaceSectionResponseAll

> **MatchReplaceSectionResponseAll**: `object`

#### Type declaration

##### kind

> **kind**: `"SectionResponseAll"`

##### operation

> **operation**: [`MatchReplaceOperationAll`](index.md#matchreplaceoperationall)

***

### MatchReplaceSectionResponseBody

> **MatchReplaceSectionResponseBody**: `object`

#### Type declaration

##### kind

> **kind**: `"SectionResponseBody"`

##### operation

> **operation**: [`MatchReplaceOperationBody`](index.md#matchreplaceoperationbody)

***

### MatchReplaceSectionResponseHeader

> **MatchReplaceSectionResponseHeader**: `object`

#### Type declaration

##### kind

> **kind**: `"SectionResponseHeader"`

##### operation

> **operation**: [`MatchReplaceOperationHeader`](index.md#matchreplaceoperationheader)

***

### MatchReplaceSectionResponseStatusCode

> **MatchReplaceSectionResponseStatusCode**: `object`

#### Type declaration

##### kind

> **kind**: `"SectionResponseStatusCode"`

##### operation

> **operation**: [`MatchReplaceOperationStatusCode`](index.md#matchreplaceoperationstatuscode)

***

### NotAssignableToJson

> **NotAssignableToJson**: `bigint` \| `symbol` \| `Function`

***

### OnCreatedWorkflowCallback()

> **OnCreatedWorkflowCallback**: (`event`: `object`) => `void`

#### Parameters

| Parameter | Type |
| ------ | ------ |
| `event` | \{ `workflow`: [`Workflow`](index.md#workflow); \} |
| `event.workflow` | [`Workflow`](index.md#workflow) |

#### Returns

`void`

***

### OnDeletedWorkflowCallback()

> **OnDeletedWorkflowCallback**: (`event`: `object`) => `void`

#### Parameters

| Parameter | Type |
| ------ | ------ |
| `event` | \{ `id`: [`ID`](index.md#id-3); \} |
| `event.id` | [`ID`](index.md#id-3) |

#### Returns

`void`

***

### OnUpdatedWorkflowCallback()

> **OnUpdatedWorkflowCallback**: (`event`: `object`) => `void`

#### Parameters

| Parameter | Type |
| ------ | ------ |
| `event` | \{ `workflow`: [`Workflow`](index.md#workflow); \} |
| `event.workflow` | [`Workflow`](index.md#workflow) |

#### Returns

`void`

***

### PageChangeEvent

> **PageChangeEvent**: \{ `path`: `string`; `routeId`: [`Routes`](index.md#routes); `type`: `"Core"`; \} \| \{ `path`: `string`; `type`: `"Plugin"`; \}

***

### Prettify\<T\>

> **Prettify**\<`T`\>: `{ [K in keyof T]: T[K] }` & `object`

#### Type Parameters

| Type Parameter |
| ------ |
| `T` |

***

### PromisifiedReturnType\<T\>

> **PromisifiedReturnType**\<`T`\>: `ReturnType`\<`T`\> *extends* `Promise`\<infer U\> ? `Promise`\<`U`\> : `Promise`\<`ReturnType`\<`T`\>\>

#### Type Parameters

| Type Parameter |
| ------ |
| `T` *extends* (...`args`: `unknown`[]) => `unknown` |

***

### ReplaySlot

> **ReplaySlot**: *typeof* [`ReplaySlot`](index.md#replayslot-1)\[keyof *typeof* [`ReplaySlot`](index.md#replayslot-1)\]

***

### ReplaySlotContent

> **ReplaySlotContent**: `object`

#### Type declaration

##### session-toolbar-primary

> **session-toolbar-primary**: [`ButtonSlotContent`](index.md#buttonslotcontent) \| [`CustomSlotContent`](index.md#customslotcontent) \| [`CommandSlotContent`](index.md#commandslotcontent)

##### session-toolbar-secondary

> **session-toolbar-secondary**: [`ButtonSlotContent`](index.md#buttonslotcontent) \| [`CustomSlotContent`](index.md#customslotcontent) \| [`CommandSlotContent`](index.md#commandslotcontent)

##### topbar

> **topbar**: [`ButtonSlotContent`](index.md#buttonslotcontent) \| [`CustomSlotContent`](index.md#customslotcontent) \| [`CommandSlotContent`](index.md#commandslotcontent)

***

### RequestDraft

> **RequestDraft**: [`Prettify`](index.md#prettifyt)\<[`As`](index.md#asttype)\<`"RequestDraft"`\> & `object`\>

***

### RequestFull

> **RequestFull**: [`Prettify`](index.md#prettifyt)\<[`As`](index.md#asttype)\<`"RequestFull"`\> & `object`\>

***

### RequestMeta

> **RequestMeta**: [`Prettify`](index.md#prettifyt)\<[`As`](index.md#asttype)\<`"RequestMeta"`\> & `object`\>

***

### RequestViewModeOptions

> **RequestViewModeOptions**: `object`

#### Type declaration

##### label

> **label**: `string`

The label of the view mode.

##### view

> **view**: [`ComponentDefinition`](index.md#componentdefinition)

The component to render when the view mode is selected.

***

### Routes

> **Routes**: *typeof* [`Routes`](index.md#routes-1)\[keyof *typeof* [`Routes`](index.md#routes-1)\]

***

### SlotContent

> **SlotContent**: [`ButtonSlotContent`](index.md#buttonslotcontent) \| [`CustomSlotContent`](index.md#customslotcontent) \| [`CommandSlotContent`](index.md#commandslotcontent)

***

### FooterSlot

> `const` **FooterSlot**: `object`

#### Type declaration

##### FooterSlotPrimary

> `readonly` **FooterSlotPrimary**: `"footer-primary"`

##### FooterSlotSecondary

> `readonly` **FooterSlotSecondary**: `"footer-secondary"`

***

### Routes

> `const` **Routes**: `object`

#### Type declaration

##### About

> `readonly` **About**: `"About"`

##### Assistant

> `readonly` **Assistant**: `"Assistant"`

##### Automate

> `readonly` **Automate**: `"Automate"`

##### Backups

> `readonly` **Backups**: `"Backups"`

##### Certificate

> `readonly` **Certificate**: `"Certificate"`

##### Environment

> `readonly` **Environment**: `"Environment"`

##### Exports

> `readonly` **Exports**: `"Exports"`

##### Files

> `readonly` **Files**: `"Files"`

##### Filter

> `readonly` **Filter**: `"Filter"`

##### Findings

> `readonly` **Findings**: `"Findings"`

##### HTTPHistory

> `readonly` **HTTPHistory**: `"HTTPHistory"`

##### Intercept

> `readonly` **Intercept**: `"Intercept"`

##### MatchReplace

> `readonly` **MatchReplace**: `"Tamper"`

##### Plugins

> `readonly` **Plugins**: `"Plugins"`

##### Projects

> `readonly` **Projects**: `"Projects"`

##### Replay

> `readonly` **Replay**: `"Replay"`

##### Scope

> `readonly` **Scope**: `"Scope"`

##### Search

> `readonly` **Search**: `"Search"`

##### Settings

> `readonly` **Settings**: `"Settings"`

##### Sitemap

> `readonly` **Sitemap**: `"Sitemap"`

##### Websockets

> `readonly` **Websockets**: `"Websockets"`

##### Workflows

> `readonly` **Workflows**: `"Workflows"`

***

### API

Renames and re-exports [Caido](index.md#caidot-e)

## Projects

### ProjectsSDK

> **ProjectsSDK**: `object`

Utilities to interact with projects.

#### Type declaration

##### onCurrentProjectChange()

> **onCurrentProjectChange**: (`callback`: (`event`: [`SelectedProjectChangeEvent`](index.md#selectedprojectchangeevent)) => `void`) => [`ListenerHandle`](index.md#listenerhandle)

Subscribe to selected project changes.

###### Parameters

| Parameter | Type | Description |
| ------ | ------ | ------ |
| `callback` | (`event`: [`SelectedProjectChangeEvent`](index.md#selectedprojectchangeevent)) => `void` | The callback to call when the selected project changes. |

###### Returns

[`ListenerHandle`](index.md#listenerhandle)

An object with a `stop` method that can be called to stop listening to project changes.

###### Example

```ts
const handler = sdk.projects.onCurrentProjectChange((event) => {
  console.log('Selected project changed to:', event.projectId);
});

// Later, stop listening
handler.stop();
```

***

### SelectedProjectChangeEvent

> **SelectedProjectChangeEvent**: `object`

Event fired when the selected project changes.

#### Type declaration

##### projectId

> **projectId**: [`ID`](index.md#id-3) \| `undefined`

## Runtime

### RuntimeSDK

> **RuntimeSDK**: `object`

Utilities to interact with the runtime.

#### Type declaration

##### version

###### Get Signature

> **get** **version**(): `string`

Get the current version of Caido.

###### Returns

`string`

## Sitemap

### SitemapSDK

> **SitemapSDK**: `object`

Utilities to interact with the Sitemap page.

#### Type declaration

##### addRequestEditorExtension()

> **addRequestEditorExtension**: (`extension`: `Extension`) => `void`

Add an extension to the request editor.

###### Parameters

| Parameter | Type | Description |
| ------ | ------ | ------ |
| `extension` | `Extension` | The extension to add. |

###### Returns

`void`

##### addRequestViewMode()

> **addRequestViewMode**: (`options`: [`RequestViewModeOptions`](index.md#requestviewmodeoptions)) => `void`

Add a custom request view mode.

###### Parameters

| Parameter | Type | Description |
| ------ | ------ | ------ |
| `options` | [`RequestViewModeOptions`](index.md#requestviewmodeoptions) | The view mode options. |

###### Returns

`void`

##### getScopeId()

> **getScopeId**: () => [`ID`](index.md#id-3) \| `undefined`

Get the current scope ID.

###### Returns

[`ID`](index.md#id-3) \| `undefined`

The current scope ID.

##### setScope()

> **setScope**: (`id`: [`ID`](index.md#id-3) \| `undefined`) => `void`

Set the current scope.

###### Parameters

| Parameter | Type | Description |
| ------ | ------ | ------ |
| `id` | [`ID`](index.md#id-3) \| `undefined` | The ID of the scope to set. |

###### Returns

`void`

## Workflows

### Workflow

> **Workflow**: `object`

A workflow

#### Type declaration

##### description

> **description**: `string`

##### id

> **id**: `string`

##### kind

> **kind**: [`WorkflowKind`](index.md#workflowkind)

##### name

> **name**: `string`

***

### WorkflowKind

> **WorkflowKind**: `"Convert"` \| `"Active"` \| `"Passive"`

The kind of workflow.

***

### WorkflowSDK

> **WorkflowSDK**: `object`

Utilities to interact with workflows.

#### Type declaration

##### getWorkflows()

> **getWorkflows**: () => [`Workflow`](index.md#workflow)[]

Get all workflows.

###### Returns

[`Workflow`](index.md#workflow)[]

All workflows.

##### onCreatedWorkflow()

> **onCreatedWorkflow**: (`callback`: [`OnCreatedWorkflowCallback`](index.md#oncreatedworkflowcallback)) => [`ListenerHandle`](index.md#listenerhandle)

Register a callback to be called when a workflow is created.

###### Parameters

| Parameter | Type | Description |
| ------ | ------ | ------ |
| `callback` | [`OnCreatedWorkflowCallback`](index.md#oncreatedworkflowcallback) | The callback to be called. |

###### Returns

[`ListenerHandle`](index.md#listenerhandle)

##### onDeletedWorkflow()

> **onDeletedWorkflow**: (`callback`: [`OnDeletedWorkflowCallback`](index.md#ondeletedworkflowcallback)) => [`ListenerHandle`](index.md#listenerhandle)

Register a callback to be called when a workflow is deleted.

###### Parameters

| Parameter | Type | Description |
| ------ | ------ | ------ |
| `callback` | [`OnDeletedWorkflowCallback`](index.md#ondeletedworkflowcallback) | The callback to be called. |

###### Returns

[`ListenerHandle`](index.md#listenerhandle)

##### onUpdatedWorkflow()

> **onUpdatedWorkflow**: (`callback`: [`OnUpdatedWorkflowCallback`](index.md#onupdatedworkflowcallback)) => [`ListenerHandle`](index.md#listenerhandle)

Register a callback to be called when a workflow is updated.

###### Parameters

| Parameter | Type | Description |
| ------ | ------ | ------ |
| `callback` | [`OnUpdatedWorkflowCallback`](index.md#onupdatedworkflowcallback) | The callback to be called. |

###### Returns

[`ListenerHandle`](index.md#listenerhandle)



================================================
FILE: src/reference/sdks/workflow/index.md
================================================
# @caido/sdk-workflow

This is the reference for the workflow SDK used by JS Nodes.
[SDK](#sdk-1) is the main interface that provides access to various services and functionalities.

## SDK

### SDK

> **SDK**: `object`

The SDK object available to all scripts.

#### Type declaration

##### console

> **console**: [`Console`](index.md#console)

The console for logging.

This is currently the same as the global `console`.

##### env

> **env**: [`EnvironmentSDK`](index.md#environmentsdk)

The SDK for the Environment service.

##### findings

> **findings**: [`FindingsSDK`](index.md#findingssdk)

The SDK for the Findings service.

##### graphql

> **graphql**: [`GraphQLSDK`](index.md#graphqlsdk)

The SDK for the GraphQL service.

##### projects

> **projects**: [`ProjectsSDK`](index.md#projectssdk)

The SDK for the Projects service.

##### replay

> **replay**: [`ReplaySDK`](index.md#replaysdk)

The SDK for the Replay service.

##### requests

> **requests**: [`RequestsSDK`](index.md#requestssdk)

The SDK for the Requests service.

##### runtime

> **runtime**: [`RuntimeSDK`](index.md#runtimesdk)

The SDK for the runtime information.

##### scope

> **scope**: [`ScopeSDK`](index.md#scopesdk)

The SDK for the Scope service.

##### asString()

Converts bytes to a string.

Unprintable characters will be replaced with `�`.

###### Parameters

| Parameter | Type |
| ------ | ------ |
| `array` | [`Bytes`](index.md#bytes) |

###### Returns

`string`

###### Example

```js
export function run(input, sdk) {
  let parsed = sdk.asString(input);
  sdk.console.log(parsed);
  return parsed;
}
```

## Data

### BytesInput

> **BytesInput**: `number`[]

The input for the Javascript Nodes.

***

### ~~ConvertInput~~

> **ConvertInput**: [`BytesInput`](index.md#bytesinput)

#### Deprecated

Use BytesInput instead.

***

### Data

> **Data**: [`Bytes`](index.md#bytes)

The output for the Javascript Nodes.

***

### Decision

> **Decision**: `boolean`

The output for the If/Else Javascript Nodes.

***

### HttpInput

> **HttpInput**: `object`

The input for the HTTP Javascript Nodes

#### Type declaration

##### request

> **request**: [`Request`](index.md#request-2) \| `undefined`

##### response

> **response**: [`Response`](index.md#response-5) \| `undefined`

***

### ~~PassiveInput~~

> **PassiveInput**: [`HttpInput`](index.md#httpinput)

#### Deprecated

Use HttpInput instead.

## Requests

### Body

The body of a [Request](index.md#request-2) or [Response](index.md#response-5).

Calling `to<FORMAT>` will try to convert the body to the desired format.

#### Constructors

##### new Body()

> **new Body**(`data`: `string` \| `number`[] \| `Uint8Array`): [`Body`](index.md#body)

###### Parameters

| Parameter | Type |
| ------ | ------ |
| `data` | `string` \| `number`[] \| `Uint8Array` |

###### Returns

[`Body`](index.md#body)

#### Properties

##### length

> `readonly` **length**: `number`

The length of the body in bytes.

#### Methods

##### toJson()

> **toJson**(): `unknown`

Try to parse the body as JSON.

###### Returns

`unknown`

###### Throws

If the body is not valid JSON.

##### toRaw()

> **toRaw**(): `Uint8Array`

Get the raw body as an array of bytes.

###### Returns

`Uint8Array`

##### toText()

> **toText**(): `string`

Parse the body as a string.

Unprintable characters will be replaced with `�`.

###### Returns

`string`

***

### RequestSpec

A mutable Request that has not yet been sent.

#### Constructors

##### new RequestSpec()

> **new RequestSpec**(`url`: `string`): [`RequestSpec`](index.md#requestspec)

Build a new [RequestSpec](index.md#requestspec) from a URL string.
We try to infer as much information as possible from the URL, including the scheme, host, path and query.

You can convert a saved immutable [Request](index.md#request-2) object into a [RequestSpec](index.md#requestspec) object by using the `toSpec()` method.

By default:

- Method is `GET`.
- Path is `/`.

###### Parameters

| Parameter | Type |
| ------ | ------ |
| `url` | `string` |

###### Returns

[`RequestSpec`](index.md#requestspec)

###### Throws

If the URL is invalid.

###### Example

```js
const spec = new RequestSpec("https://example.com");
```

#### Methods

##### getBody()

> **getBody**(): `undefined` \| [`Body`](index.md#body)

The body of the request.

###### Returns

`undefined` \| [`Body`](index.md#body)

##### getHeader()

> **getHeader**(`name`: `string`): `undefined` \| `string`[]

Get a header value.

Header name is case-insensitive.
The header might have multiple values.

###### Parameters

| Parameter | Type |
| ------ | ------ |
| `name` | `string` |

###### Returns

`undefined` \| `string`[]

##### getHeaders()

> **getHeaders**(): `Record`\<`string`, `string`[]\>

The headers of the request.

Header names are case-insensitive.
Each header might have multiple values.

###### Returns

`Record`\<`string`, `string`[]\>

###### Example

```json
{
  "Host": ["caido.io"],
  "Connection": ["keep-alive"],
  "Content-Length": ["95"]
}
```

##### getHost()

> **getHost**(): `string`

Get the host of the request.

###### Returns

`string`

##### getMethod()

###### Call Signature

> **getMethod**(): `string`

Get the HTTP method of the request.

Get the raw version by passing `{ raw: true }` in the options.

###### Returns

`string`

###### Call Signature

> **getMethod**(`options`: [`RawOption`](index.md#rawoption)): `Uint8Array`

Get the HTTP method of the request.

Get the raw version by passing `{ raw: true }` in the options.

###### Parameters

| Parameter | Type |
| ------ | ------ |
| `options` | [`RawOption`](index.md#rawoption) |

###### Returns

`Uint8Array`

##### getPath()

###### Call Signature

> **getPath**(): `string`

Get the path of the request.

Get the raw version by passing `{ raw: true }` in the options.

###### Returns

`string`

###### Call Signature

> **getPath**(`options`: [`RawOption`](index.md#rawoption)): `Uint8Array`

Get the path of the request.

Get the raw version by passing `{ raw: true }` in the options.

###### Parameters

| Parameter | Type |
| ------ | ------ |
| `options` | [`RawOption`](index.md#rawoption) |

###### Returns

`Uint8Array`

##### getPort()

> **getPort**(): `number`

Get the port of the request.

###### Returns

`number`

##### getQuery()

###### Call Signature

> **getQuery**(): `string`

Get the unparsed query of the request.

Get the raw version by passing `{ raw: true }` in the options.

Excludes the leading `?`.

###### Returns

`string`

###### Call Signature

> **getQuery**(`options`: [`RawOption`](index.md#rawoption)): `Uint8Array`

Get the unparsed query of the request.

Get the raw version by passing `{ raw: true }` in the options.

Excludes the leading `?`.

###### Parameters

| Parameter | Type |
| ------ | ------ |
| `options` | [`RawOption`](index.md#rawoption) |

###### Returns

`Uint8Array`

##### getRaw()

> **getRaw**(): [`RequestSpecRaw`](index.md#requestspecraw)

This methods converts the [RequestSpec](index.md#requestspec) to a [RequestSpecRaw](index.md#requestspecraw).

This is useful to retrieve the raw bytes of the request.

###### Returns

[`RequestSpecRaw`](index.md#requestspecraw)

###### Example

```js
const spec = new RequestSpec("https://example.com");
const specRaw = spec.getRaw();
const bytes = specRaw.getRaw(); // GET / HTTP/1.1\r\nHost: example.com\r\n\r\n
```

##### getTls()

> **getTls**(): `boolean`

Get if the request uses TLS (HTTPS).

###### Returns

`boolean`

##### removeHeader()

> **removeHeader**(`name`: `string`): `void`

Removes a header.

###### Parameters

| Parameter | Type |
| ------ | ------ |
| `name` | `string` |

###### Returns

`void`

##### setBody()

> **setBody**(`body`: [`Bytes`](index.md#bytes) \| [`Body`](index.md#body), `options`?: [`SetBodyOptions`](index.md#setbodyoptions)): `void`

Set the body of the request.

The body can either be a [Body](index.md#body) or any type that can be converted to [Bytes](index.md#bytes).

###### Parameters

| Parameter | Type |
| ------ | ------ |
| `body` | [`Bytes`](index.md#bytes) \| [`Body`](index.md#body) |
| `options`? | [`SetBodyOptions`](index.md#setbodyoptions) |

###### Returns

`void`

###### Example

```js
const body = new Body("Hello world.");
const options = { updateContentLength: true };
request.setBody(body, options);
```

##### setHeader()

> **setHeader**(`name`: `string`, `value`: `string`): `void`

Set a header value.

This will overwrite any existing values.

###### Parameters

| Parameter | Type |
| ------ | ------ |
| `name` | `string` |
| `value` | `string` |

###### Returns

`void`

##### setHost()

> **setHost**(`host`: `string`): `void`

Set the host of the request.

It will also update the `Host` header.

###### Parameters

| Parameter | Type |
| ------ | ------ |
| `host` | `string` |

###### Returns

`void`

##### setMethod()

> **setMethod**(`method`: [`Bytes`](index.md#bytes)): `void`

Set the HTTP method of the request.

All strings are accepted.

###### Parameters

| Parameter | Type |
| ------ | ------ |
| `method` | [`Bytes`](index.md#bytes) |

###### Returns

`void`

##### setPath()

> **setPath**(`path`: [`Bytes`](index.md#bytes)): `void`

Set the path of the request.

###### Parameters

| Parameter | Type |
| ------ | ------ |
| `path` | [`Bytes`](index.md#bytes) |

###### Returns

`void`

##### setPort()

> **setPort**(`port`: `number`): `void`

Set the port of the request.

The port number must be between 1 and 65535.

###### Parameters

| Parameter | Type |
| ------ | ------ |
| `port` | `number` |

###### Returns

`void`

##### setQuery()

> **setQuery**(`query`: [`Bytes`](index.md#bytes)): `void`

Set the unparsed query of the request.

The query string should not include the leading `?`.

###### Parameters

| Parameter | Type |
| ------ | ------ |
| `query` | [`Bytes`](index.md#bytes) |

###### Returns

`void`

###### Example

```js
spec.setQuery("q=hello");
```

##### setRaw()

> **setRaw**(`raw`: [`Bytes`](index.md#bytes)): [`RequestSpecRaw`](index.md#requestspecraw)

This method sets the raw [Bytes](index.md#bytes) of the request and converts it to a [RequestSpecRaw](index.md#requestspecraw).

This is useful when you have a prepared [RequestSpec](index.md#requestspec) and you just want to modify the raw data.

###### Parameters

| Parameter | Type |
| ------ | ------ |
| `raw` | [`Bytes`](index.md#bytes) |

###### Returns

[`RequestSpecRaw`](index.md#requestspecraw)

###### Example

```js
const rawBytes = []; // RAW BYTES HERE
const request = new RequestSpec("https://example.com");
const rawRequest = request.setRaw(rawBytes);
```

##### setTls()

> **setTls**(`tls`: `boolean`): `void`

Set if the request uses TLS (HTTPS).

###### Parameters

| Parameter | Type |
| ------ | ------ |
| `tls` | `boolean` |

###### Returns

`void`

##### parse()

###### Call Signature

> `static` **parse**(`bytes`: [`Bytes`](index.md#bytes)): [`RequestSpec`](index.md#requestspec)

Parses raw bytes into a [RequestSpec](index.md#requestspec).

###### Parameters

| Parameter | Type |
| ------ | ------ |
| `bytes` | [`Bytes`](index.md#bytes) |

###### Returns

[`RequestSpec`](index.md#requestspec)

###### Throws

If the bytes are not a valid HTTP request.

###### Example

```js
const rawInput = 'GET / HTTP/1.1\r\nHost: example.com\r\n\r\n';
const spec = RequestSpec.parse(rawInput);
spec.setHeader('x-caido', 'test');
const specRaw = spec.getRaw();
const rawOutput = specRaw.getRaw(); // Will contain the new header
```

###### Call Signature

> `static` **parse**(`raw`: [`RequestSpecRaw`](index.md#requestspecraw)): [`RequestSpec`](index.md#requestspec)

Parses the raw bytes of a [RequestSpecRaw](index.md#requestspecraw) into a [RequestSpec](index.md#requestspec).

###### Parameters

| Parameter | Type |
| ------ | ------ |
| `raw` | [`RequestSpecRaw`](index.md#requestspecraw) |

###### Returns

[`RequestSpec`](index.md#requestspec)

###### Throws

If the bytes are not a valid HTTP request.

***

### RequestSpecRaw

A mutable raw Request that has not yet been sent.

#### Constructors

##### new RequestSpecRaw()

> **new RequestSpecRaw**(`url`: `string`): [`RequestSpecRaw`](index.md#requestspecraw)

Build a new [RequestSpecRaw](index.md#requestspecraw) from a URL string. Only the host, port and scheme will be parsed.

You can convert a saved immutable [Request](index.md#request-2) object into a [RequestSpecRaw](index.md#requestspecraw) object by using the `toSpecRaw()` method.

You MUST use `setRaw` to set the raw bytes of the request.

###### Parameters

| Parameter | Type |
| ------ | ------ |
| `url` | `string` |

###### Returns

[`RequestSpecRaw`](index.md#requestspecraw)

###### Example

```js
const spec = new RequestSpecRaw("https://example.com");
```

#### Methods

##### getHost()

> **getHost**(): `string`

Get the host of the request.

###### Returns

`string`

##### getPort()

> **getPort**(): `number`

Get the port of the request.

###### Returns

`number`

##### getRaw()

> **getRaw**(): `Uint8Array`

Get the raw bytes of the request.

###### Returns

`Uint8Array`

##### getSpec()

> **getSpec**(): [`RequestSpec`](index.md#requestspec)

This methods converts the [RequestSpecRaw](index.md#requestspecraw) to a [RequestSpec](index.md#requestspec).

###### Returns

[`RequestSpec`](index.md#requestspec)

###### Throws

If the bytes are not a valid HTTP request.

###### See

[RequestSpec.parse](index.md#parse)

##### getTls()

> **getTls**(): `boolean`

Get if the request uses TLS (HTTPS).

###### Returns

`boolean`

##### setHost()

> **setHost**(`host`: `string`): `void`

Set the host of the request.

It will NOT update the `Host` header.

###### Parameters

| Parameter | Type |
| ------ | ------ |
| `host` | `string` |

###### Returns

`void`

##### setPort()

> **setPort**(`port`: `number`): `void`

Set the port of the request.

The port number must be between 1 and 65535.

###### Parameters

| Parameter | Type |
| ------ | ------ |
| `port` | `number` |

###### Returns

`void`

##### setRaw()

> **setRaw**(`raw`: [`Bytes`](index.md#bytes)): `void`

Set the raw [Bytes](index.md#bytes) of the request.

###### Parameters

| Parameter | Type |
| ------ | ------ |
| `raw` | [`Bytes`](index.md#bytes) |

###### Returns

`void`

##### setTls()

> **setTls**(`tls`: `boolean`): `void`

Set if the request uses TLS (HTTPS).

###### Parameters

| Parameter | Type |
| ------ | ------ |
| `tls` | `boolean` |

###### Returns

`void`

***

### Request

> **Request**: `object`

An immutable saved Request.

To modify, use `toSpec` to get a `RequestSpec` object.

#### Type declaration

##### getBody()

The body of the request.

###### Returns

`undefined` \| [`Body`](index.md#body)

##### getCreatedAt()

The datetime the request was recorded by the proxy.

###### Returns

`Date`

##### getHeader()

Get a header value.

Header name is case-insensitive.
The header might have multiple values.

###### Parameters

| Parameter | Type |
| ------ | ------ |
| `name` | `string` |

###### Returns

`undefined` \| `string`[]

##### getHeaders()

The headers of the request.

Header names are case-insensitive.
Each header might have multiple values.

###### Returns

`Record`\<`string`, `string`[]\>

###### Example

```json
{
  "Host": ["caido.io"],
  "Connection": ["keep-alive"],
  "Content-Length": ["95"]
}
```

##### getHost()

The target host of the request.

###### Returns

`string`

##### getId()

The unique Caido [ID](index.md#id) of the request.

###### Returns

[`ID`](index.md#id)

##### getMethod()

The HTTP method of the request.

###### Returns

`string`

##### getPath()

The path of the request.

###### Returns

`string`

##### getPort()

The target port of the request.

###### Returns

`number`

##### getQuery()

The unparsed query of the request.

Excludes the leading `?`.

###### Returns

`string`

##### getRaw()

The raw version of the request.

Used to access the bytes directly.

###### Returns

[`RequestRaw`](index.md#requestraw)

##### getTls()

If the request uses TLS (HTTPS).

###### Returns

`boolean`

##### getUrl()

The full URL of the request.

###### Returns

`string`

##### toSpec()

Copied the request to a mutable un-saved [RequestSpec](index.md#requestspec).
This enables you to make modify a request before re-sending it.

###### Returns

[`RequestSpec`](index.md#requestspec)

##### toSpecRaw()

Copied the request to a mutable un-saved [RequestSpecRaw](index.md#requestspecraw).
The raw requests are not parsed and can be used to send invalid HTTP Requests.

###### Returns

[`RequestSpecRaw`](index.md#requestspecraw)

***

### RequestOrderField

> **RequestOrderField**: `"ext"` \| `"host"` \| `"id"` \| `"method"` \| `"path"` \| `"query"` \| `"created_at"` \| `"source"`

Field to order requests by.

***

### RequestRaw

> **RequestRaw**: `object`

An immutable saved raw Request.

#### Type declaration

##### toBytes()

Get the raw request as an array of bytes.

###### Returns

`Uint8Array`

##### toText()

Parse the raw request as a string.

Unprintable characters will be replaced with `�`.

###### Returns

`string`

***

### RequestResponse

> **RequestResponse**: `object`

An immutable saved Request and Response pair.

#### Type declaration

##### request

> **request**: [`Request`](index.md#request-2)

##### response

> **response**: [`Response`](index.md#response-5)

***

### RequestResponseOpt

> **RequestResponseOpt**: `object`

An immutable saved Request and optional Response pair.

#### Type declaration

##### request

> **request**: [`Request`](index.md#request-2)

##### response?

> `optional` **response**: [`Response`](index.md#response-5)

***

### RequestsConnection

> **RequestsConnection**: `object`

A connection of requests.

#### Type declaration

##### items

> **items**: [`RequestsConnectionItem`](index.md#requestsconnectionitem)[]

##### pageInfo

> **pageInfo**: [`PageInfo`](index.md#pageinfo)

***

### RequestsConnectionItem

> **RequestsConnectionItem**: `object`

An item in a connection of requests.

#### Type declaration

##### cursor

> **cursor**: [`Cursor`](index.md#cursor)

##### request

> **request**: [`Request`](index.md#request-2)

##### response?

> `optional` **response**: [`Response`](index.md#response-5)

***

### RequestSendTimeouts

> **RequestSendTimeouts**: `object`

Timeouts for sending a request and receiving a response.

#### Type declaration

##### connect?

> `optional` **connect**: `number`

The timeout to open the TCP connection to the target host
and perform the TLS handshake.

Defaults to 30s.

##### extra?

> `optional` **extra**: `number`

The timeout to read data after we have a read the full response.

This is useful if you believe the server will send more data
than implied by the Content-Length header.

Defaults to 0s (no timeout).

##### global?

> `optional` **global**: `number`

The global timeout for sending a request and receiving a response.

No default value.

##### partial?

> `optional` **partial**: `number`

The timeout between each read attempt for the response.
On a slow connection, this is important to increase.

Defaults to 5s.

##### response?

> `optional` **response**: `number`

The timeout to receive the first byte of the response.

After the first byte is received, the partial timeout will be used.

Defaults to 30s.

***

### RequestsQuery

> **RequestsQuery**: `object`

Query builder to fetch requests.

#### Type declaration

##### after()

Requests after a given cursor.

###### Parameters

| Parameter | Type | Description |
| ------ | ------ | ------ |
| `cursor` | [`Cursor`](index.md#cursor) | [Cursor](index.md#cursor) of the request |

###### Returns

[`RequestsQuery`](index.md#requestsquery)

##### ascending()

###### Call Signature

Ascending ordering.

###### Parameters

| Parameter | Type | Description |
| ------ | ------ | ------ |
| `target` | `"req"` | Target of the ordering: req or resp. |
| `field` | [`RequestOrderField`](index.md#requestorderfield) | Field to order by. |

###### Returns

[`RequestsQuery`](index.md#requestsquery)

###### Call Signature

###### Parameters

| Parameter | Type |
| ------ | ------ |
| `target` | `"resp"` |
| `field` | [`ResponseOrderField`](index.md#responseorderfield) |

###### Returns

[`RequestsQuery`](index.md#requestsquery)

##### before()

Requests before a given cursor.

###### Parameters

| Parameter | Type | Description |
| ------ | ------ | ------ |
| `cursor` | [`Cursor`](index.md#cursor) | [Cursor](index.md#cursor) of the request |

###### Returns

[`RequestsQuery`](index.md#requestsquery)

##### descending()

###### Call Signature

Descending ordering.

###### Parameters

| Parameter | Type | Description |
| ------ | ------ | ------ |
| `target` | `"req"` | Target of the ordering: req or resp. |
| `field` | [`RequestOrderField`](index.md#requestorderfield) | Field to order by. |

###### Returns

[`RequestsQuery`](index.md#requestsquery)

###### Call Signature

###### Parameters

| Parameter | Type |
| ------ | ------ |
| `target` | `"resp"` |
| `field` | [`ResponseOrderField`](index.md#responseorderfield) |

###### Returns

[`RequestsQuery`](index.md#requestsquery)

##### execute()

Execute the query.

###### Returns

`Promise`\<[`RequestsConnection`](index.md#requestsconnection)\>

###### Throws

If a query parameter is invalid or the query cannot be executed.

##### filter()

Filter requests.

###### Parameters

| Parameter | Type | Description |
| ------ | ------ | ------ |
| `filter` | `string` | HTTPQL filter |

###### Returns

[`RequestsQuery`](index.md#requestsquery)

##### first()

First n requests.

###### Parameters

| Parameter | Type | Description |
| ------ | ------ | ------ |
| `n` | `number` | Number of requests to return |

###### Returns

[`RequestsQuery`](index.md#requestsquery)

##### last()

Last n requests.

###### Parameters

| Parameter | Type | Description |
| ------ | ------ | ------ |
| `n` | `number` | Number of requests to return |

###### Returns

[`RequestsQuery`](index.md#requestsquery)

***

### RequestsSDK

> **RequestsSDK**: `object`

The SDK for the Requests service.

#### Type declaration

##### get()

Get a request by its unique [ID](index.md#id).

###### Parameters

| Parameter | Type |
| ------ | ------ |
| `id` | [`ID`](index.md#id) |

###### Returns

`Promise`\<`undefined` \| [`RequestResponseOpt`](index.md#requestresponseopt)\>

###### Example

```js
await sdk.requests.get("1");
```

##### inScope()

Checks if a request is in scope.

###### Parameters

| Parameter | Type |
| ------ | ------ |
| `request` | [`Request`](index.md#request-2) \| [`RequestSpec`](index.md#requestspec) |

###### Returns

`boolean`

###### Example

```js
if (sdk.requests.inScope(request)) {
 sdk.console.log("In scope");
}
```

##### matches()

Checks if a request/response matches an HTTPQL filter.

###### Parameters

| Parameter | Type | Description |
| ------ | ------ | ------ |
| `filter` | `string` | HTTPQL filter |
| `request` | [`Request`](index.md#request-2) | The [Request](index.md#request-2) to match against |
| `response`? | [`Response`](index.md#response-5) | The [Response](index.md#response-5) to match against |

###### Returns

`boolean`

##### query()

Query requests of the current project.

###### Returns

[`RequestsQuery`](index.md#requestsquery)

###### Example

```js
const page = await sqk.requests.query().first(2).execute();
sdk.console.log(`ID: ${page.items[1].request.getId()}`);
```

##### send()

Sends an HTTP request, either a [RequestSpec](index.md#requestspec) or [RequestSpecRaw](index.md#requestspecraw).

This respects the upstream proxy settings.

###### Parameters

| Parameter | Type |
| ------ | ------ |
| `request` | [`RequestSpec`](index.md#requestspec) \| [`RequestSpecRaw`](index.md#requestspecraw) |
| `options`? | [`RequestSendOptions`](index.md#requestsendoptions) |

###### Returns

`Promise`\<[`RequestResponse`](index.md#requestresponse)\>

###### Throws

If the request cannot be sent.
If the request times out, the error message will contain the word "Timeout".

###### Example

```js
const spec = new RequestSpec("https://example.com");
try {
  const res = await sdk.requests.send(request)
  sdk.console.log(res.request.getId());
  sdk.console.log(res.response.getCode());
} catch (err) {
  sdk.console.error(err);
}
```

***

### Response

> **Response**: `object`

An immutable saved Response.

#### Type declaration

##### getBody()

The body of the response

###### Returns

`undefined` \| [`Body`](index.md#body)

##### getCode()

The status code of the response.

###### Returns

`number`

##### getCreatedAt()

The datetime the response was recorded by the proxy.

###### Returns

`Date`

##### getHeader()

Get a header value.

Header name is case-insensitive.
The header might have multiple values.

###### Parameters

| Parameter | Type |
| ------ | ------ |
| `name` | `string` |

###### Returns

`undefined` \| `string`[]

##### getHeaders()

The headers of the response.

Header names are case-insensitive.
Each header might have multiple values.

###### Returns

`Record`\<`string`, `string`[]\>

###### Example

```json
{
  "Date": ["Sun, 26 May 2024 10:59:21 GMT"],
  "Content-Type": ["text/html"]
}
```

##### getId()

The unique Caido [ID](index.md#id) of the response.

###### Returns

[`ID`](index.md#id)

##### getRaw()

The raw version of the response.

Used to access the bytes directly.

###### Returns

[`ResponseRaw`](index.md#responseraw)

##### getRoundtripTime()

The time it took to send the request and receive the response in milliseconds.

###### Returns

`number`

***

### ResponseOrderField

> **ResponseOrderField**: `"length"` \| `"roundtrip"` \| `"code"`

Field to order responses by.

***

### ResponseRaw

> **ResponseRaw**: `object`

An immutable saved raw Response.

#### Type declaration

##### toBytes()

Get the raw response as an array of bytes.

###### Returns

`Uint8Array`

##### toText()

Parse the raw response as a string.

Unprintable characters will be replaced with `�`.

###### Returns

`string`

***

### SetBodyOptions

> **SetBodyOptions**: `object`

Options when setting the body of a Request.

#### Type declaration

##### updateContentLength

> **updateContentLength**: `boolean`

Should update the Content-export type header.

###### Default

```ts
true
```

## Findings

### DedupeKey

> **DedupeKey**: `string` & `object`

A deduplication key.

#### Type declaration

##### \_\_dedupeKey?

> `optional` **\_\_dedupeKey**: `never`

***

### Finding

> **Finding**: `object`

A saved immutable Finding.

#### Type declaration

##### getDedupeKey()

The deduplication key of the finding.

###### Returns

`undefined` \| [`DedupeKey`](index.md#dedupekey)

##### getDescription()

The description of the finding.

###### Returns

`undefined` \| `string`

##### getId()

The unique Caido [ID](index.md#id) of the finding.

###### Returns

[`ID`](index.md#id)

##### getReporter()

The name of the reporter.

###### Returns

`string`

##### getRequestId()

The ID of the associated [Request](index.md#request-2).

###### Returns

`string`

##### getTitle()

The title of the finding.

###### Returns

`string`

***

### FindingSpec

> **FindingSpec**: `object`

A mutable Finding not yet created.

#### Type declaration

##### dedupeKey?

> `optional` **dedupeKey**: [`DedupeKey`](index.md#dedupekey)

Deduplication key for findings.
If a finding with the same dedupe key already exists, it will not be created.

##### description?

> `optional` **description**: `string`

The description of the finding.

##### reporter

> **reporter**: `string`

The name of the reporter.
It will be used to group findings.

##### request

> **request**: [`Request`](index.md#request-2)

The associated [Request](index.md#request-2).

##### title

> **title**: `string`

The title of the finding.

***

### FindingsSDK

> **FindingsSDK**: `object`

The SDK for the Findings service.

#### Type declaration

##### create()

Creates a new Finding.

###### Parameters

| Parameter | Type |
| ------ | ------ |
| `spec` | [`FindingSpec`](index.md#findingspec) |

###### Returns

`Promise`\<[`Finding`](index.md#finding)\>

###### Throws

If the request cannot be saved.

###### Example

```js
await sdk.findings.create({
  title: "Title",
  description: "Description",
  reporter: "Reporter",
  dedupeKey: `${request.getHost()}-${request.getPath()}`,
  request,
});
```

##### exists()

Check if a [Finding](index.md#finding) exists.
Similar to `get`, but returns a boolean.

###### Parameters

| Parameter | Type |
| ------ | ------ |
| `input` | [`GetFindingInput`](index.md#getfindinginput) |

###### Returns

`Promise`\<`boolean`\>

###### Example

```js
await sdk.findings.exists("my-dedupe-key");
```

##### get()

Try to get a [Finding](index.md#finding) for a request.

Since a request can have multiple findings, this will return the first one found.
You can also filter by reporter to get a specific finding.

Finally, you can use a deduplication key to get a specific finding.

###### Parameters

| Parameter | Type |
| ------ | ------ |
| `input` | [`GetFindingInput`](index.md#getfindinginput) |

###### Returns

`Promise`\<`undefined` \| [`Finding`](index.md#finding)\>

###### Example

```js
await sdk.findings.get({
 reporter: "Reporter",
 request,
});
```

***

### GetFindingInput

> **GetFindingInput**: [`DedupeKey`](index.md#dedupekey) \| \{ `reporter`: `string`; `request`: [`Request`](index.md#request-2); \}

Input to get a [Finding](index.md#finding).

#### Type declaration

[`DedupeKey`](index.md#dedupekey)

\{ `reporter`: `string`; `request`: [`Request`](index.md#request-2); \}

##### reporter?

> `optional` **reporter**: `string`

The name of the reporter.

##### request

> **request**: [`Request`](index.md#request-2)

The associated [Request](index.md#request-2).

## Replay

### ReplayCollection

> **ReplayCollection**: `object`

A collection of replay sessions.

#### Type declaration

##### getId()

The unique Caido [ID](index.md#id) of the replay collection.

###### Returns

[`ID`](index.md#id)

##### getName()

The name of the replay collection.

###### Returns

`string`

***

### ReplaySDK

> **ReplaySDK**: `object`

The SDK for the Replay service.

#### Type declaration

##### createSession()

###### Parameters

| Parameter | Type |
| ------ | ------ |
| `source`? | [`RequestSource`](index.md#requestsource) |
| `collection`? | [`ID`](index.md#id) \| [`ReplayCollection`](index.md#replaycollection) |

###### Returns

`Promise`\<[`ReplaySession`](index.md#replaysession)\>

##### getCollections()

###### Returns

`Promise`\<[`ReplayCollection`](index.md#replaycollection)[]\>

***

### ReplaySession

> **ReplaySession**: `object`

A replay session.

#### Type declaration

##### getId()

The unique Caido [ID](index.md#id) of the replay session.

###### Returns

[`ID`](index.md#id)

##### getName()

The name of the replay session.

###### Returns

`string`

## Projects

### Project

> **Project**: `object`

A saved immutable Project.

#### Type declaration

##### getId()

The unique Caido [ID](index.md#id) of the project.

###### Returns

[`ID`](index.md#id)

##### getName()

The name of the project.

###### Returns

`string`

##### getPath()

The directory where the project is located.

###### Returns

`string`

##### getStatus()

The status of the project.

###### Returns

[`ProjectStatus`](index.md#projectstatus)

##### getVersion()

The version of the project.
The format is `MAJOR.MINOR.PATCH`.

###### Returns

`string`

***

### ProjectsSDK

> **ProjectsSDK**: `object`

The SDK for the Projects service.

#### Type declaration

##### getCurrent()

Get the currently selected [Project](index.md#project) if any.

###### Returns

`Promise`\<`undefined` \| [`Project`](index.md#project)\>

###### Example

```js
await sdk.projects.getCurrent();
```

***

### ProjectStatus

> **ProjectStatus**: `"ready"` \| `"restoring"` \| `"error"`

A [Project](index.md#project) status.

## Shared

### Bytes

> **Bytes**: `string` \| `number`[] \| `Uint8Array`

Types that can be converted to bytes in inputs.

***

### Cursor

> **Cursor**: `string` & `object`

A cursor for pagination.

#### Type declaration

##### \_\_cursor?

> `optional` **\_\_cursor**: `never`

***

### ID

> **ID**: `string` & `object`

A unique identifier.

#### Type declaration

##### \_\_id?

> `optional` **\_\_id**: `never`

***

### RawOption

> **RawOption**: `object`

Option to return raw value

#### Type declaration

##### raw

> **raw**: `true`

***

### RequestSource

> **RequestSource**: [`ID`](index.md#id) \| [`Request`](index.md#request-2) \| [`RequestSpec`](index.md#requestspec) \| [`RequestSpecRaw`](index.md#requestspecraw)

The source of a request.

## Environment

### EnvironmentSDK

> **EnvironmentSDK**: `object`

The SDK for the Environment service.

#### Type declaration

##### getVar()

Get the value of an environment variable.

###### Parameters

| Parameter | Type | Description |
| ------ | ------ | ------ |
| `name` | `string` | The name of the environment variable. |

###### Returns

`undefined` \| `string`

The value of the environment variable.

##### getVars()

Get all the environment variables.
It includes the global environment and the selected environment.
Those variables can change over time so avoid caching them.

###### Returns

[`EnvironmentVariable`](index.md#environmentvariable)[]

An array of [EnvironmentVariable](index.md#environmentvariable)

##### setVar()

Sets an environment variable to a given value.
This will override any existing value.
The environment variable can be set either on the currently
selected environment or the global environment.

###### Parameters

| Parameter | Type |
| ------ | ------ |
| `input` | [`SetVarInput`](index.md#setvarinput) |

###### Returns

`Promise`\<`void`\>

###### Throws

If trying to set when a project is not selected.

###### Throws

If trying to set when an environment is not selected (with `global: false`).

###### Example

```js
await sdk.env.setVar({
  name: "USER_SECRET",
  value: "my secret value",
  secret: true,
  global: false
});
```

***

### EnvironmentVariable

> **EnvironmentVariable**: `object`

A saved immutable Finding.

#### Type declaration

##### isSecret

> `readonly` **isSecret**: `boolean`

If the environment variable is a secret

##### name

> `readonly` **name**: `string`

The name of the environment variable

##### value

> `readonly` **value**: `string`

The value of the environment variable

***

### SetVarInput

> **SetVarInput**: `object`

Input for the `setVar` of [EnvironmentSDK](index.md#environmentsdk).

#### Type declaration

##### env?

> `optional` **env**: `string`

The `name` of the Environment to set the variable on.
This will take precedence over the `global` flag if provided.

##### global

> **global**: `boolean`

If the environment variable should be set on the global
environment or the currently selected environment.
By default, it will be set globally.

###### Default

```ts
true
```

##### name

> **name**: `string`

Name of the environment variable

##### secret

> **secret**: `boolean`

If the environment variable should be treated as secret.
Secrets are encrypted on the disk.

###### Default

```ts
false
```

##### value

> **value**: `string`

Value of the environment variable

## GraphQL

### GraphQLSDK

> **GraphQLSDK**: `object`

The SDK for the GraphQL service.

#### Type declaration

##### execute()

Executes a GraphQL query.

###### Type Parameters

| Type Parameter |
| ------ |
| `T` |

###### Parameters

| Parameter | Type |
| ------ | ------ |
| `query` | `string` |
| `variables`? | `Record`\<`string`, `any`\> |

###### Returns

`Promise`\<[`GraphQLResponse`](index.md#graphqlresponset)\<`T`\>\>

###### Example

```js
await sdk.graphql.execute(`
  query {
    viewer
  }
`);
```

## Other

### Console

> **Console**: `object`

Console interface for logging.

Currently logs are only available in the backend logs.
See the [documentation](https://docs.caido.io/report_bug.html#1-backend-logs) on how to retrieve them.

#### Type declaration

##### debug()

Log a message with the debug level.

Usually used for troubleshooting purposes.

###### Parameters

| Parameter | Type |
| ------ | ------ |
| `message` | `any` |

###### Returns

`void`

##### error()

Log a message with the error level.

Usually used for critical errors.

###### Parameters

| Parameter | Type |
| ------ | ------ |
| `message` | `any` |

###### Returns

`void`

##### log()

Log a message with the info level.

Usually used for general information.

###### Parameters

| Parameter | Type |
| ------ | ------ |
| `message` | `any` |

###### Returns

`void`

##### warn()

Log a message with the warn level.

Usually used for unexpected behaviors.

###### Parameters

| Parameter | Type |
| ------ | ------ |
| `message` | `any` |

###### Returns

`void`

***

### GraphQLError

> **GraphQLError**: `object`

#### Type declaration

##### extensions

> **extensions**: `Record`\<`string`, `any`\>

##### locations

> **locations**: [`GraphQLLocation`](index.md#graphqllocation)[]

##### message

> **message**: `string`

##### path

> **path**: [`GraphQLPathSegment`](index.md#graphqlpathsegment)[]

***

### GraphQLLocation

> **GraphQLLocation**: `object`

#### Type declaration

##### column

> **column**: `number`

##### line

> **line**: `number`

***

### GraphQLPathSegment

> **GraphQLPathSegment**: `string` \| `number`

***

### GraphQLResponse\<T\>

> **GraphQLResponse**\<`T`\>: `object`

#### Type Parameters

| Type Parameter |
| ------ |
| `T` |

#### Type declaration

##### data?

> `optional` **data**: `T`

##### errors?

> `optional` **errors**: [`GraphQLError`](index.md#graphqlerror)[]

***

### PageInfo

> **PageInfo**: `object`

Information on the current page of paginated data.

#### Type declaration

##### endCursor

> **endCursor**: [`Cursor`](index.md#cursor)

##### hasNextPage

> **hasNextPage**: `boolean`

##### hasPreviousPage

> **hasPreviousPage**: `boolean`

##### startCursor

> **startCursor**: [`Cursor`](index.md#cursor)

***

### RequestSendOptions

> **RequestSendOptions**: `object`

#### Type declaration

##### save?

> `optional` **save**: `boolean`

If true, the request and response will be saved to the database
and the user will see them in the Search tab.

If you do not save, the request and response IDs will be set to 0.

###### Default

```ts
true
```

##### timeouts?

> `optional` **timeouts**: [`RequestSendTimeouts`](index.md#requestsendtimeouts) \| `number`

The timeouts to use for sending a request and receiving a response.

If a number is provided, it will be used as the global timeout and
the other timeouts will be set to infinity.

See the [RequestSendTimeouts](index.md#requestsendtimeouts) for the default values.

## Runtime

### RuntimeSDK

> **RuntimeSDK**: `object`

The SDK for the runtime information.

#### Type declaration

##### version

###### Get Signature

> **get** **version**(): `string`

Get the current version of Caido.

###### Returns

`string`

## Scope

### Scope

> **Scope**: `object`

A saved immutable Scope.

#### Type declaration

##### allowlist

> `readonly` **allowlist**: `string`[]

The allowlist of the scope.

##### denylist

> `readonly` **denylist**: `string`[]

The denylist of the scope.

##### id

> `readonly` **id**: [`ID`](index.md#id)

The unique Caido [ID](index.md#id) of the scope.

##### name

> `readonly` **name**: `string`

The name of the scope.

***

### ScopeSDK

> **ScopeSDK**: `object`

The SDK for the Scope service.

#### Type declaration

##### getAll()

Get all the scopes.

###### Returns

`Promise`\<[`Scope`](index.md#scope)[]\>

An array of [Scope](index.md#scope)



Directory structure:
└── reference/
    ├── burp_vs_caido.md
    ├── cli.md
    ├── command_shortcuts.md
    ├── context_menu.md
    ├── data_storage.md
    ├── download_links.md
    ├── httpql.md
    ├── index.md
    ├── match_replace.md
    ├── workflow_data_types.md
    └── workflow_nodes.md

================================================
FILE: src/reference/burp_vs_caido.md
================================================
---
description: "A side-by-side reference of common Burp Suite features and where to find their counterparts in Caido."
---

# Burp Suite vs Caido

This page provides a mapping of Burp Suite features to their counterparts in Caido.

## Tools

| Burp Suite | Caido |
|------------|-------|
| Dashboard | [Plugins](/quickstart/plugins.md) |
| Target | [Sitemap](/quickstart/sitemap.md)/[Scopes](/quickstart/scopes.md)/[Findings](/quickstart/findings.md) |
| Burp's browser | [Using a Preconfigured Browser](/guides/preconfigured_browser.md) |
| Proxy | [Intercept](/quickstart/intercept.md)/[HTTP History](/quickstart/http_history.md)/[WS History](/quickstart/ws_history.md)/[Match & Replace](/quickstart/match_replace.md) |
| Scanner | [Scanner](https://github.com/caido-community/scanner) |
| Intruder | [Automate](/quickstart/automate.md) |
| Repeater | [Replay](/quickstart/replay.md) |
| Decoder | [Convert Workflows](/concepts/workflows_intro.md#convert-workflows) |
| Comparer | [Compare](https://github.com/amrelsagaei/Compare) |
| Logger | [Search](/quickstart/search.md)/[Cerebrum](https://github.com/DewSecOff/Caido-Plugin-Cerebrum) |
| Collaborator | [QuickSSRF](https://github.com/caido-community/quickssrf)/[OmniOAST](https://github.com/hahwul/OmniOAST) |
| Search | [HTTPQL](/reference/httpql.md) |
| Organizer | [Findings](/quickstart/findings.md) |
| Filter settings | [Filters](/quickstart/filters.md) |

## Extensions

::: info
The functionality of many Burp Suite Bambdas, custom scan checks, and extensions can be implemented using [workflows](http://localhost:5173/concepts/workflows_intro.html) in Caido or by [defining checks for the Scanner plugin](https://github.com/caido-community/scanner#check-definition).
:::

| Burp Suite | Caido |
|------------|-------|
| Param Miner | [ParamFinder](https://github.com/bebiksior/ParamFinder) |
| JWT Editor | [JWT Analyzer](https://github.com/amrelsagaei/JWT-Analyzer) |
| JS Miner | [Data Grep](https://github.com/caido-community/data-grep) |
| Active Scan++ | [Scanner: Custom Checks](https://github.com/caido-community/scanner#check-definition) |
| Content Type Converter | [Convert Tools](https://github.com/caido-community/convert-tools) |
| Logger++ | [Search](/guides/search_filtering.md) |
| Hackvertor | [Convert Workflows](/concepts/workflows_intro.html#convert-workflows) |
| 403 Bypasser | [403Bypasser](https://github.com/bebiksior/Caido403Bypasser) |
| InQL | [GraphQL Analyzer](https://github.com/amrelsagaei/GraphQL-Analyzer) |
| Autorize/Auth Analyzer | [Autorize](https://github.com/caido-community/autorize) |
| Auth Analyzer | [Authify](https://github.com/saltify7/Authify) |
| Bypass WAF| [Passive Workflows](/concepts/workflows_intro.html#passive-workflows) |
| Reflected Parameters | [Passive Workflows](/concepts/workflows_intro.html#passive-workflows) |
| Sensitive Discoverer | [Passive Workflows](/concepts/workflows_intro.html#passive-workflows) |
| Additional Scanner Checks | [Scanner: Custom Checks](https://github.com/caido-community/scanner#check-definition)/[Passive Workflows](/concepts/workflows_intro.html#passive-workflows) |
| CORS*, Additional CORS Checks | [Scanner: Custom Checks](https://github.com/caido-community/scanner#check-definition)/[Passive Workflows](/concepts/workflows_intro.html#passive-workflows) |
| Request Minimizer | [Squash](https://github.com/evanconnelly/squash) |
| Add Custom Header | [Add a Header Workflow](/tutorials/add_header.md) |
| CSP Auditor | [CSP Auditor](https://github.com/GangGreenTemperTatum/csp-auditor) |
| AuthMatrix | [AuthMatrix](https://github.com/caido-community/authmatrix) |
| AWS Signer | [Resign AWS Requests Workflow](/tutorials/aws_signature.md) |
| Notes | [Notes++](https://github.com/caido-community/NotesPlusPlus) |
| YesWeBurp | [YesWeCaido](https://github.com/yeswehack/yeswecaido) |
| Burp Share Requests | [Drop](https://github.com/caido-community/drop) |

## AI

| Burp Suite | Caido |
|------------|-------|
| Using Burp AI in Repeater | [Shift](https://github.com/caido-community/shift) |
| Generating AI-powered explanations | [Prompting the Assistant to Explain Requests](/guides/assistant_explain.md) |
| Automating tasks with custom actions | [Shift](https://github.com/caido-community/shift) |

::: tip Additional Caido AI Plugins

- [Chatio](https://github.com/amrelsagaei/Chatio)
- [Ebka AI Assistant](https://github.com/Slonser/Ebka-Caido-AI)
:::



================================================
FILE: src/reference/cli.md
================================================
---
description: "Find detailed reference information on Caido CLI command-line options and flags for advanced configuration and troubleshooting."
---

# CLI Options

To view the options available to the Caido CLI, use `-h` or `--help`.

``` txt
Options:
  -l, --listen <ADDR:PORT>                         Listening address
      --invisible                                  Enable invisible mode for all listeners
      --proxy-listen <ADDR:PORT>                   Proxy listening addresses
      --ui-listen <ADDR:PORT>                      UI listening addresses
      --ui-domain <UI_DOMAIN>                      Allowed domains for UI
      --no-open                                    Do not open the UI a browser tab
      --debug                                      Record and display debug logs
      --reset-cache                                Reset the instance cache of cloud data
      --reset-credentials                          Reset the instance credentials (DANGEROUS)
      --data-path <DATA_PATH>                      Directory to store data
      --no-logging                                 Disable file logging
      --no-renderer-sandbox                        Disable sandboxing for the renderer
      --import-ca-cert <IMPORT_CA_CERT>            Import CA certificate
      --import-ca-cert-pass <IMPORT_CA_CERT_PASS>  Import CA certificate password
      --allow-guests                               Allow login as guest
  -h, --help                                       Print help (see more with '--help')
  -V, --version                                    Print version
```



================================================
FILE: src/reference/command_shortcuts.md
================================================
---
description: "Find detailed reference information on Caido keyboard shortcuts and commands for efficient navigation and operation across all interfaces."
---

# Command Shortcuts

::: tip
To set, unset, or change shortcut keybindings, view the [Creating Shortcuts](/guides/shortcuts.md) guide.
:::

::: info
Additional commands may be available depending on the Plugins you have installed.
:::

## Automate

| Command          | Description                                     | Default Keybinding | macOS Keybinding |
|------------------|-------------------------------------------------|--------------------|------------------|
| Send to Automate | Send the currently focused request to Automate. | `CTRL` + `M`       | `⌘` + `M`        |

## Editor

| Command       | Description                                     | Default Keybinding | macOS Keybinding |
|---------------|-------------------------------------------------|--------------------|------------------|
| Search        | Search within the currently focused request/response. | `CTRL` + `F`       | `⌘` + `F`        |
| Cancel Search | Close the search interface.                       | `ESC`              | `ESC`            |
| Undo          | Undo an edit to a request/response.               | `CTRL` + `Z`       | `⌘` + `Z`        |
| Redo          | Redo an edit to a request/response.               | `CTRL` + `SHIFT` + `Z` | `⌘` + `SHIFT` + `Z` |

## Findings

| Command          | Description                | Default Keybinding | macOS Keybinding |
|------------------|----------------------------|--------------------|------------------|
| Send to Findings | Manually create a finding. |                    |                  |

## Intercept

| Command  | Description                        | Default Keybinding | macOS Keybinding |
|----------|-----------------------------------|--------------------|------------------|
| Drop     | Drop an intercepted request/response. |                    |                  |
| Forward  | Forward an intercepted request/response. | `CTRL` + `;`       | `⌘` + `;`        |

## Miscellaneous

| Command                | Description                                     | Default Keybinding | macOS Keybinding |
|------------------------|-------------------------------------------------|--------------------|------------------|
| Close Tab              | Close the currently focused tab.                |                    |                  |
| Reload Window          | Refreshes Caido and reloads all components.     |                    |                  |
| Toggle Command Palette | Open/close the command palette window.          | `CTRL` + `K`       | `⌘` + `K`        |
| Toggle Sidebar         | Open/close the command palette window.          |                    |                  |

## Navigation

| Command               | Description                                     | Default Keybinding | macOS Keybinding |
|-----------------------|-------------------------------------------------|--------------------|------------------|
| Go to Assistant       | Navigate to the Assistant interface.            |                    |                  |
| Go to Automate        | Navigate to the Automate interface.             | `CTRL` + `SHIFT` + `A` | `⌘` + `SHIFT` + `A` |
| Go to Exports         | Navigate to the Exports interface.              |                    |                  |
| Go to Files           | Navigate to the Files interface.                |                    |                  |
| Go to Filters         | Navigate to the Filters interface.              |                    |                  |
| Go to HTTP History    | Navigate to the HTTP History interface.         | `CTRL` + `\|`      | `⌘` + `\|`       |
| Go to Intercept       | Navigate to the Intercept interface.            |                    |                  |
| Go to Match & Replace | Navigate to the Match & Replace interface.      |                    |                  |
| Go to Plugins         | Navigate to the Plugins interface.              |                    |                  |
| Go to Replay          | Navigate to the Replay interface.               | `CTRL` + `SHIFT` + `R` | `⌘` + `SHIFT` + `R` |
| Go to Scope           | Navigate to the Scope interface.                |                    |                  |
| Go to Search          | Navigate to the Search interface.               |                    |                  |
| Go to Settings        | Navigate to the application settings interface. |                    |                  |
| Go to Sitemap         | Navigate to the Sitemap interface.              |                    |                  |
| Go to Workflows       | Navigate to the Workflows interface.            |                    |                  |
| Go to Workspace       | Navigate to the Workspace interface.            |                    |                  |
| Go to WS History      | Navigate to the WS History interface.           |                    |                  |
| Next Tab              | Navigate to the next tab from the currently selected tab. | `CTRL` + `]`       | `⌘` + `]`        |
| Previous Tab          | Navigate to the previous tab from the currently selected tab. | `CTRL` + `[`       | `⌘` + `[`        |

## Proxy

| Command                   | Description                | Default Keybinding | macOS Keybinding |
|---------------------------|----------------------------|--------------------|------------------|
| Toggle Proxy Interception | Enable/disable interception. | `CTRL` + `P`       | `⌘` + `P`        |

## Replay

| Command           | Description                                     | Default Keybinding | macOS Keybinding |
|-------------------|-------------------------------------------------|--------------------|------------------|
| Select Next Entry | Go forward through the request session history. |                    |                  |
| Select Previous Entry | Go backward through the request session history. |                    |                  |
| Send Request      | Forward the request.                            | `CTRL` + `ENTER`   | `⌘` + `ENTER`    |
| Send to Replay    | Send the currently focused request to Replay.   | `CTRL` + `R`       | `⌘` + `R`        |

## Request

| Command           | Description                                     | Default Keybinding | macOS Keybinding |
|-------------------|-------------------------------------------------|--------------------|------------------|
| Copy URL          | Copy the request URL to your clipboard.         |                    |                  |
| Go to Stream      | Navigate to the WebSocket stream view for the current request. |                    |                  |
| Replay in Browser | Copy the request to your clipboard.             |                    |                  |
| Show in Browser   | Copy the response data to your clipboard.       |                    |                  |

## Runtime

| Command           | Description                | Default Keybinding | macOS Keybinding |
|-------------------|----------------------------|--------------------|------------------|
| Toggle Logs Panel | Enable/disable interception. |                    |                  |

## Table

| Command           | Description                | Default Keybinding | macOS Keybinding |
|-------------------|----------------------------|--------------------|------------------|
| Select Next Row   | Move downward through table rows. | `DOWN ARROW`       | `DOWN ARROW`     |
| Select Previous Row | Move upward through table rows. | `UP ARROW`         | `UP ARROW`       |



================================================
FILE: src/reference/context_menu.md
================================================
---
description: "Find detailed reference information on all context menu options available in Caido interfaces for request manipulation and workflow operations."
---

# Context Menu Options

| Option | Description |
|--------|-------------|
| Copy   | Copies the highlight selected text to your clipboard. |
| Copy as cURL | Copies a request as a curl command to your clipboard. |
| Copy URL | Copies a request URL to your clipboard. |
| Send to Replay | Sends a request to the Replay interface. Hovering over this option will allow you to specify the collection to add the request to. |
| Add session | Creates a new request. |
| Delete sessions | Deletes the specified number of request in a collection. |
| Move | Moves a request to a different collection. |
| Close | Closes a request tab. |
| Close Others | Closes all other request tabs besides the one selected. |
| Close to the Left | Closes all other request tabs to the left of the one selected. |
| Close to the Right | Closes all other request tabs to the right of the one selected. |
| Close All | Closes all request tabs. |
| Send to Automate | Sends a request to the Automate interface. |
| Send to Findings... | Sends a request and response pair to the findings interface. Selecting this option will present a window in which you can enter finding details. |
| Replay in browser | Copies a request to your clipboard as a URL. This request includes any modifications that have been made and can be entered into your browser while actively proxying traffic. |
| View response in browser | Copies a URL to your clipboard that allows you to view a response in your browser while actively proxying traffic. |
| Highlight | Color highlights a request's table row. |
| Add in Scope | Adds a request's host as in scope to either an existing or new scope preset. |
| Add out of Scope | Adds a request's host as out of scope to either an existing or new scope preset. |
| Convert (Preview) | Displays a preview of the result of a convert workflow on a selection. |
| Convert (Replace) | Replaces a selection with the result of a convert workflow. |
| Run workflow | Executes an active workflow. |
| Assistant | Prompts the Assistant to either explain a request or generate a CSRF proof-of-concept. |
| Set request | Generates a corresponding request to a URL. |
| Toggle GET/POST | Toggles a request between GET and POST methods. |
| Plugins | Plugin specific options. These will vary depending on which plugins are installed. |
| Select | Loads the associated project. |
| Rename | Allows you to rename an entity. |
| Duplicate | Creates a copy of an entity. |
| Copy path | Copies an entity's file system location to your clipboard. |
| Create backup | Creates a backup of a project. |
| Restore | Recreates a project from a backup. |
| Download | Downloads a backup. |
| Delete... | Deletes an entity. |
| Delete selected | Deletes all selected entities. |
| Delete all... | Deletes all related entities. |



================================================
FILE: src/reference/data_storage.md
================================================
---
description: "Find detailed reference information on Caido's internal file structure, storage locations, and database organization across different operating systems."
---

# Data Storage

All the data Caido creates is stored in a single directory. The default location of this directory is dependent on your operating system:

| OS      | Location                                         |
| ------- | ------------------------------------------------ |
| Linux   | `~/.local/share/caido`                           |
| MacOS   | `~/Library/Application\ Support/io.caido.Caido/` |
| Windows | `%APPDATA%\caido\Caido\data`                     |

::: info
The `/logs` subdirectory stores the log files that contain the output from workflow nodes using the [Workflow SDK](https://developer.caido.io/reference/sdks/workflow/).
:::

## Structure

::: danger
We do not recommend modifying the files directly as this might result in problems in the application and/or corruption of data. Proceed at your own risk.
:::

### Files

- `config.db`: Contains all the non-critical configurations of the instance and the cached data from the cloud for offline support.
- `secrets.db`: Contains all the sensitive configurations. Currently, it is AES encrypted with a static secret, but we plan to support a user-specified password in the future.
- `projects.db`: Contains the metadata of the projects and hosted files.

::: info
Each file is a sqlite3 database in `journal` mode. We usually use pretty recent sqlite3 versions, but we do not make any guarantees on exactly which.
:::

### Subdirectories

- `files`: Hosted files that have been uploaded to your instance.
- `browsers`: The binary of the browser used for rendering.
- `projects`: The data for each project. Each subdirectory name is the UUID of the project.

For each project, you will see the following:

- `database.caido`: The majority of the data of the project is contained in that database.
- `database_raw.caido`: Contains the raw data of the requests and responses, it is split for performance reasons.
- `exports`: Folder containing the exported data.

::: info
Each file is a sqlite3 database in `wal` mode. If you copy them, ensure to also copy the `-wal` files.
:::



================================================
FILE: src/reference/download_links.md
================================================
---
description: "Find detailed reference information on Caido download links API and file formats for automated download systems and third-party integrations."
---

# Download

The download links of Caido are hosted under the domain `caido.download`.

::: warning NOTE
You may encounter outdated Google Cloud bucket links. These are deprecated and should not be used.
:::

## Latest

To obtain the latest release links, use `GET https://caido.download/releases/latest`.

The API will return JSON data resembling:

```json
{
  "id": "01J4KSCQQFY1E9SWEEKJ1WMJWD",
  "version": "0.47.3",
  "links": [
    {
      "display": "Linux x86_64",
      "platform": "linux-x86_64",
      "kind": "cli",
      "link": "https://caido.download/releases/v0.47.3/caido-cli-v0.47.3-linux-x86_64.tar.gz",
      "os": "linux",
      "arch": "x86_64",
      "format": "tar.gz",
      "hash": "gu9MUK4jnHZSQUENeP+29JXz79kPaJO8QHZlagSxLdNJ1qaC3IRwTbcLeU+g2M10WGsdWlrwua6meL1gYQ3tYw=="
    },
    {
      "display": "macOS Desktop x86_64",
      "platform": "mac-x86_64",
      "kind": "desktop",
      "link": "https://caido.download/releases/v0.47.3/caido-desktop-v0.47.3-mac-x86_64.dmg",
      "os": "macos",
      "arch": "x86_64",
      "format": "dmg",
      "hash": "1Be/o7cHKaEGELuq24d0yonI9TRCwlWLfzviafYVXKT6RUZ4YBdfI2RNAqZJ6jz+ViLj02XgVciTATJHn2c7xA=="
    },
    {
      "display": "Windows Desktop x86_64",
      "platform": "win-x86_64",
      "kind": "desktop",
      "link": "https://caido.download/releases/v0.47.3/caido-desktop-v0.47.3-win-x86_64.exe",
      "os": "windows",
      "arch": "x86_64",
      "format": "exe",
      "hash": "p8Rr3wOe3Fbm7eETOogP0ulpifeDFAm+gVxDVItuK4B5wbAOgqqjwZEKoJArcDnAclvmVRtOAQlSXM7dg+amZA=="
    }
    // ... Other links
  ],
  "released_at": "2025-03-27T19:52:00.851138Z"
}
```

| Field | Description |
|-------|-------------|
| `display` | The display name. |
| `platform` | (Deprecated) Operating system (`linux`/`mac`/`win`) + `-` + architecture (`x86_64`/`aarch64`). |
| `kind` | Either `desktop` or `cli` ([CLI vs Desktop](/concepts/essentials/cli_vs_desktop.md)). |
| `link` | The download link. |
| `os` | The operating system of the binary (`linux`/`macos`/`windows`). |
| `arch` | The architecture of the binary (`x86_64`/`aarch64`). |
| `format` | The archive/binary format (`zip`/`tar.gz`/`deb`/`AppImage`/`dmg`/`exe`). |
| `hash` | The Base64-encoded SHA512 hash of the file (may be `null` for older releases). |

::: info
If you prefer a file-based hash, we also build `[link].sha256` and `[link].sha512` files for each binary.
These are hex encoded and will produce the same output as `shasum -a 256` and `shasum -a 512`.
:::

::: warning
The download links **will redirect** to a signed URL, ensure your download client follows redirects.
:::



================================================
FILE: src/reference/httpql.md
================================================
---
description: "Find detailed reference information on HTTPQL query language used in Caido for filtering requests and responses with namespaces, fields, and operators."
---

# HTTPQL

HTTPQL is the query language used in Caido that gives you the ability to filter traffic. The constructing primitives of an HTTPQL filter clause, in order of position, are the:

1. [Namespace](#namespaces)
2. [Field](#fields)
3. [Operator](#operators)
4. [Value](#values)

<img width="500" alt="Parts of a filter clause" src="/_images/httpql_clause.png" no-shadow center/>

::: tip
The development of fields is ongoing. To request a field, [submit a templated issue.](https://github.com/caido/caido/issues/new?template=feature.md&title=New%20HttpQL%20field:)
:::

<div class="video small">
  <iframe src="https://www.youtube.com/embed/0SxdQVjzRss?si=7bb3aoxU8anKV4Sc" title="YouTube video player." frameborder="0"></iframe>
</div>

## Namespaces

::: info
Namespaces are project-specific.
:::

| Namespace | Description |
|-----------|-------------|
| `req` | All proxied HTTP requests. |
| `resp` | All proxied HTTP responses. |
| `preset` | Filter presets. |
| `row` | A request's numerical identifier in the traffic tables. |
| `source` | The Caido feature source (only available in the Search interface). |

::: warning NOTE
The `preset` and `source` namespaces do not have any fields available and instead take direct values.
:::

## Fields

### req

| Available Fields | Description | Value Type |
|------------------|-------------|------------|
| `created_at` | The date and time the request was sent. | Date/Time: [RFC3339](https://datatracker.ietf.org/doc/html/rfc3339) (`2024-06-24T17:03:48+00:00`) / [ISO 8601](https://datatracker.ietf.org/doc/html/rfc3339#appendix-A) (`2024-06-24T17:03:48+0000`) / [RFC2822](https://datatracker.ietf.org/doc/html/rfc2822) (`Mon, 24 Jun 2024 17:03:48 +0000`) / [RFC7231](https://datatracker.ietf.org/doc/html/rfc7231#section-7.1.1.2) (`Mon, 24 Jun 2024 17:03:48 GMT`) / [ISO9075](https://dev.mysql.com/doc/refman/8.0/en/date-and-time-functions.html#function_get-format) (`2024-06-24T17:03:48Z`) |
| `ext` | The extension of the requested file. | String/Byte |
| `host` | The value of the request's `Host` header. | String/Byte |
| `len` | The request size in bytes (includes request line, headers, and body data). | Integer |
| `method` | The HTTP method used for the request. | String/Byte |
| `path` | The URL path (includes files). | String/Byte |
| `port` | The port of the target server. | Integer |
| `query` | The URL query string (excludes the leading `?`). | String/Byte |
| `raw` | The full raw data of the request (includes request line, headers, and body data). | String/Byte |
| `tls` | If the connection used TLS/SSL encryption. | Boolean (`true`/`false`) |

### resp

| Available Fields | Description | Value Type |
|------------------|-------------|------------|
| `code` | The status code of the reponse. | Integer |
| `len` | The response size in bytes (includes response line, headers, and body data). | Integer |
| `raw` | The full raw data of the response (includes response line, headers, and body data). | String/Byte |
| `roundtrip` | The total request/response cycle time (in milliseconds). | Integer |

### row

| Available Field | Description | Value Type |
|------------------|-------------------|------------|
| `id` | The numerical identifier of a request's traffic table row. | Integer |

## Operators

| Operator | Description | Value Type | Additional Details |
|----------|-------------|------------|-------------------|
| `eq` | Equal to the supplied value. | String/Byte, Integer | Case sensitive. Requires leading `.` character for `ext` field. |
| `gt` | Greater than the supplied value. | Date/Time, Integer | |
| `gte` | Greater than or equal to the supplied value. | Integer | |
| `lt` | Less than the supplied value. | Date/Time, Integer | |
| `lte` | Less than or equal to the supplied value. | Integer | |
| `ne` | Not equal to the supplied value. | String/Byte, Integer | Case sensitive. Requires leading `.` character for `ext` field. |
| `cont` | Contains the supplied value. | String/Byte | Case insensitive. |
| `like` | The [SQLite LIKE Operator](https://www.sqlite.org/lang_expr.html#the_like_glob_regexp_match_and_extract_operators). | String/Byte | Case sensitive for Unicode characters beyond the ASCII range. |
| `ncont` | Does not contain the supplied value. | String/Byte | Case insensitive. |
| `nlike` | The [SQLite NOT LIKE Operator](https://www.sqlite.org/lang_expr.html#the_like_glob_regexp_match_and_extract_operators). | String/Byte | Case sensitive for Unicode characters beyond the ASCII range. |
| `regex` | Matches to the regular expression. | String/Byte | Rust-flavored syntax. |
| `nregex` | Does not match to the regular expression. | String/Byte | Rust-flavored syntax. |

::: tip
In SQLite - the `%` character matches zero or more characters (_`%.js` matches `.map.js`_) and the `_` character matches one character (_`v_lue` matches `vAlue`_). Visit [https://regex101.com/](https://regex101.com/) and select **Rust** syntax to test regular expressions.
:::

::: warning NOTE
Not all regex features are currently supported by Caido (_such as look-ahead expressions_) as they are not included in the regex library of Rust.
:::

## Values

### preset

| Available Values | Example |
|------------------|---------|
| A filter preset's alias. | `preset:"no-images"` |
| A filter preset's name. | `preset:"No Images"` |

### source

| Available Values | Additional Details | Example |
|------------------|--------------------|---------|
| `automate`, `intercept`, `plugin`, `replay`, `workflow` | Requires lowercase. Autocomplete is not supported. | `source:"plugin"` |

::: warning NOTE
The `source` namespace is only available in the Search interface. If no results are returned, ensure the inclusion of the source is enabled in the [Advanced options](/guides/search_filtering.md) menu.
:::

::: tip
Entering a string (_such as `"my value"`_) into the HTTPQL input field will search across both requests and responses. The supplied string is replaced at runtime by:

```sql
(req.raw.cont:"my value" OR resp.raw.cont:"my value")
```

:::

## Queries

Queries are composed of multiple filter clauses that are combined together using logical operators and logical grouping.

<img width="600" alt="A full HTTPQL Query" src="/_images/httpql_logical.png" no-shadow center/>

### Logical Operators

| Operator | Description |
|----------|-------------|
| AND | Both the left and right clauses must be true. |
| OR | Either the left or right clause must be true. |

::: info
Operators are case insensitive. Both have the **same priority**.
:::

### Logical Grouping

Caido supports the priority of operations: `AND` has a higher priority than `OR`.

- `<Clause1> AND <Clause2> OR <Clause3>` is equivalent to `((<Clause1> AND <Clause2>) OR <Clause3>)`.
- `<Clause1> OR <Clause2> AND <Clause3>` is equivalent to `(<Clause1> OR (<Clause2> AND <Clause3>))`.
- `<Clause1> AND <Clause2> AND <Clause3>` is equivalent to `((<Clause1> AND <Clause2>) AND <Clause3>)`.

::: tip
While parentheses are optional, we recommend using them to make your logical grouping clear.
:::



================================================
FILE: src/reference/index.md
================================================
---
description: "Find detailed reference information on Caido shortcuts, workflow nodes, HTTPQL, and other features."
---

# Reference

The Reference section provides precise, factual resources to help you use Caido effectively.

It’s designed for quick lookups, offering detailed technical information without explanations or tutorials. Whether you’re troubleshooting errors, exploring HTTPQL fields, or working with workflow nodes, this section serves as a reliable source for exact details.

Use this section as your go-to resource for detailed technical information about Caido.



================================================
FILE: src/reference/match_replace.md
================================================
---
description: "Find detailed reference information on Caido's Match & Replace feature including request/response sections, actions, matchers, and replacers."
---

# Match & Replace

::: tip
If you're having an issue with your Match & Replace rule not taking affect,
make sure you're looking at the un-prettified version of the request/response body by pressing the `{}` button within any request/response pane to ensure your spacing is correct.
:::

## Request Sections

| Section | Target |
|---------|-------------|
| Request Path | The path of a request. |
| Request Method | The HTTP method of a request. |
| Request Query | The query of a request. |
| Request First Line | The first line of a request. |
| Request Header | The header or headers of a request. |
| Request Body | The body data of a request. |

## Response Sections

| Section | Target |
|---------|-------------|
| Response First Line | The first line of a response. |
| Response Status Code | The HTTP status code of a response. |
| Response Header | The header or headers of a response. |
| Response Body | The body data of a response. |

## Request Query Section Actions

| Action | Description |
|--------|-------------|
| Update Raw | Makes modifications to the query as a whole. |
| Update Param | Matches against a query parameter key name and modifies its value. |
| Add Param | Appends an additional query parameter. |
| Remove Param | Removes a query parameter by key name. |

## Request Header/Response Header Section Actions

| Action | Description |
|--------|-------------|
| Update Raw | Makes modifications to the headers as a whole. |
| Update Value | Matches against a header's key name and modifies its value. |
| Add | Inserts a new header key-value pair. |
| Remove | Removes a header by key name. |

## Matcher

| Matcher | Description |
|---------|-------------|
| Full | Matches against the entire section will be replaced. If there are multiple section items, such as when dealing with headers, all instances will be replaced. |
| Regex | Matches against Rust flavor regular expressions. |
| String | Matches against string values. |

::: warning NOTE
Caido does not currently support look-around and backreference regular expressions.
:::

::: tip
To test your regular expressions, visit [regex101.com](https://regex101.com/).
:::

## Replacer

| Replacer | Description |
|----------|-------------|
| Term | Replaces the match with a string value. |
| Workflow | Applies a workflow to the match. |



================================================
FILE: src/reference/workflow_data_types.md
================================================
---
description: "Find detailed reference information on workflow node data types and their compatibility conversions in Caido workflow automation."
---

# Workflow Node Data Types

Nodes are defined by various different input and output data types.

When referencing a node's data for use in another, the types must be compatible with each other.

## Data Type Conversions

Data can be shared across nodes as long as the types are `Exact` (expected) or are `Compatible` based on the following conversions:

::: tip
You can view the data type by clicking on a node and viewing the value within the parenthesis. This will be above the reference data drop-down menu.
<img alt="Node reference drop-down menu." src="/_images/node_reference_selection.png" center no-shadow/>
:::

::: info
[View the SDK for the types here.](https://developer.caido.io/reference/sdks/workflow/#data)
:::

### String

Strings are compatible with:

| Type | Description |
|------|-------------|
| String: Choice | Variation of string. |
| String: Code | Variation of string. |
| Bytes | Encoded as UTF-8 with lossy conversion (invalid characters are replaced with `�`). |
| Bool | Converts to `"true"` or `"false"`. |
| Integer | Base-10 decimal encoding. |

### Bytes

Bytes are compatible with:

| Type | Description |
|------|-------------|
| String | UTF-8 encoded bytes. |
| Bool | Converts to `"true"` or `"false"` in bytes. |
| Integer | First converts to string type and then to UTF-8 encoded bytes. |

### Bool

Booleans are compatible with:

| Type | Description |
|------|-------------|
| Integer | Is `true` if integer is not zero - otherwise `false`. |
| Bytes/String | Is `true` for `"true"`, `"on"`, `"yes"`, and `"1"` - otherwise `false`. |

### Integer

Integers are compatible with:

| Type | Description |
|------|-------------|
| Bool | Is `true` if integer is `1` - `false` if `0`. |
| Bytes | Converted to string loosely, supports hex (`0x`), binary (`0b`), octal (`0o`), supports sign (`+`, `-`). |
| String | Parsed from string, supports hex (`0x`), binary (`0b`), octal (`0o`), supports sign (`+`, `-`). |

### Request & Responses

There is no conversion besides their own.



================================================
FILE: src/reference/workflow_nodes.md
================================================
---
description: "Find detailed reference information on Caido workflow nodes including JavaScript, Shell, If/Else, and other automation components."
---

# Workflow Nodes

## Passive Workflow Nodes

| Node | Description |
|------|-------------|
| On Intercept Request | Triggers a workflow when a request passes through the proxy. |
| On Intercept Response | Triggers a workflow when a response passes through the proxy. |
| Passive End | Ends the passive workflow. |
| If/Else | Branches off based on the conditional output of a previous node. |
| If/Else Javascript | Branches off based on a JavaScript condition. |
| Javascript | Runs JavaScript. |
| Shell | Runs a shell command. |
| Check Finding | Checks if a finding already exists. |
| Create Finding | Reports a finding to the system. |
| In Scope | Checks if a request is in-scope. |
| Matches HTTPQL | Matches a request/response against an HTTPQL query. |
| Set Color | Sets the traffic table request row color. |

## Active Workflow Nodes

| Node | Description |
|------|-------------|
| Active Start | Starts the active workflow. |
| Active End | Ends the active workflow. |
| If/Else | Branches off based on the conditional output of a previous node. |
| If/Else Javascript | Branches off based on a JavaScript condition. |
| Javascript | Runs JavaScript. |
| Shell | Runs a shell command. |
| Check Finding | Checks if a finding already exists. |
| Create Finding | Reports a finding to the system. |
| In Scope | Checks if a request is in-scope. |
| Matches HTTPQL | Matches a request/response against an HTTPQL query. |
| Set Color | Sets the traffic table request row color. |

## Convert Workflow Nodes

| Node | Description |
|------|-------------|
| Convert Start | Starts conversion. |
| Convert End | Ends conversion. |
| If/Else | Branches off based on the conditional output of a previous node. |
| If/Else Javascript | Branches off based on a JavaScript condition. |
| Javascript | Runs JavaScript. |
| Shell | Runs a shell command. |
| Base64 Decode | Converts Base64-encoded data back to original format. |
| Base64 Encode | Converts data to Base64-encoded format. |
| Hex Decode | Converts hexadecimal strings back to original data. |
| Hex Encode | Converts data to hexadecimal format. |
| HTML Decode | Converts HTML entities back to original characters. |
| HTML Encode | Converts text to HTML-safe encoded format. |
| Join | Joins two elements. |
| JSON Minify | Minifies JSON input. |
| JSON Prettify | Prettifies JSON input. |
| JWT Decode | Base64 decodes the header and payload segments of JSON Web Tokens. |
| Match & Replace | Match and replace on input. |
| MD5 Hash | Hashes input using MD5 algorithm. |
| SHA1 Hash | Hashes input using SHA1 algorithm. |
| SHA2 Hash | Hashes input using SHA2 algorithm. |
| Trim | Trims input string. |
| URL Decode | Converts URL-encoded text back to original characters. |
| URL Encode | Converts text to URL-safe encoded format. |



