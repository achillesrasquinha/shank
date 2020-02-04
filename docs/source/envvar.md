### Environment Variables

| Name                                  | Type                                  | Description |
|---------------------------------------|---------------------------------------|-------------|
| `shank_ACCEPT_ALL_DIALOGS`       | `boolean`                             | Confirm for all dialogs.
| `shank_DRY_RUN`                  | `boolean`                             | Perform a dry-run, avoid updating packages.
| `shank_UPDATE_LATEST`            | `boolean`                             | Update all packages to latest.
| `shank_DISPLAY_FORMAT`           | `string` (table, tree, json, yaml)    | Display packages format.
| `shank_DISPLAY_ALL_PACKAGES`     | `boolean`                             | List all packages.
| `shank_UPDATE_PIP`               | `boolean`                             | Update pip. 
| `shank_INTERACTIVE`              | `boolean`                             | Interactive Mode.
| `shank_GIT_USERNAME`             | `string`                              | Git Username
| `shank_GIT_EMAIL`                | `string`                              | Git Email
| `shank_GITHUB_ACCESS_TOKEN`      | `string`                              | GitHub Access Token
| `shank_GITHUB_REPONAME`          | `string`                              | Target GitHub Repository Name
| `shank_GITHUB_USERNAME`          | `string`                              | Target GitHub Username
| `shank_TARGET_BRANCH`            | `string`                              | Target Branch
| `shank_JOBS`                     | `integer`                             | Number of Jobs to be used.
| `shank_USER_ONLY`                | `boolean`                             | Install to the Python user install directory for environment variables and user configuration.
| `shank_NO_INCLUDED_REQUIREMENTS` | `boolean`                             | Avoid updating included requirements.
| `shank_NO_CACHE`                 | `boolean`                             | Avoid fetching latest updates from PyPI server.
| `shank_FORCE`                    | `boolean`                             | Force search for files within a project.
| `shank_NO_COLOR`                 | `boolean`                             | Avoid colored output.
| `shank_OUTPUT_FILE`              | `string`                              | Output File.