# lib-version
A version-aware library that can can be asked for the version of the library.

## How to use:

To install package: 
`pip install remla24-team7-libversion`

### Python example

    import versioning

    from versioning.versioning import VersionUtil

    # Create an instance of VersionUtil
    version_util = VersionUtil()

    # Get the current version of the library
    current_version = version_util.version