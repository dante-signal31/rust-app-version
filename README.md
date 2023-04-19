![GitHub release (latest SemVer)](https://img.shields.io/github/v/release/dante-signal31/rust-app-version)
[![License](https://img.shields.io/badge/License-BSD%203--Clause-blue.svg)](https://opensource.org/licenses/BSD-3-Clause)
[![GitHub issues](https://img.shields.io/github/issues/dante-signal31/rust-app-version)](https://github.com/dante-signal31/rust-app-version/issues)
[![GitHub commit activity](https://img.shields.io/github/commit-activity/y/dante-signal31/rust-app-version)](https://github.com/dante-signal31/rust-app-version/commits/main)
[![GitHub last commit](https://img.shields.io/github/last-commit/dante-signal31/rust-app-version)](https://github.com/dante-signal31/markdown2man/commits/main)

# rust-app-version
Get your current app version reading it from Cargo.toml.

I use this action to create automatically release for my pushed rust apps with that version as a tag.

This Action has been used as an example in [this tutorial](https://www.dlab.ninja/2021/12/how-to-create-your-own-custom-actions.html) 
about how to develop your own custom Actions.

## Inputs

**Optional:**
* *cargo_toml_folder*: Folder path where Cargo.toml can be found. Defaults to project root folder.

## Outputs
* *app_version*: App version as it is registered at Cargo.toml file.

## Usage

```yaml
    - name: Get current rust app version from its Cargo.toml.
      id: foo
      uses: dante-signal31/rust-app-version@v1.1.0
      with:
         cargo_toml_folder: rust_app_folder/
         
    - name: Use that version to do something funny.
      shell: bash
      run: echo "Current app version is ${{ steps.foo.outputs.app_version }}"
```

Be aware that you can use whatever you want as id, I used "foo" just as an example.
